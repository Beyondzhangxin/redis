# coding=utf-8
import pymysql

# database configuration
database_ip = 'localhost'
database_port = '3306'
database_name = 'solar'
user = 'root'
pwd=''

# 插入一条语句，参数为表名称和插入的记录，data为tuple的字符串格式
def insert(table_name,data):
    # connect database
    db = pymysql.connect(database_ip,user,pwd,database_name)

    # use cursor to manipulate
    cursor= db.cursor()

    sql = " insert into "+table_name+" values "+data
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def update(table_name,data_dic):
    # connect database
    db = pymysql.connect(database_ip, user, pwd, database_name)
    # use cursor to manipulate
    cursor = db.cursor()
    for k,v in data_dic.items:
        suffix =+ " " + k + "=" + v + " "

    sql = "alter "+table_name+ " set "+ suffix
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def delete(table_name,where_condition=""):
    # connect database
    db = pymysql.connect(database_ip, user, pwd, database_name)
    # use cursor to manipulate
    cursor = db.cursor()
    sql= "delete from "+table_name
    if where_condition!="":
        sql=+" where " +where_condition
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def read(table_name ,select_data="*", where_condition=""):
    # connect database
    db = pymysql.connect(database_ip, user, pwd, database_name)
    # use cursor to manipulate
    cursor = db.cursor()
    sql = "select "+select_data+" from " + table_name
    if where_condition!="":
        sql=+" where " +where_condition
    try:
        cursor.execute(sql)
        rs=cursor.fetchall()
        return rs
    except:
        print("Error:unable to fetch data ")
    db.close()


def check_connect():
    db = pymysql.connect(database_ip,user,pwd,database_name)
    print(db)
    db.close()