import mysql.connector


def read_test_data_from_db():
    test_data = []

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="users"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM user")

    myresult = mycursor.fetchall()
    for t in myresult:
        test_data.append(list(t))
    return test_data
