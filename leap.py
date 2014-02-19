# app.py

import sys
import json
import argparse

from flask import (
    Flask, make_response, render_template, jsonify, request
)
from unipath import Path

TEMPLATE_DIR = Path(__file__).ancestor(1).child("templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)


def leap(year=0):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


@app.route('/')
def index():
    """
    Return the main view.
    """
    return render_template('index.html')


@app.route('/api/', methods=['GET'])
def api():
    year = request.args.get('year', 0, type=int)
    return jsonify(
        {
            "success": True,
            "leap": leap(int(year)),
            "year": year,
        }
    )


def main():
    """
    Main entry point for script.
    """
    app.run(debug=True)


if __name__ == '__main__':
    sys.exit(main())