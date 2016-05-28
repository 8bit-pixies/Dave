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


