# coding:utf-8

import re
import datetime

db = {}

def newuser(db):
    prompt = 'login desired:'
    while True:
        name = raw_input('Please input the username:')
        if db.has_key(name):
            prompt = 'name taken'
            continue
        else:
            print 'Username should be made of A~Z、a~z、0~9、_'
            continue
        for valuename in db.keys():
            if name.lower() == valuename.lower():
                break
        else:
            break
    passwd = raw_input('Please input the password:')
    db[name] = encodepass(passwd)

    
def olduser(db):
    name = raw_input('Login:')
    if name in db:
        pwd = raw_input('passwd:')
        passwd = db.get(name)
        if passwd == encodepass(pwd):
            print 'Welcome back!',name
            time_order(name)
        else:
            print 'Login incorrent!'
    else:
        YN = raw_input('Do you want to instead a new user? Yes or No:')
        if YN.lower()=='yes':
            newuser(db)

def deluser(db):
    print 'Please login as admin' 
    name = raw_input('Login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    if passwd == encodepass(pwd) and name=='admin':
        user = raw_input('Please input a user name:')
        if user != 'admin':
            if db.pop(user):
                print 'Delete Current!'
        else:
            print 'Con not delete admin!'
    else:
        print 'Wrong passwprd'

def checkuser(db):
    print 'Please login as admin'  
    name = raw_input('Login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    if passwd == encodepass(pwd) and name == 'admin':
        for key in db:
            print 'username: %10s ====> password: %10s' % (key,db[key])
    else:
        print 'You can not check all users'
