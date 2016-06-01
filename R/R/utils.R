#' converts date string vector from iso8601 format
#'
#' @param dates is a vector of date strings
#' @export
to_datetime <- function(dates) { # nocov start
  if (! requireNamespace("xts", quietly = TRUE)) {
    stop("Please install xts: install.packages('xts').")
  }
  return(sapply(dates, function(date) xts::.parseISO8601(date)$first.time))
} # nocov end
