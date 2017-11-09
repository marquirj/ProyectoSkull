#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import Flask, json, request
import json

app = Flask(__name__)


@app.route('/')
def prueba():
 data = {'status': 'OK'}
 return json.dumps(data)

if __name__ == '__main__':
 port = int(os.environ.get('PORT', 5000))
 app.run(host='0.0.0.0', debug=True)
