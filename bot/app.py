from flask import Flask, jsonfi, request
from contenedores import *

app = Flask(__name__)

@app.route('/')
def status():
 return jsonfi(status='OK')

@app.route('/prueba')
def prueba():
 return json(getClasificacion())

if __name__ == '__main__':
 
 app.run(host='0.0.0.0', debug=True)
