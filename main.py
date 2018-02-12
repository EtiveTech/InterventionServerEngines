#!/usr/bin/env python

from flask import Flask, request, jsonify

from controller.get_data import verifyToken
from controller.mini_planner.engine_one_miniplanner import launch_engine_one, launch_engine_one_Pendulum
from controller.planner.engine_three import launch_engine_three

app = Flask(__name__)

@app.route('/engine_one', methods=['GET', 'POST'])
def e1():
    if (hasattr(request.form, 'token') and verifyToken(request.form['token'])):
        if request.method == 'POST':
            return launch_engine_one_Pendulum(request)
        else:
            return jsonify({'error': 'Not found'}), 404
    else:
        return jsonify({'error': 'Unauthorized'}), 401

@app.route('/engine_three', methods=['GET', 'POST'])
def e2():
    if (hasattr(request.form, 'token') and verifyToken(request.form['token'])):
        if request.method == 'POST':
            return launch_engine_three(request)
        else:
            return jsonify({'error': 'Not found'}), 404
    else:
        return jsonify({'error': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run()