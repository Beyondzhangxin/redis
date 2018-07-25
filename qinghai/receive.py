import redis
import threading
import datetime
from qinghai import connect_mysql


def main():
    REDIS_ADDR = '123.56.235.47'
    REDIS_PORT = 8200
    REDIS_PASS = 'DogStandNFdoa1'
    r = redis.Redis(host=REDIS_ADDR, port=REDIS_PORT, password=REDIS_PASS, db=0)

    def lockDecorator(func):
        def wrapper(*args, **kwargs):
            lock = threading.RLock()
            lock.acquire()
            func(*args, **kwargs)
            lock.release()

        return wrapper

    def ctyd_buffer():
        data_ctyd_buffer = r.blpop("data_ctyd_buffer", 0)

        mylist = list(eval(data_ctyd_buffer[1]))
        mylist[0] = mylist[0].strftime('%Y-%m-%d %H:%M:%S')

        connect_mysql.delete("data_ctyd_buffer")
        connect_mysql.insert("data_ctyd_history", str(tuple(mylist)))
        connect_mysql.insert("data_ctyd_buffer", str(tuple(mylist)))

    def spgs_buffer():
        data_spgs_buffer = r.blpop("data_spgs_buffer", 0)
        connect_mysql.delete("data_spgs_buffer")
        connect_mysql.insert("data_spgs_history", data_spgs_buffer[1].decode('utf-8'))
        connect_mysql.insert("data_spgs_buffer", data_spgs_buffer[1].decode('utf-8'))
    def caes_buffer():
        data_caes_buffer = r.blpop("data_caes_buffer", 0)
        connect_mysql.delete("data_caes_buffer")
        connect_mysql.insert("data_caes_buffer", data_caes_buffer[1].decode('utf-8'))
        connect_mysql.insert("data_caes_history", str(eval(data_caes_buffer[1])[:-2]))

    def caes_dp():
        # 先删除一条记录再添加达到更新目的
        data_caes_dp = r.blpop("data_caes_dp", 0)
        connect_mysql.delete("data_caes_dp")
        connect_mysql.insert("data_caes_dp", data_caes_dp[1].decode('utf-8'))

    def hggs_buffer():
        data_hggs_buffer = r.blpop("data_hggs_buffer", 0)
        connect_mysql.delete("data_hggs_buffer")
        connect_mysql.insert("data_hggs_buffer", data_hggs_buffer[1].decode('utf-8'))
        connect_mysql.insert("data_hggs_history", data_hggs_buffer[1].decode('utf-8'))

    def mcds_buffer():
        data_mcds_buffer = r.blpop("data_mcds_buffer", 0)
        connect_mysql.delete("data_mcds_buffer")
        connect_mysql.insert("data_mcds_history", data_mcds_buffer[1].decode('utf-8'))
        connect_mysql.insert("data_mcds_buffer", data_mcds_buffer[1].decode('utf-8'))

    def mcds_df():
        # 先删除一条记录在添加达到更新目的
        data_mcds_df = r.blpop("data_mcds_df", 0)
        connect_mysql.delete("data_mcds_df")
        connect_mysql.insert("data_mcds_df", data_mcds_df[1].decode('utf-8'))

    def prcs_buffer():
        data_prcs_buffer = r.blpop("data_prcs_buffer", 0)
        connect_mysql.delete("data_prcs_buffer")
        connect_mysql.insert("data_prcs_history", data_prcs_buffer[1].decode('utf-8'))
        connect_mysql.insert("data_prcs_buffer", data_prcs_buffer[1].decode('utf-8'))

    def spgs_kzg():
        # 先删除一条记录在添加达到更新目的
        data_spgs_kzg = r.blpop("data_spgs_kzg", 0)
        connect_mysql.delete("data_spgs_kzg")
        connect_mysql.insert("data_spgs_kzg", data_spgs_kzg[1].decode('utf-8'))

    def receive_loop():
        rlock=threading.RLock()
        rlock.acquire()
        # 多线程，从redis取出数据，没有则继续等待
        t1=datetime.datetime.now()
        # threading.Thread(spgs_buffer()).start()
        spgs_buffer()
        spgs_kzg()
        caes_dp()
        caes_buffer()
        hggs_buffer()
        mcds_df()
        mcds_buffer()
        prcs_buffer()
        rlock.release()
        # threading.Thread(spgs_kzg()).start()
        # threading.Thread(caes_buffer()).start()
        # threading.Thread(caes_dp()).start()
        # threading.Thread(hggs_buffer()).start()
        # threading.Thread(mcds_buffer()).start()
        # threading.Thread(mcds_df()).start()
        # threading.Thread(prcs_buffer()).start()
        timer = threading.Timer(3, receive_loop)
        t2=datetime.datetime.now()
        print(t2-t1)
        print("dsfasdfas")
        timer.start()

    def ctyd_loop():
        threading.Thread(ctyd_buffer()).start()
        # ctyd_buffer()
        print("I am doing now !")
        timer = threading.Timer(30, receive_loop)
        timer.start()

    threading.Thread(receive_loop()).start()
    threading.Thread(ctyd_loop()).start()


if __name__ == '__main__':
    main()
