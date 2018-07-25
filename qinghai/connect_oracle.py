# coding=utf-8
import cx_Oracle
import os
import redis
import threading

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def fetch_data(fetchSql):
    db = cx_Oracle.connect('pmp', 'pmp', 'localhost:1521/xe')
    conn = db.cursor()
    conn.execute(fetchSql)
    rs = conn.fetchone()
    db.close()
    return rs


def send_to_redis():
    REDIS_ADDR = '123.56.235.47'
    REDIS_PORT = 8200
    REDIS_PASS = 'DogStandNFdoa1'
    r = redis.Redis(host=REDIS_ADDR, port=REDIS_PORT, password=REDIS_PASS, db=0)


    def send_loop1():
        rs_spgs = fetch_data("select * from data_spgs_buffer")
        rs_caes_buffer = fetch_data("select * from data_caes_buffer")
        rs_caes_dp = fetch_data("select * from data_caes_dp")
        rs_hggs_buffer = fetch_data("select * from data_hggs_buffer")
        rs_mcds_buffer = fetch_data("select * from data_mcds_buffer")
        rs_mcds_df = fetch_data("select * from data_mcds_df")
        rs_prcs_buffer = fetch_data("select * from data_prcs_buffer")
        rs_spgs_kzg = fetch_data("select * from data_spgs_kzg ")


        r.rpush("data_spgs_buffer", rs_spgs)  # 数据每隔3秒采集一次
        r.rpush("data_caes_buffer", rs_caes_buffer)  # 数据每隔3秒采集一次
        r.rpush("data_caes_dp", rs_caes_dp)  # 数据每隔3秒采集一次
        r.rpush("data_hggs_buffer", rs_hggs_buffer)  # 数据每隔3秒采集一次
        r.rpush("data_mcds_buffer", rs_mcds_buffer)  # 数据每隔3秒采集一次
        r.rpush("data_mcds_df", rs_mcds_df)  # 数据每隔3秒采集一次
        r.rpush("data_prcs_buffer", rs_prcs_buffer)  # 数据每隔3秒采集一次
        r.rpush("data_spgs_kzg", rs_spgs_kzg)  # 数据每隔3秒采集一次
        threading.Timer(3, send_loop1).start()

    def send_loop2():
        rs_ctyd_buffer = fetch_data("select * from data_ctyd_buffer")
        r.rpush("data_ctyd_buffer", rs_ctyd_buffer)  # 数据每隔30秒采集一次
        threading.Timer(30, send_loop2).start()

    send_loop1()
    send_loop2()

if __name__ == "__main__":
    send_to_redis()
