from flask import Flask, jsonify
import mysql.connector
from time import sleep


# ! do not take the habit of putting db credentials in the source code
def connect_to_db(database=None):
    mydb = None
    while mydb is None:
        sleep(1)
        try:
            if database is None:
                mydb = mysql.connector.connect(
                    host="mysqldb",
                    user="root",
                    password="p@ssw0rd1"
                )
            else:
                mydb = mysql.connector.connect(
                    host="mysqldb",
                    user="root",
                    password="p@ssw0rd1",
                    database=database
                )
        except Exception as e:
            print("not connected, trying again...")
    return mydb


app = Flask(__name__)

# creation of the DB and tables
mydb = connect_to_db()
cursor = mydb.cursor()
cursor.execute("DROP DATABASE IF EXISTS todos")
cursor.execute("CREATE DATABASE todos")
cursor.execute("USE todos")
cursor.execute("DROP TABLE IF EXISTS todos")
cursor.execute(
    "CREATE TABLE todos (name VARCHAR(255), description VARCHAR(255))"
)
cursor.close()


@app.route('/api')
def base_route():
    return jsonify({
        "msg": "API is up",
        "data": None
    })


@app.route('/api/todos')
def get_todos():
    mydb = connect_to_db("todos")
    cursor = mydb.cursor()
    cursor.execute("USE todos")
    cursor.execute("SELECT * FROM todos")
    # this will extract row headers
    row_headers = [x[0] for x in cursor.description]
    results = cursor.fetchall()
    data = []
    for result in results:
        data.append(dict(zip(row_headers, result)))
    cursor.close()
    return jsonify({
        "msg": "todos fetched",
        "data": data
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
