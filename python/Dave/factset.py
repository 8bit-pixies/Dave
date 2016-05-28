# MIT Copyright 2016 Chapman Siu

import json
import pandas as pd # for flattening?
import dateutil.parser

def check_schema(schema):
    '''checks for valid schema'''
    if schema is None:
        schema = {"entity": "entity",
                  "datetime" : "datetime"}
    else:
        if "entity" not in schema.keys() or "datetime" not in schema.keys():
            raise Exception("""Schema must be a dictionary with keys: "entity", "datetime" """)
    return schema
    
def load_jsonlines(path):
    with open(path) as jsonlines:    
        factsets = pd.DataFrame(json.loads(line) for line in jsonlines)
    return factsets
               
def flatten_dataframe(factsets, schema=None):
    '''takes in list of python dicts, and schema and flattens'''    
    schema = check_schema(schema)
    return (factsets
                .groupby([schema['datetime'], schema['entity']])
                .agg(lambda x: x.iloc[x.last_valid_index()])
                .reset_index()
                .to_dict(orient='records'))

# the "main" functions you should be using, the above are helper functions                
def load_factsets(path, schema=None):
    '''
    Read factset in the form of jsonlines, and outputs a flattened
    json, and transforms the datatypes as specified in the schema dictionary
    '''
    schema = check_schema(schema)
    factsets = load_jsonlines(path)
    factsets[schema['datetime']] = (factsets[schema['datetime']]
                                      .apply(lambda x: dateutil.parser.parse(x).isoformat()))
    # insert other json supported formats
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
    

