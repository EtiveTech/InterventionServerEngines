#!/usr/bin/env python

from flask import Flask, request, jsonify

from controller.mini_planner.engine_one_miniplanner import launch_engine_one, launch_engine_one_Pendulum
from controller.planner.engine_three import launch_engine_three

app = Flask(__name__)

@app.route('/engine_one', methods=['GET', 'POST'])
def e1():
    if request.method == 'POST':
        return launch_engine_one_Pendulum(request)
    else:
        return jsonify({'error': 'Not found'}), 404

@app.route('/engine_three', methods=['GET', 'POST'])
def e2():
    if request.method == 'POST':
        return launch_engine_three(request)
    else:
        return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run()