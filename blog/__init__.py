#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app= Flask(__name__)

# import  os
# print os.environ.keys()
# print os.environ.get('FLASK_SETTINGS')

app.config.from_object('blog.setting')
app.config.from_envvar('FLASK_SETTINGS')

db=SQLAlchemy(app)

from .models import Category
from .models import User

import controllers

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


