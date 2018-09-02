import threading
from time import ctime , sleep

class Threadreading1(object) :
    def __init__(self, func, args, name = ''):
        self.func = func
        self.args = args
        self.name = name
        print('func;{},args:{},name:{}'.format(self.func, self.args,self.name))
    def __call__(self):
        self.func(*self.args)

def loop(loop ,nspc):
    print('start loop{}, at:{}'.format(loop, ctime()))
    sleep(nspc)
    print('stop loop {} ,at:{}'.format(loop, ctime()))

loopNspc = [2,4]
def main() :

    loops = range(len(loopNspc))
    threadArray = []
    for i in loops :
        t = threading.Thread(target=Threadreading1(loop,(i,loopNspc[i]), loop.__name__))
        threadArray.append(t)
    for i in range(len(threadArray)) :
        threadArray[i].start()
    for i in range(len(threadArray)) :
        threadArray[i].join()
    print('all DONE at:', ctime())
if __name__ == '__main__':
    main()