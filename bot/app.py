from flask import Flask, jsonify, request
from contenedores import *

app = Flask(__name__)

@app.route('/')
def status():
 return jsonify(status='OK')

@app.route('/prueba')
def prueba():
 return jsonify(getClasificacion())

if __name__ == '__main__':
 
 app.run(host='0.0.0.0', port=5005, debug=True)
