from flask import render_template, redirect, url_for, flash, session, Response, request,Flask
from config.manager import app
import route.index 



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5001)