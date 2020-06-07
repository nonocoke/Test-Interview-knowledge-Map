#! /usr/bin/python3

import time
import redis


class RedisLock(object):
    """Reids 的分布式锁"""
    def __init__(self, key):
        # 连接数据库，创建连接对象
        self.rdcon = redis.Redis(host='', port=6379, password='', db=1)
        # 设置锁的值
        self._lock = 0
        # 分布式锁的键
        self.lock_key = "%s_dynamic_test" % key

    @staticmethod
    def get_lock(cls, timeout=10):
        """获取 redis 分布式锁

        设置分布式锁，判断锁是否超时
        :param cls: 锁的类对象
        :param timeout: 锁超时时间
        :return:
        """
        while cls._lock != 1:
            # 设置锁的过期时间
            _timestamp = time.time() + timeout + 1
            # 设置 redis 分布式锁键值
            cls._lock = cls.rdcon.setnx(cls.lock_key, _timestamp)
            # 判断锁的值是否为1， 或当前时间大于锁预期释放的时间，如果成立则退出循环，释放锁
            if cls._lock == 1 or (
                    time.time() > cls.rdcon.get(cls.lock_key) and
                    time.time() > cls.rdcon.getset(cls.lock_key, _timestamp)):
                print("get lock")
                break
            else:
                time.sleep(0.3)

    @staticmethod
    def release(cls):
        """释放锁
        
        :param cls: 锁的类对象
        :return:
        """
        # 判断当前时间释放大于锁最大释放时间
        if time.time() < cls.rdcon.get(cls.lock_key):
            print("release ok")
            cls.rdcon.delete(cls.lock_key)


def deco(cls):
    """分布式锁装饰器
    
    :param cls: 锁的类对象
    :return: 外层函数
    """
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called [%s]." % (func.__name__, cls))
            cls.get_lock(cls)
            try:
                return func(*args, **kwargs)
            finally:
                cls.release(cls)
            return __deco
        return _deco

@deco(RedisLock("demoLock"))
def myfunc():
    print("myfunc() called.")
    # 设置 20s 模拟超过锁释放时间就自动释放锁的操作
    time.sleep(20)

def test_redis():
    # 创建连接对象
    conn_obj = redis.Redis(host='localhost', port=6379, db=0)
    # 设置一个键值
    conn_obj.set('test', '1')
    # 读取一个键值
    conn_obj.get('test')  # ->> '1'
    # 不需要关闭连接

if __name__ == "__main__":
    myfunc()
