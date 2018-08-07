from flask import (Flask, render_template, flash, redirect, url_for, request, send_from_directory)
import db_connect
import pymysql

web_app = Flask(__name__)

DEBUG = True
PORT = '****'
HOST = '0.0.0.0'

conn = pymysql.connect(db = "all_knowledge",
                    user = "***",
                    passwd = "*******",
                    unix_socket = "*******",
                    port = '****')

cur = conn.cursor()
stuff = cur.execute('SELECT * FROM raspberrypi_commands')
results = str(cur.fetchone())

outpost = 'Command: ' + results

@web_app.route('/')
def main_page():
    return render_template('base.html')

if __name__ == '__main__':
    web_app.run(debug=DEBUG, host=HOST, port=PORT)

