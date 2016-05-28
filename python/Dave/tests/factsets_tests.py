from nose.tools import assert_equal
from Dave.factset import load_factsets, flatten_dataframe, export_factsets, load_jsonlines


def test_simplejson():    
    factsets = load_factsets("tests/data/simple.json", {'entity': 'id', 'datetime':'as_at'})
    assert_equal(factsets, [{'as_at': '2016-05-28T11:39:00', 'zipcode': '123456', 'id': 'cust_001', 'gender': 'male'}])
    
def test_flatten():
    import pandas as pd
    df = pd.DataFrame({
        'entity' : [1,1],
        'datetime': [1,1],
        'info1': [None, 1],
        'info2': [2, None]
    })    
    assert_equal(flatten_dataframe(df), [{'info1': 1.0, 'datetime': 1.0, 'info2': 2.0, 'entity': 1.0}])

def test_export():
    import json
    assert_equal(export_factsets([{'a':1}]), '{"a": 1}')
