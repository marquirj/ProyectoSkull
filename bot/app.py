from flask import Flask, jsonfy, request
from contenedores import *

app = Flask(__name__)

@app.route('/')
def status():
 return jsonfy(status='OK')

@app.route('/prueba')
def prueba():
 return jsonfy(getClasificacion())

if __name__ == '__main__':
 
 app.run(host='0.0.0.0', debug=True)
