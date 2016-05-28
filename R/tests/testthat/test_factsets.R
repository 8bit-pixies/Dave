
test_that("dataframes as flattened corrected", {
  simple_df <- data.frame(a = c(1,1),
                          b = c(1,1),
                          c = c(NA, 2),
                          d = c(3, NA))
  simple_df <- flatten_df(simple_df, list(entity="a", datetime="b"))
  expect_equal(dim(simple_df), c(1,4))
})
