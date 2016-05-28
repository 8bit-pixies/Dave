library(jsonlite)

test_that("jsonlite loads jsonlines properly", {
  input_dat <- system.file("extdata", "simple.json", package="Dave")
  con_in <- file(input_dat)
  sample_dat <- stream_in(con_in)
  expect_equal(dim(sample_dat), c(2, 4))
})
