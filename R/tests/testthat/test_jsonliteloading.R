
test_that("jsonlite loads jsonlines properly", {
  input_dat <- system.file("extdata", "simple.json", package="Dave")
  sample_dat <- load_jsonlines(input_dat)
  expect_equal(dim(sample_dat), c(2, 4))
})
