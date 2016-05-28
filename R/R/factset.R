#' Check Schema
#'
#' @param schema is a list containing the entity and datetime column information and optionally the data types for the dataframe
#' @export
check_schema <- function(schema=NULL) {
  if(is.null(schema)){
    return(list(entity="entity", datetime="datetime"))
  }
  if(!("entity" %in% names(schema)) | !("datetime" %in% names(schema))) {
    stop("Schema either does not contain entity or datetime information")
  }
  return(schema)
}

#' Load jsonlines file into a data frame object.
#'
#' @param path is the location of the jsonlines file
#' @export
#' @importFrom jsonlite stream_in
load_jsonlines <- function(path) {
  con_in <- file(path)
  factsets <- stream_in(con_in)
  return(factsets)
}

#' Flattens a dataframe given the entity and date fields
#'
#' @param factsets is the dataframe to be flattened
#' @param schema is the provided schema of the dataframe
#' @importFrom dplyr group_by_ summarise_each funs first
#' @export
flatten_df <- function(factsets, schema=NULL) {
  schema <- check_schema(schema)

  f <- function(.) if(length(unique(.[!is.na(.)])) > 1L) . else first(.[!is.na(.)])
  summarise_each(
    group_by_(factsets, schema[['entity']], schema[['datetime']]),
    funs(f))
}


