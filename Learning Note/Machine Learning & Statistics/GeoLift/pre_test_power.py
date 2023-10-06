----------------------------------Start-----------------------------
GeoLiftMarketSelection <- function(data,
                                   treatment_periods,
                                   N = c(),
                                   X = c(),
                                   Y_id = "Y",
                                   location_id = "location",
                                   time_id = "time",
                                   effect_size = seq(-0.2, 0.2, 0.05),
                                   lookback_window = 1,
                                   include_markets = c(),
                                   exclude_markets = c(),
                                   holdout = c(),
                                   cpic = 1,
                                   budget = NULL,
                                   alpha = 0.1,
                                   normalize = FALSE,
                                   model = "none",
                                   fixed_effects = TRUE,
                                   dtw = 0,
                                   Correlations = FALSE,
                                   ProgressBar = FALSE,
                                   print = TRUE,
                                   run_stochastic_process = FALSE,
                                   parallel = TRUE,
                                   parallel_setup = "sequential",
                                   side_of_test = "two_sided",
                                   conformal_type = "iid",
                                   ns = 1000,
                                   import_augsynth_from = "library(augsynth)",
                                   import_tidyr_from = "library(tidyr)") {
  if (parallel == TRUE) {
    cl <- build_cluster(
      parallel_setup = parallel_setup,
      import_augsynth_from = import_augsynth_from,
      import_tidyr_from = import_tidyr_from
    )
  }

  message("Calculating which the best treatment groups are.")
  # Part 1: Treatment and pre-treatment periods
  data <- data %>% dplyr::rename(Y = paste(Y_id), location = paste(location_id), time = paste(time_id))
  max_time <- max(data$time)
  data$location <- tolower(data$location)
  include_markets <- tolower(include_markets)
  exclude_markets <- tolower(exclude_markets)

  # Data Checks

  if (any(include_markets %in% exclude_markets)) {
    stop("\ninclude_markets and exclude_markets overlap. Please define where these locations should go.")
  }

  # Small Pre-treatment Periods
  if (max_time / max(treatment_periods) < 4) {
    message(paste0("Caution: Small pre-treatment period!.
                   \nIt's recommended to have at least 4x pre-treatment periods for each treatment period.\n"))
  }

  # Populate N if it's not provided
  if (length(N) == 0) {
    N <- unique(round(quantile(c(1:length(unique(data$location))),
      probs = seq(0, 0.5, 0.1),
      type = 1,
      names = FALSE
    )))

    if (length(include_markets) > 0) {
      # Keep only those equal or larger than included markets
      N <- N[length(include_markets) <= N]
      if (length(N) == 0) {
        stop("All N are smaller than amount of included markets. Please increase N.")
      }
    }
  }

  # More include_markets than N
  if (length(include_markets) > 0 & min(N) < length(include_markets)) {
    message(paste0(
      "Error: More forced markets than total test ones.",
      " Consider increasing the values of N."
    ))
    return(NULL)
  }

  # Check that the provided markets exist in the data.
  if (!all(tolower(include_markets) %in% tolower(unique(data$location)))) {
    message(paste0(
      "Error: One or more markets in include_markets were not",
      " found in the data. Check the provided list and try again."
    ))
    return(NULL)
  }

  # Check that the provided markets exist in the data.
  if (!all(tolower(exclude_markets) %in% tolower(unique(data$location)))) {
    message(paste0(
      "Error: One or more markets in exclude_markets were not",
      " found in the data. Check the provided list and try again."
    ))
    return(NULL)
  }

  #  Check the holdout parameter
  if (length(holdout) > 1) {
    if (length(holdout) > 2) {
      message("Error: Too many arguments in holdout. Provide the min and max holdout sizes.")
      return(NULL)
    } else if (holdout[1] >= holdout[2]) {
      message("Error: The first argument in holdout should be strictly smaller than the second.")
      return(NULL)
    } else if (min(holdout) < 0 | max(holdout > 1)) {
      message("Error: Please specify valid values for holdouts (values from 0 to 1)")
      return(NULL)
    }
  } else if (length(holdout) == 1) {
    message("Error: Too few arguments in holdout. Provide the min and max holdout sizes.")
    return(NULL)
  }

  results <- data.frame(matrix(ncol = 10, nrow = 0))

  # Setting the lookback window to the smallest length of treatment if not provided.
  if (lookback_window <= 0) {
    lookback_window <- 1
  }

  BestMarkets <- MarketSelection(
    data,
    location_id = "location",
    time_id = "time",
    Y_id = "Y",
    dtw = dtw,
    exclude_markets = exclude_markets
  )

  N <- limit_test_markets(BestMarkets, N, run_stochastic_process)

  # Aggregated Y Per Location
  AggYperLoc <- data %>%
    dplyr::group_by(location) %>%
    dplyr::summarize(Total_Y = sum(Y))

  for (n in N) {
    BestMarkets_aux <- stochastic_market_selector(
      n,
      BestMarkets,
      run_stochastic_process = run_stochastic_process
    )

 ------------------------------------END------------------------------------------------
