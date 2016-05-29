# MIT Copyright 2016 Chapman Siu

import json
import pandas as pd # for flattening?

def check_schema(schema):
    '''checks for valid schema'''
    if schema is None:
        schema = {"entity": "entity",
                  "datetime" : "datetime"}
    else:
        if "entity" not in schema.keys() or "datetime" not in schema.keys():
            raise Exception("""Schema must be a dictionary with keys: "entity", "datetime" """)
    return schema
    
def load_jsonlines(path, stream=False):
    '''Loads the jsonlines file either as a stream,
    or through pandas `read_json`. Note that the `read_json` method will
    automatically convert many fields into the correct datatype and 
    should be the preferred method if the data can fit in memory'''
    if stream:
        with open(path) as jsonlines:    
            factsets = pd.DataFrame(json.loads(line) for line in jsonlines)
    else:
        jsonlines = open(path, 'r').readlines()
        json = "[{}]".format(", ".join(jsonlines))
        factsets = pd.read_json(json)
    return factsets
               
def flatten_dataframe(factsets, schema=None, export=None):
    '''takes in list of python dicts, and schema and flattens'''    
    schema = check_schema(schema)
    df = (factsets
                .groupby([schema['datetime'], schema['entity']])
                .agg(lambda x: x.iloc[x.last_valid_index()])
                .reset_index())
    if export is None:
        return df
    if export == 'dict':
        return df.to_dict(orient='records')

# the "main" functions you should be using, the above are helper functions                
def load_factsets(path, schema=None):
    '''
    Read factset in the form of jsonlines, and outputs a flattened
    json, and transforms the datatypes as specified in the schema dictionary
    '''
    schema = check_schema(schema)
    factsets = load_jsonlines(path)
    
    return flatten_dataframe(factsets, schema)
    
def export_factsets(factls, path=None):
    """takes in factset in the form of list of dictionaries, and exports to 
    path (if provided) otherwise dumps it to a string"""
    
    if path is None:
        return '\n'.join([json.dumps(jsonline) for jsonline in factls])
    # check overwriting
    with open(path, 'a') as f:
        for jsonline in factls:
            json.dump(jsonline, f)
            f.write('\n')
    return None
    

