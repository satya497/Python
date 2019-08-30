import pandas as pd
import numpy as np
import sqlalchemy as sq

def Get_input():
    movie = input("Enter a Movie Name : ")
    movie = movie.lower()
    print(movie)
    return movie
def ConnectingToSQL():
    password =''
    connect_string = f'mysql://root:{password}@127.0.0.1/samle'
    sql_engine = sq.create_engine(connect_string)
    query = "SELECT * FROM mytable WHERE wordsInTitle LIKE %s"
    try:
        df = pd.read_sql_query(query, sql_engine, params=[f'%{movie}%'])
        name = df.ix[0,'title']
        year = df.ix[0,'year']
        rating = df.ix[0,'imdbRating']
        awardsno = df.ix[0,'nrOfWins']
        print(df)
        print("The Name of the Movie :    ",name)
        print("Year :                     ",year)
        print("The IMDB RATING :          ",rating)
        print("The Number of Awards Won : ",awardsno)
    except:
        print ("PLEASE ENTER A VALID MOVIE NAME")
movie = Get_input()
ConnectingToSQL()