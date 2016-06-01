

test_that("simple snapshot example", {
  datf <- data.frame(
    entity=c(1,1),
    datetime=c(1,1),
    info1= c(NA, 1),
    info2= c(2, NA)
  )
  expect_equal(dim(get_snapshot(flatten_df(datf))), dim(flatten_df(datf)))
})

test_that("path snapshot example", {
  input_dat <- system.file("extdata", "simple.json", package="Dave")
  df_gf <- get_filtered(input_dat, schema=list(entity='id', datetime='as_at'))
  expect_true(inherits(df_gf, "data.frame"))
})

test_that("more complex snapshot example", {
  datf <- data.frame(
    entity=c(1,1,1,1),
    datetime=c(1,1,2,3),
    info1= c(NA, 1, 1, 1),
    info2= c(2, NA, 1, 1)
  )
  expect_error(get_snapshot(flatten_df(datf), schema=2))
  expect_equal(max(get_snapshot(flatten_df(datf), date=2)$datetime), 2)
  expect_false(isTRUE(all.equal(max(get_snapshot(flatten_df(datf), date=2)$datetime), max(datf$datetime))))
})

test_that("more complex gradient example", {
  datf <- data.frame(
    entity=c(1,1,1,1),
    datetime=c(1,1,2,3),
    info1= c(NA, 1, 1, 1),
    info2= c(2, NA, 1, 1)
  )
  expect_error(get_gradient(flatten_df(datf), schema=c(0, 2)))
  expect_equal(max(get_gradient(flatten_df(datf), date=c(0, 2))$datetime), 2)
  expect_equal(min(get_gradient(flatten_df(datf), date=c(0, 2))$datetime), 1)
})
