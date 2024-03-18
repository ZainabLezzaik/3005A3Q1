import psycopg2

#this function will connect to the db
def get_DB_connection():
    try:
      connection = psycopg2.connect(
          host="localhost",
          database="schoolDatabase",
          user="postgres",
          password="change29"
      )
      return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while trying to connect to PostgreSQL", error)
        exit(1)