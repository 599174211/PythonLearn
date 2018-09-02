from MyThread import MyThread
import threading
from  time import  ctime, sleep
def loop(nloop, sleepTime) :
    print('start_loop:{}, at:'.format(nloop, ctime()))
    sleep(sleepTime)
    print('stop_loop:{},at:{}'.format(nloop, ctime()))
    return nloop
def main():
    sleepTime = [2,4]
    loops = range(len(sleepTime))
    tArray = []
    for i in loops:
        t = MyThread(loop, args = (i, sleepTime[i]), name = loop.__name__)
        print(t)
        tArray.append(t)
    for i in range(len(tArray)) :
        tArray[i].start()
    for i in range(len(tArray)) :
        tArray[i].join()
        print('getResult.res:',tArray[i].getResult())
    print('all DONE at:{}'.format(ctime()))
if __name__ == '__main__':
    main()
