import pandas as pd
import numpy as np
import sqlalchemy as sq
import traceback

def Get_input():
    while True:
        print(""" Choices :
        1.Search by Movie Name
        2.Search by Movie Year
        3.Search by Number of Awards
        4.Search by IMDB Rating
        5.Close the Session""")
        user_choice = input("Enter your Choice : ")
        if user_choice == "1" :
            movie1 = (input("Enter a Movie Name: ")).lower()
            query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE wordsInTitle LIKE '"+movie1+"'"
            ConnectingToSQL(query)
        elif user_choice == "2" :
            print("""1.Movies Above Year\n2.Movies Below Year""")
            choice2 = input("Enter your Choice : ")
            if choice2 == "1":
                in_year = input("Enter a year : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE year >="+in_year
                ConnectingToSQL(query)
            elif choice2 == "2":
                in_year = input("Enter a year : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE year <="+in_year
                ConnectingToSQL(query)
            else :
                print("Enter a correct Choice")
        elif user_choice == "3" :
            print("""1.Movies Morethan Awards\n2.Movies LessThan Awards""")
            choice3 = input("Enter your Choice : ")
            if choice3 == "1":
                no_of_awards = input("Enter number of Awards : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE nrOfWins >="+no_of_awards
                ConnectingToSQL(query)
            elif choice3 == "2":
                in_year = input("Enter a year : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE nrOfWins <="+no_of_awards
                ConnectingToSQL(query)
            else :
                print("Enter a correct Choice")
        elif user_choice == "4" :
            print("""1.Above Rating\n2.Below Rating""")
            choice = input("Enter your Choice : ")
            if choice == "1":
                rating = input("Enter a Rating : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE imdbRating >="+rating
                ConnectingToSQL(query)
            elif choice == "2":
                rating = input("Enter a Rating : ")
                query = "SELECT title,year,imdbRating,nrOfWins FROM mytable WHERE imdbRating <="+rating
                ConnectingToSQL(query)
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
        connect_string = f'mysql://root:{password}@127.0.0.1/samle'
        sql_engine = sq.create_engine(connect_string)
    except:
        print("Error in connecting to Database. Check Database Connection")
    try :
        df = pd.read_sql_query(query, sql_engine)

        if df.empty:
            print('No result.')
        else:
            print(df)
            base_filename = 'C:\\Users\\Admin\\Desktop\\satya.txt'
            np.savetxt(base_filename,df.values, fmt='%s\t%s\t%s\t%s',encoding='utf-8',delimiter = ",")
    except ValueError:
        traceback.print_exc()
        print("No Movie Was found for your entries")

Get_input()
