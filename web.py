#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from flask import Flask, json, request
import json
import os
app = Flask(__name__)


@app.route('/')
def status():
 data = {'status': 'OK'}
 return json.dumps(data)

if __name__ == '__main__':
 
 app.run(host='0.0.0.0:8000', debug=True)
