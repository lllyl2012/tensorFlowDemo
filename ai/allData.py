import pymysql
import requests
import json
import pandas as pd

db = pymysql.connect("183.131.126.142:60008","ydb","ydb_yiyun_2018","yidongban" )


def getAll():
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = ""
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            ql_inner_code = row[0]
            legal_state = row[1]
            person_state = row[2]
            yztb_test = row[3]
            zlb_isexist = row[4]
            matters.append({'ql_inner_code': ql_inner_code, 'legal_state': legal_state, 'person_state': person_state,
                            'yztb_test': yztb_test, 'zlb_isexist': zlb_isexist})
        return matters
    except:
        print("Error: unable to fetch data")