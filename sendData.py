

from __future__ import division
import redis
from threading import Thread
import json
import time
import random
def main():
    channel='test'
    REDIS_ADDR='123.56.235.47'
    REDIS_PORT=8200
    REDIS_PASS='DogStandNFdoa1'
    # REDIS_ADDR='166.111.61.165'
    # REDIS_ADDR='127.0.0.1'
    # REDIS_ADDR='166.111.61.115'
    # REDIS_PORT=6379
    # REDIS_PASS='DogStandNFdoa1'
    r = redis.Redis(host=REDIS_ADDR, port=REDIS_PORT, password=REDIS_PASS, db=0)
    # f = open('test.json')  
    # rt_json = json.load(f)
    # outputchannels=["OutputChannel-1","OutputChannel-10","OutputChannel-100","OutputChannel-101","OutputChannel-102","OutputChannel-103","OutputChannel-104","OutputChannel-105","OutputChannel-106","OutputChannel-107","OutputChannel-108","OutputChannel-109","OutputChannel-11","OutputChannel-12","OutputChannel-13","OutputChannel-14","OutputChannel-15","OutputChannel-16","OutputChannel-17","OutputChannel-18","OutputChannel-19","OutputChannel-2","OutputChannel-20","OutputChannel-21","OutputChannel-22","OutputChannel-23","OutputChannel-24","OutputChannel-25","OutputChannel-26","OutputChannel-27","OutputChannel-28","OutputChannel-29","OutputChannel-3","OutputChannel-30","OutputChannel-31","OutputChannel-32","OutputChannel-33","OutputChannel-34","OutputChannel-35","OutputChannel-36","OutputChannel-37","OutputChannel-38","OutputChannel-39","OutputChannel-4","OutputChannel-40","OutputChannel-41","OutputChannel-42","OutputChannel-43","OutputChannel-44","OutputChannel-45","OutputChannel-46","OutputChannel-47","OutputChannel-48","OutputChannel-49","OutputChannel-5","OutputChannel-50","OutputChannel-51","OutputChannel-52","OutputChannel-53","OutputChannel-54","OutputChannel-55","OutputChannel-56","OutputChannel-57","OutputChannel-58","OutputChannel-59","OutputChannel-6","OutputChannel-60","OutputChannel-61","OutputChannel-62","OutputChannel-63","OutputChannel-64","OutputChannel-65","OutputChannel-66","OutputChannel-67","OutputChannel-68","OutputChannel-69","OutputChannel-7","OutputChannel-70","OutputChannel-71","OutputChannel-72","OutputChannel-73","OutputChannel-74","OutputChannel-75","OutputChannel-76","OutputChannel-77","OutputChannel-78","OutputChannel-79","OutputChannel-8","OutputChannel-80","OutputChannel-81","OutputChannel-82","OutputChannel-83","OutputChannel-84","OutputChannel-85","OutputChannel-86","OutputChannel-87","OutputChannel-88","OutputChannel-89","OutputChannel-9","OutputChannel-90","OutputChannel-91","OutputChannel-92","OutputChannel-93","OutputChannel-94","OutputChannel-95","OutputChannel-96","OutputChannel-97","OutputChannel-98","OutputChannel-99"]
    # print len(rt_json)
    # for val in rt_json:
    # sendMessage={
    #     'cmd':'msg',
    #     'data':'run start v 1.15',
    #     'task_id':1569835412
    # }
    # r.publish(str(channel),json.dumps(sendMessage) )
    # sendMessage={
    #     'cmd':'draw',
    #     'data':'',
    #     'task_id':1569835412
    # }
    # for times in range(0,10):
    #     for x in range(0,20):
    #         sendList={}
    #         for ch in outputchannels:
    #             sendList[ch]=[]
    #             for y in range(0,50):
    #                 t=times+x/20+y/1000
    #                 sendList[ch].append([t,random.random()])
    #         sendMessage['data']=sendList
    #         sendMessage['time']=times+x/20
    #         r.publish(str(channel),json.dumps(sendMessage) )
    #         print times+x/20
    #         time.sleep(0.001)
    # for ch in outputchannels:
    #     sendList[ch]=[]
    # for times in range(1,100000):
        
    #     if (times % 100)==0:
    #         sendList={}
    # sendMessage={
    #     'cmd':'msg',
    #     'data':'run ends',
    #     'task_id':1569835412
    # }
    # r.publish(str(channel),json.dumps(sendMessage) )
    # r.set("jason","test111")
    # r.set("baylee","she is a girl!")
    dic = {"a1": "aa", "b1": "bb"}
    r.hmset("dic_name", dic)




if __name__ == '__main__':
    main()
    print("success")
