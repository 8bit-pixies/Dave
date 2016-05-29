from Dave.factset import load_factsets, check_schema


def get_snapshot(path_or_df, schema=None, date=None):
    """gets the snapshot of the input data at a particular point in time"""
    if schema is not None and not isinstance(schema, dict):
        raise Exception('Your schema does not have keys, maybe you were trying to set the date parameter')
    schema = check_schema(schema)
    if isinstance(path_or_df, str):
        df = load_factsets(path_or_df, schema)
    else:
        df = path_or_df
    
    if date is not None:
        df = df[df[schema['datetime']] <= date]
    df = (df.sort_values([schema['entity'], schema['datetime']], 
                  ascending=[False, False])
            .groupby(schema['entity'])
            .first()
            .reset_index())       
    return df
        
        