import pandas as pd
import numpy as np
import sqlalchemy as sq
from flask import Flask, request,jsonify
import traceback
import json
import xlrd
import xlsxwriter
import os
parentdir = os.getcwd()
app = Flask(__name__)
def Get_input(data):
    while True:
        print(""" Choices :
        1.Search by Movie Name
        2.Search by Movie Year
        3.Search by Number of Awards
        4.Search by IMDB Rating
        5.Close the Session""")
        user_choice = data["userchoice1"]
        if user_choice == "1" :
            movie1 = (input("Enter a Movie Name: ")).lower()
            query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE wordsInTitle LIKE '"+movie1+"'"
            msg = ConnectingToSQL(query)
        elif user_choice == "2" :
            print("""1.Movies Above Year\n2.Movies Below Year""")
            choice2 = input("Enter your Choice : ")
            if choice2 == "1":
                in_year = input("Enter a year : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE year >="+in_year
                msg = ConnectingToSQL(query)
            elif choice2 == "2":
                in_year = input("Enter a year : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE year <="+in_year
                msg = ConnectingToSQL(query)
            else :
                print("Enter a correct Choice")
        elif user_choice == "3" :
            print("""1.Movies Morethan Awards\n2.Movies LessThan Awards""")
            choice3 = input("Enter your Choice : ")
            if choice3 == "1":
                no_of_awards = input("Enter number of Awards : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE nrOfWins >="+no_of_awards
                msg = ConnectingToSQL(query)
            elif choice3 == "2":
                in_year = input("Enter a year : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE nrOfWins <="+no_of_awards
                msg = ConnectingToSQL(query)
            else :
                print("Enter a correct Choice")
        elif user_choice == "4" :
            print("""1.Above Rating\n2.Below Rating""")
            choice = data["userchoice2"]
            if choice == "1":
                rating = data["userchoice3"]
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE imdbRating >="+rating
                msg = ConnectingToSQL(query)
                return msg
            elif choice == "2":
                rating = input("Enter a Rating : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE imdbRating <="+rating
                msg = ConnectingToSQL(query)
            else :
                print("Enter a correct choice")
        elif user_choice == "5":
            break
        else :
            print("Enter a correct Choice")
            continue
def ConnectingToSQL(query):
    try :
        password =''
        host = os.environ['HOST_IP']
        connect_string = f'mysql://root:{password}@{host}/test'
        #host.docker.internal
        #127.0.0.1
        sql_engine = sq.create_engine(connect_string)
    except:
        print("Error in connecting to Database. Check Database Connection")
    try :
        df = pd.read_sql_query(query, sql_engine)

        if df.empty:
            print('No result.')
        else:
            return df
            #base_filename = 'C:\\Users\\Admin\\Desktop\\satya.txt'
            #np.savetxt(base_filename,df.values, fmt='%s\t%s\t%s\t%s',encoding='utf-8',delimiter = ",")
    except ValueError:
        traceback.print_exc()
        print("No Movie Was found for your entries")

@app.route('/movies',methods = ["GET","POST"])
def hello():
    data = request.json
    print(data)
    #print(parentdir)
    df = Get_input(data)
    df.to_excel("./output/movies_out.xlsx",index=False)
    df = df.to_json()
    return jsonify(df)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')