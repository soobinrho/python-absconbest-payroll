import pandas as pd

def read_xlsx(workbook, columns, row, does_require_drop=True): #temporary file
    rawdata=pd.read_excel(
        workbook,
        parse_cols=columns).iloc[:row]
    if(does_require_drop): rawdata=rawdata.dropna()
    return rawdata

    # rawdata = pd.read_excel(
    # 'payroll_management.xlsx',
    # parse_cols='A, B').iloc[:30]

def get_sorted(rawdata, column):
    sorted_data=rawdata.sort_values(
        column,
        ascending=True)
    #rawdata.sort_values('TIM', ascending=True)
    return sorted_data
