#!/usr/bin/python
# -*- coding:utf-8 -*-

from blog import db

class Category(db.Model):

    __tablename__='b_category'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(10),unique=True)
    content=db.Column(db.String(100))

    def __init__(self,title,content):
        self.title=title
        self.content=content

    def __repr__(self):
        return "<Category %r>" % self.title



class User(db.Model):

    __tablename__='b_user'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),unique=True)
    password=db.Column(db.String(16))

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def __repr__(self):
        return "<User %r>" % self.username