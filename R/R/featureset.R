#' Gets the gradient related information for a period of time
#'
#' @param df is the path of dataframe object of interest
#' @param schema is the schema of the object
#' @param date is the date which we want to filter on.
#'        This can be either a vector, empty, or single date. If it is a vector
#'        it will filter based on this vector, if it is a single date it will take latest entry based
#'        on the date. If it is NULL it will consider the whole time period
#' @param method is the approach on which the data will be subsetted. Can be either snapshot  or left out (will be assumed to be non-snapshot)
#' @export
get_filtered <- function(df, schema=NULL, date=NULL, method="snapshot") UseMethod("get_filtered")

#' Gets the gradient related information for a period of time
#'
#' @param df is the path of dataframe object of interest
#' @param schema is the schema of the object
#' @param date is the date which we want to filter on.
#'        This can be either a vector, empty, or single date. If it is a vector
#'        it will filter based on this vector, if it is a single date it will take latest entry based
#'        on the date. If it is NULL it will consider the whole time period
#' @param method is the approach on which the data will be subsetted. Can be either snapshot  or left out (will be assumed to be non-snapshot)
#' @seealso\code{\link{get_filtered}}
#' @export
get_filtered.character <- function(df, schema=NULL, date=NULL, method="snapshot") {
  factsets <- load_factsets(df, schema)
  return(get_filtered(factsets, schema, date, method))
}


#' Gets the gradient related information for a period of time
#'
#' @param df is the path of dataframe object of interest
#' @param schema is the schema of the object
#' @param date is the date which we want to filter on.
#'        This can be either a vector, empty, or single date. If it is a vector
#'        it will filter based on this vector, if it is a single date it will take latest entry based
#'        on the date. If it is NULL it will consider the whole time period
#' @param method is the approach on which the data will be subsetted. Can be either snapshot  or left out (will be assumed to be non-snapshot)
#' @seealso\code{\link{get_filtered}}
#' @importFrom dplyr group_by_ filter row_number arrange_ n
#' @export
get_filtered.data.frame <- function(df, schema=NULL, date=NULL, method="snapshot") {
  schema <- check_schema(schema)

  if (!is.null(date)) {
    if(length(date) > 1) {
      start_date <- min(date)
      end_date <- max(date)
      df <- df[df[, schema[['datetime']]] <= end_date & df[, schema[['datetime']]] >= start_date,]
    } else {
      df <- df[df[, schema[['datetime']]] <= date,]
    }
  }

  if (method=="snapshot") {
    return(filter(arrange_(group_by_(df, schema[['entity']]), schema[['datetime']]), row_number() == n()))
  } else {
    return(df)
  }
}

#' Convenience function for get filtered
#'
#' @param df is the path of dataframe object of interest
#' @param schema is the schema of the object
#' @param date is the date which we want to filter on.
#'        This can be either a vector, empty, or single date. If it is a vector
#'        it will filter based on this vector, if it is a single date it will take latest entry based
#'        on the date. If it is NULL it will consider the whole time period
#' @seealso\code{\link{get_filtered}}
#' @export
get_snapshot <- function(df, schema=NULL, date=NULL) {
  return(get_filtered(df, schema, date, method="snapshot"))
}

#' Convenience function for get filtered
#'
#' @param df is the path of dataframe object of interest
#' @param schema is the schema of the object
#' @param date is the date which we want to filter on.
#'        This can be either a vector, empty, or single date. If it is a vector
#'        it will filter based on this vector, if it is a single date it will take latest entry based
#'        on the date. If it is NULL it will consider the whole time period
#' @seealso\code{\link{get_filtered}}
#' @export
get_gradient <- function(df, schema=NULL, date=NULL) {
  return(get_filtered(df, schema, date, method="gradient"))
}



