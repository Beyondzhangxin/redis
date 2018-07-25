import redis
import threading
import time


def loop(time2):
    for i in range(1000):
        r = redis.Redis(connection_pool=pool)
        r.set("name", time2)
        time.sleep(time2)


def loop2():
    for i in range(1000):
        print(r.get("name"))
        time.sleep(1)


if __name__ == '__main__':
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)

    t1 = threading.Thread(target=loop, name="l1", args=(1,))
    t2 = threading.Thread(target=loop, name="l2", args=(3,))
    t3 = threading.Thread(target=loop2, name="l3")
    t1.start()
    t2.start()

    t3.start()


    pool.disconnect()