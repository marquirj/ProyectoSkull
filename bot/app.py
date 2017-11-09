from flask import Flask, json, request
from contenedores import *

app = Flask(__name__)

@app.route('/')
def status():
 return json(status='OK')

@app.route('/prueba')
def prueba():
 return json(getClasificacion())

if __name__ == '__main__':
 
 app.run(host='0.0.0.0', debug=True)
