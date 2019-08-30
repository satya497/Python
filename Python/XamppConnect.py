import sqlalchemy as sql
import pandas as pd
def readfile():
    queryfile1 = open(f"C:\\Users\\Admin\\Documents\\python_codes_visual\\query.txt",'r')
    queryout = queryfile1.read()
    queryfile1.close()
    return queryout
def execute_query():
    database='samle'
    host='127.0.0.1'
    user='root'
    password=''
    port='3306'
    query=queryout
    connect_string = f'mysql://{user}:{password}@{host}/{database}'
    sql_engine = sql.create_engine(connect_string)

    try:
        df = pd.read_sql_query(query, sql_engine)
        
    except sql.exc.ResourceClosedError:
        print ("QUERY OTHER THAN SELECT")
    return df
queryout = readfile()
outtable = pd.DataFrame(execute_query())
outtable.to_csv('C:\\Users\\Admin\\Documents\\python_codes_visual\\student.csv', index=False)