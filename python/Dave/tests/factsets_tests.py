from nose.tools import assert_equal, assert_raises
from Dave.factset import load_factsets, flatten_dataframe, export_factsets, load_jsonlines, check_schema


def test_simplejson():
    factsets = load_factsets("Dave/tests/data/simple.json", {'entity': 'id', 'datetime':'as_at'})
    assert_equal(set(factsets.columns), set(['as_at', 'zipcode', 'id', 'gender']))

def test_loadjson():
    factsets_stream = load_jsonlines("Dave/tests/data/simple.json", stream=True)
    factsets_nostream = load_jsonlines("Dave/tests/data/simple.json", stream=False)
    assert_equal(set(factsets_nostream.columns), set(factsets_stream.columns))

def test_flatten():
    import pandas as pd
    df = pd.DataFrame({
        'entity' : [1,1],
        'datetime': [1,1],
        'info1': [None, 1],
        'info2': [2, None]
    })
    assert_equal(flatten_dataframe(df, export='dict'), [{'info1': 1.0, 'datetime': 1.0, 'info2': 2.0, 'entity': 1.0}])

def test_export():
    import json
    assert_equal(export_factsets([{'a':1}]), '{"a": 1}')

def test_schemaexception():
    assert_raises(Exception, check_schema, {'a':1})
