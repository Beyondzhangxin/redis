# coding=utf-8
import redis

REDIS_ADDR = '123.56.235.47'
REDIS_PORT = 8200
REDIS_PASS = 'DogStandNFdoa1'
# REDIS_ADDR='localhost'
# REDIS_ADDR='166.111.61.115'
# REDIS_PORT=6379
# REDIS_PASS=None
# REDIS_PASS='DogStandNFdoa1'
r = redis.Redis(host=REDIS_ADDR, port=REDIS_PORT, password=REDIS_PASS, db=0)
# length=r.llen("data_spgs_buffer")
data = r.keys("data*")
for item in data:
    print(item.decode('utf-8'))
    print(r.llen(item.decode('utf-8')))
r.delete("data_spgs_buffer111")
data_caes_dp = r.lpop("data_caes_dp")
print(data_caes_dp)

# def caes_dp():
#     # 先删除一条记录再添加达到更新目的
#     data_caes_dp = r.blpop("data_caes_dp", 0)
#     connect_mysql.delete("data_caes_dp")
#     print(data_caes_dp[1].decode('utf-8'))
#     connect_mysql.insert("data_caes_dp", data_caes_dp[1].decode('utf-8'))
# caes_dp()