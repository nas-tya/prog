from flask import Flask, request
import os
import socket
import json
import mysql.connector
import datetime

app = Flask(__name__)
cnt = 0


@app.route('/')
def hello():
    name = os.getenv("NAME", 'world')
    hostname = socket.gethostname()

    global cnt
    cnt += 1

    html = f"""
    <h1>Hello, {name}!</h1>
    <b>Hostname:</b> {hostname} <br>
    <b>The counter:</b> {cnt} <br>
    """
    return html


@app.route('/stat')
def stat():
    headers = str(request.headers['User-Agent'])

    html = """
        <b>Datetime</b>: {d} <br>
        <b>Client User-Agent</b>: {req_headers}"""

    return html.format(d=datetime.datetime.now(), req_headers=headers)


@app.route('/initdb')
def db_init():
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="password")
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS counter")
    cursor.execute("CREATE DATABASE counter")
    cursor.close()

    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="password",
                                   database="counter")
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS logs")
    cursor.execute(
        "CREATE TABLE logs (datetime VARCHAR(255), client_info VARCHAR(255))")
    
    cursor.close()

    return 'init database'


@app.route('/addlog')
def add_log():
    """
    Позволяет вводить данные о посещении
    """
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="password",
                                  database="counter")
    

    client_info = str(request.headers['User-Agent'])

    cursor = mydb.cursor()

    date = datetime.datetime.now()

    try:
        cursor.execute("INSERT INTO logs (client_info, datetime) VALUES (%s, %s)", (client_info, date))
        mydb.commit()
        return "log added"
    except Exception as e:
        mydb.rollback()
        return str(e)
    finally:
        mydb.close()
    


@app.route('/logs')
def get_logs():
    """
    Извлекает данные из таблицы logs
    
    """
    mydb = mysql.connector.connect(host="mysqldb",
                                   user="root",
                                   password="password",
                                   database="counter")
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM logs")

    row_headers = [x[0] for x in cursor.description] # названия полей таблицы

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result))) # с помощью zip соединяем столбцы со значениями, которые в них содержатся, создаем из этого словарь и словарь помещаем в список json_data

    cursor.close()

    return json.dumps(json_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
