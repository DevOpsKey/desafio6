# Configuracao do Flask
from os import environ
from flask import Flask, jsonify, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from rq import Queue
import mysql.connector
import redis


app = Flask(__name__)

@app.route('/')
def hello():
    return {"API": {
        "api": "1.0",
        "dep": {
            "db-sql": banco(),
            "db-nosql": redis2(),
            "fila": fila(),
        },
    }

}
    
def fila():
    try:
        valida = redis.StrictRedis(
        host = '34.204.189.20',
        port = '6379',
        password = 'RBOJ9cCNoGCKhlEBwQLHri1g+atWgn4Xn4HwNUbtzoVxAYxkiYBi7aufl4MILv1nxBqR4L6NNzI0X6cE',
        charset = "utf-8")

        valida.llen('client list')
        print (valida.llen('Fila OK'))
        return "OK"
    except Exception as e:
        print (e)
        return ('Gordinho, a fila ficou Off porque o redis foi para o vinagre')

def banco():
    try:
        con = mysql.connector.connect(host='34.204.189.20',user='root',password='Email12@QW')
        db_info = con.get_server_info()
        print ("Conectada ao servidor Mysql",db_info)
        return "OK"
    except:
        return "Gordinho o banco foi para o vinagre"

def redis2():
    try:
        r = redis.StrictRedis(
        host = '34.204.189.20',
        port = '6379',
        password = 'RBOJ9cCNoGCKhlEBwQLHri1g+atWgn4Xn4HwNUbtzoVxAYxkiYBi7aufl4MILv1nxBqR4L6NNzI0X6cE',
        charset = "utf-8")
        
        r.set('foo','bar')
        print (r.get("foo"))
        return "OK"
    except:
        return "Gordinho o redis foi para o vinagre"
