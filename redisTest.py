import datetime
import json
import pickle

import redis  # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

from qinghai.connect_oracle import fetch_data

'''
 连接redis，加上decode_responses=True，写入的键
 值对中的value为str类型，不加这个参数写入的则为字节类型。
'''
# r=redis.Redis(host='localhost',port=6379,decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# r.set('name','junxi')
# print(r['name'])
# print(r.get('name'))
# print(type(r.get('name')))
'''
redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池
'''

# pool = redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)
# r= redis.Redis(connection_pool=pool)
# r.set('gender','male')
# r.set('jason',
#       'he is a handsome boy!')
# print(r['jason'])
# print(r.get('gender'))


'''
  set(name,value,ex=None,Px=None,nx=False,xx=False)
  在Redis中设置值，默认，不存在则创建，存在则修改
  参数：
      ex，过期时间（秒）
      px，过期时间（毫秒）
      nx，如果设置为True，则只有name不存在时，当前set操作才执行
      xx，如果设置为True，则只有name存在时，当前set操作才执行
'''
# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(connection_pool=pool)
# # r.set('food', 'mutton',ex=3)
# print(r['jason'])
# print(r.get('food'))
from qinghai import connect_mysql


def main():
    REDIS_ADDR = '123.56.235.47'
    REDIS_PORT = 8200
    REDIS_PASS = 'DogStandNFdoa1'
    r = redis.Redis(host=REDIS_ADDR, port=REDIS_PORT, password=REDIS_PASS, db=0)


    data_ctyd_buffer = r.blpop("data_ctyd_buffer", 0)

    mylist=list(eval(data_ctyd_buffer[1]))
    mylist[0]=mylist[0].strftime('%Y-%m-%d %H:%M:%S')

    print(tuple(mylist))

    connect_mysql.delete("data_ctyd_buffer")
    connect_mysql.insert("data_ctyd_history", str(tuple(mylist)))
    connect_mysql.insert("data_ctyd_buffer", str(tuple(mylist)))


if __name__ == '__main__':
    main()


