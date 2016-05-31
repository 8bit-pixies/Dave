from nose.tools import assert_equal, assert_not_equal, assert_raises, assert_true
from Dave.featureset import get_snapshot, get_gradient, get_filtered
from Dave.factset import flatten_dataframe, load_factsets

def test_snapshotsimple():
    import pandas as pd
    df = pd.DataFrame({
        'entity' : [1,1],
        'datetime': [1,1],
        'info1': [None, 1],
        'info2': [2, None]
    })
    assert_equal(get_snapshot(flatten_dataframe(df)).shape,
                 flatten_dataframe(df).shape)

def test_getfilterpath():
    from pandas import DataFrame
    df_gf = get_filtered("Dave/tests/data/simple.json", {'entity':'id', 'datetime': 'as_at'})
    assert_true(isinstance(df_gf, DataFrame))

def test_snapshotsimple2():
    import pandas as pd
    df = pd.DataFrame({
        'entity' : [1,1,1],
        'datetime': [1,1,2],
        'info1': [None, 1,1],
        'info2': [2, None,1]
    })
    assert_not_equal(get_snapshot(flatten_dataframe(df)).shape,
                     flatten_dataframe(df).shape)

def test_snapshotcond():
    import pandas as pd
    df = pd.DataFrame({
        'entity' : [1,1,1,1],
        'datetime': [1,1,2,3],
        'info1': [None, 1,1,1],
        'info2': [2, None,1,1]
    })
    assert_raises(Exception, get_snapshot, flatten_dataframe(df), 2)
    assert_equal(get_snapshot(flatten_dataframe(df), date=2)['datetime'].max(), 2)
    assert_not_equal(get_snapshot(flatten_dataframe(df), date=2)['datetime'].max(), df['datetime'].max())

def test_gradient():
    import pandas as pd
    df = pd.DataFrame({
        'entity' : [1,1,1,1],
        'datetime': [1,1,2,3],
        'info1': [None, 1,1,1],
        'info2': [2, None,1,1]
    })
    assert_raises(Exception, get_gradient, flatten_dataframe(df), 2)
    assert_equal(get_gradient(flatten_dataframe(df), date=[0,2])['datetime'].max(), 2)
    assert_not_equal(get_gradient(flatten_dataframe(df), date=[0,2])['datetime'].max(), df['datetime'].max())
