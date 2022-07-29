import psycopg2
from psycopg2 import Error
import os
from urllib.parse import urlparse


# Connect to an existing database
db_url = os.getenv("DATABASE_URL")
result = urlparse(db_url)
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port
connection = psycopg2.connect(
                                database = database,
                                user = username,
                                password = password,
                                host = hostname,
                                port = port
                                )
 


def insert(count):
    cur = connection.cursor()
    insert_query = """ 
                    INSERT INTO cmd (SKILL,COUNT) 
                    VALUES ('calc',%s)
                    """
    cur.execute(insert_query,count)
    connection.commit()
    cur.close()

def update(c):
    cur = connection.cursor()
    update_query = """
                    Update cmd
                    set count = %s
                    where skill = 'calc'
                    """
    cur.execute(update_query,(c,))
    connection.commit()
    cur.close()


def retrieve():
    cur = connection.cursor()
    cur.execute("SELECT count FROM cmd ORDER BY count")
    row = cur.fetchone()
    while row is not None:
        count = int(row[0])
        row = cur.fetchone()
    connection.commit()
    cur.close()
    return count
