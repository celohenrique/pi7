import mysql.connector

def sql_insert_data(wh,wht):
    mydb = mysql.connector.connect(
        host="localhost",
        user="myusername",
        password="mypassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO Workers (With Helmet, Without Helmet) VALUES (%s, %s)"
    val = (wh, wht)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
