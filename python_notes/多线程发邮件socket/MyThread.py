import threading
from time import ctime

class MyThread(threading.Thread) :
    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def getResult(self):
        return self.res
    def __str__(self):
        return 'func:{},args:{},name:{}'.format(self.func, self.args, self.name)
    __repr__= __str__
    def run(self):
        print('name:{},at:{}'.format(self.name, ctime()))
        self.res = self.func(*self.args)
        print('res:{}'.format(self.res))
        print('name:{},at:{}'.format(self.name, ctime()))