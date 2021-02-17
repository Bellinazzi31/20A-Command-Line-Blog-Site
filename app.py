import dbcreds
import mariadb
import sys

def connect():
    return mariadb.connect(
        host = dbcreds.host,
        port = dbcreds.port,
        username = dbcreds.username,
        password = dbcreds.password,
        database = dbcreds.database
    )
def createBlogPost():
    conn = None
    cursor = None
    conn = connect()
    cursor = conn.cursor()

    try:
        conn = connect()
        cursor = conn.cursor
        content = input("What is on your mind?")
        cursor.execute("INSERT INTO blog_post(username, content, id) VALUES (?, ?, NULL)", [username, content])
        conn.commit()
        print("Post created")
        
    except mariadb.DataError as ex: 
        print("Invalid data", ex)

    else: 
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close() 
def allBlogPost():
    conn = None
    cursor = None
    rows = []

    try:
        conn = connet()
        cursor = conn.cursor()
        cursor.Execute("SELECT * FROM blog_post") 
        rows =cursor.fetchall()
        print("row")
    
    except mariadb.DatabaseError as ex:
        print("There was an error with database", ex)

    else: 
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()

while True:
    print("Welcome to my blog! Add username and make your choise!")            
    username = input("username: ")
    userChoise = input(" 1 = Create a blog post:, 2 = View all post: ")


    if userChoise == "1":
        createBlogPost()
    elif  userChoise == "2":
        allBlogPost()  
    else: 
        print("ERROR")                     