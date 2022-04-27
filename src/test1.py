import threading
import  time,datetime
# single instance
'''
1.类的初始化总是先执行__new__（此时的传参cls表示当前这个类），return一个实例化的对象，作为self参数传给__init__；
2.单例模式可以用于共享资源访问

'''
class Singleton:
    def __new__(cls, *args, **kwargs):
        #print('I have been executed')
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

class Bus(Singleton):
    #lock = threading.RLock()
    def sendData(self, data):
        #self.lock.acquire()
        time.sleep(3)
        print(datetime.datetime.now().strftime('%H:%M:%S'))
        print('Sending Data...', data)
        print(id(self))
        #self.lock.release()

class VisitEntity(threading.Thread):
    def getName(self) -> str:
        return self.name
    def setName(self, name: str) -> None:
        self.name = name
    def run(self) -> None:
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)

def singleton(cls, *args, **kwargs):
    instances = {}
    def wrapper():
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return wrapper

@singleton
class NewClass:
    pass

if __name__ == '__main__':
    # for i in range(3):
    #     print(' Entity%d begin to run..'%i)
    #     my_entity = VisitEntity()
    #     my_entity.setName("Entity"+str(i))
    #     my_entity.start()
    a = NewClass()
    b = NewClass()
    print(id(a), id(b))