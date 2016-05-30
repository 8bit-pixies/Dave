Dave: a framework for a feature store
=====================================

[![Build Status](https://travis-ci.org/Jules-and-Dave/Dave.svg?branch=master)](https://travis-ci.org/Jules-and-Dave/Dave)
[![Coverage Status](http://codecov.io/github/Jules-and-Dave/Dave/coverage.svg?branch=master)](http://codecov.io/github/Jules-and-Dave/Dave?branch=master)

Dave is a feature store (sort of). Simple as that. It stores facts and extracts features.
This version simply demonstrates how this concept works in environments like
`python` and `R`.

Dave is inspired by Ambiata's implementation of Ivory, though treats facts
in a slightly different way.

Concepts
========

Fact sets
---------

Facts in Dave are represented as [`jsonlines`](http://jsonlines.org/) format. It
is also inspired by [entity, attribute, value](https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model),
in order to create a sparse data set.

These attributes can be provided in any number of rows, however each observation
must have at least the entity information (this can be thought of as a key), with
an optional longitude component being time (if applicable)

For example, the following two fact sets are equivalent:

```
{"id": "cust_001", "as_at": "2016-05-28T11:39:+00:00", "gender": "male", "zipcode": "123456"}
```

```
{"id": "cust_001", "as_at": "2016-05-28T11:39:+00:00", "gender": "male"}
{"id": "cust_001", "as_at": "2016-05-28T11:39:+00:00", "zipcode": "123456"}
```

Feature sets
------------

Feature sets can be thought of in two parts of the same picture:

*  Feature engineering
*  Feature extraction

**Feature engineering** may be of interest when you take data over a time range; for
 example if we are interested in duration between events, simply looking at
 snapshot related information may not be sufficient.

 **Feature extraction** is outputting the information which is ingested into a
 (hopefully) [tidy data format](http://vita.had.co.nz/papers/tidy-data.html) for
 machine learning.


License and Copyrights
======================

This library is released under MIT License 2016 Chapman Siu.
