from Dave.factset import load_factsets, check_schema


def get_filtered(path_or_df, schema=None, date=None, method="snapshot"):
    """get gradient related information for a period of time"""
    if schema is not None and not isinstance(schema, dict):
        raise Exception('Your schema does not have keys, maybe you were trying to set the date parameter')
    schema = check_schema(schema)
    if isinstance(path_or_df, str):
        df = load_factsets(path_or_df, schema)
    else:
        df = path_or_df
    
    if date is not None:
        if isinstance(date, list):
            start_date = min(date)
            end_date = max(date)
            df = df[(df[schema['datetime']] <= end_date) & (df[schema['datetime']] >= start_date)]
        else:
            df = df[df[schema['datetime']] <= date]
    
    if method=="snapshot":
        df = (df.sort_values([schema['entity'], schema['datetime']], 
                  ascending=[False, False])
            .groupby(schema['entity'])
            .first()
            .reset_index()) 
       
    # apply transformations (to do)
    return df
    
    

def get_snapshot(path_or_df, schema=None, date=None):
    """gets the snapshot of the input data at a particular point in time"""    
    return get_filtered(path_or_df, schema, date, method="snapshot")

def get_gradient(path_or_df, schema=None, date=None):
    """get gradient related information for a period of time"""
    return get_filtered(path_or_df, schema, date, method="gradient")
    
