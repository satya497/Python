import pandas as pd
import sqlalchemy as sq
import numpy as np

def reading_query():
    df_excel = pd.read_excel("C:\\Users\\Admin\\Documents\\python_codes_visual\\product_details.xlsx")
    df_excel.index = pd.RangeIndex(1,len(df_excel.index)+1)
    df_excel.index.name = 'S.No'
    df_excel = pd.read_excel("C:\\Users\\Admin\\Documents\\python_codes_visual\\product_details.xlsx")
    df_excel.index = pd.RangeIndex(1,len(df_excel.index)+1)
    df_excel.index.name = 'S.No'
    df_excel['EXPECTED']=df_excel['EXPECTED'].str.replace('$','')
    df_excel['ACTUAL']=df_excel['ACTUAL'].str.replace('$','')
    df_excel['EXPECTED']=pd.to_numeric(df_excel.EXPECTED)
    df_excel['ACTUAL']=pd.to_numeric(df_excel.ACTUAL)
    df_excel['DIFFERENCE'] = df_excel['EXPECTED']-df_excel['ACTUAL']
    df_excel['DIFFERENCE'] = np.where(df_excel['DIFFERENCE']<0,'-$'+df_excel['DIFFERENCE'].astype(str).str[1:],'$'+df_excel['DIFFERENCE'].astype(str).str[1:])
    return df_excel

def ConnectingToSQL():
    password =''
    connect_string = f'mysql://root:{password}@127.0.0.1/samle'
    sql_engine = sq.create_engine(connect_string)
    ExcelOut.to_sql("product_details",sql_engine,if_exists ='replace')

ExcelOut = reading_query()
ConnectingToSQL()