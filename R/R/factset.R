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

#' Load factsets is the key function which takes in a jsonline files and flattens, applying
#' all relevant transformations based on the schema.
#'
#' @param path is the path of the jsonlines file
#' @param schema is the schema information
#' @export
load_factsets <- function(path, schema = NULL) {
  schema <- check_schema(schema)
  factsets <- load_jsonlines(path)

  factsets[schema[['datetime']]] <- to_datetime(factsets[schema[['datetime']]])
  return(flatten_df(factsets, schema))
}

#' Export factsets exports the dataframe into a jsonlines file format.
#'
#' @param factset is the data frame to be exported
#' @param path path is the optional path which the file is to be saved
#' @importFrom jsonlite toJSON stream_out
#' @export
export_factsets <- function(factset, path=NULL) {
  if(is.null(path)) {
    jsonlines <- vector("character")
    con <- textConnection('jsonlines', 'wr', local=T)
    stream_out(factset, con=con)
    close(con)
    return(paste0(jsonlines, collapse="\n"))
  } else {
    con_out <- file(path)
    stream_out(factset, con=con_out)
    return(NULL)
  }
}
