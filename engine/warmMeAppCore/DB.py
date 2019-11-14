#!/usr/bin/python3
import pymysql

def getDBConnection():
    global con
    con = pymysql.connect('localhost', 'warmme', 'warmme', 'warmme')
    return con
  
def __init__(self):
    self.getDBConnection()