

test_that("jsonlite loads jsonlines properly", {
  input_dat <- system.file("extdata", "simple.json", package="Dave")
  sample_dat <- load_jsonlines(input_dat)
  expect_equal(dim(sample_dat), c(2, 4))
})

test_that("dataframes as flattened corrected", {
  simple_df <- data.frame(a = c(1,1),
                          b = c(1,1),
                          c = c(NA, 2),
                          d = c(3, NA))
  simple_df <- flatten_df(simple_df, list(entity="a", datetime="b"))
  expect_equal(dim(simple_df), c(1,4))
})

test_that("export factsets works as expected", {
  expect_equal(export_factsets(data.frame(a=1)), "{\"a\":1}")
})

test_that("check schema correctly returns schema", {
  expect_equal(check_schema(), list(entity="entity", datetime="datetime"))
  expect_error(check_schema(list(a=1)))
})

test_that("load factsets actually loads something", {
  input_dat <- system.file("extdata", "simple.json", package="Dave")
  sample_dat <- load_factsets(input_dat, list(entity='id', datetime='as_at'))
})
