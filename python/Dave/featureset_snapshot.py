from Dave.factset import load_factsets, check_schema


def get_snapshot(path_or_df, schema=None, date=None):
    """gets the snapshot of the input data at a particular point in time"""
    schema = check_schema(schema)
    if isinstance(path_or_df, str):
        df = load_factsets(path_or_df, schema)
    else:
        df = path_or_df
    
    if date is None:
        df = (df.sort_values([schema['entity'], schema['datetime']], 
                      ascending=[False, False])
                .groupby(schema['entity'])
                .first())
    return df.reset_index()
        
        