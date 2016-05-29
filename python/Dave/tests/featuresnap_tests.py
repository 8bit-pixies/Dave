from nose.tools import assert_equal, assert_not_equal
from Dave.featureset_snapshot import get_snapshot
from Dave.factset import flatten_dataframe

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

def test_snapshotsimple():
    import pandas as pd
    df = pd.DataFrame({
        'entity' : [1,1,1],
        'datetime': [1,1,2],
        'info1': [None, 1,1],
        'info2': [2, None,1]
    })    
    assert_not_equal(get_snapshot(flatten_dataframe(df)).shape, 
                     flatten_dataframe(df).shape)

