import pandas as pd

def create_calendar(input):

    df_input = pd.DataFrame(
        {
            'DATE_IN'     : input['DATE_IN'],
        })

    # input to Datetime
    date_format="%Y-%m-%dZ"
    df = pd.to_datetime(df_input['DATE_IN'], format=date_format)
    
    # WORKAROUND:
    # Tableau Prep Builder only shows data from begin-1 and end-1,
    # there is an offset of one day, therefore we add +1 day in advance
    # Currently no idea how to solve this issue!
    date_begin = df.min() + pd.DateOffset(1)
    date_end  = pd.Timestamp.today().date() + pd.DateOffset(1)
    
    date_range = pd.date_range(date_begin, date_end, freq="D", normalize=True)
    date_range = date_range.date # Datetiem -> Date

    df_return = pd.DataFrame()
    
    for date in date_range:
        d = {"DATE_OUT": str(date)}
        df_return = df_return.append(d, ignore_index=True)
    
    return df_return


def get_output_schema():
    
    return pd.DataFrame(
        {
            'DATE_OUT'     : prep_date(),
        })