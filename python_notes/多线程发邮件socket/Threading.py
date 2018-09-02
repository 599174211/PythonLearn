import threading
from time import sleep,ctime
loops = [4,2]
def loop(nloop, nsec) :
    print('start loop', nloop,',nsec:',nsec,'at:',ctime())
    sleep(nsec)
    print('stop loop',nloop,'at:',ctime())
def main():
    print('starting at:', ctime())
    thread = []

    nloops = range(len(loops))

    t = threading.Thread()
    thread.append(t)
    for i in nloops :
        #创建线程
        t = threading.Thread(target=loop, args=(i, loops[i]))
        thread.append(t)
    for i in range(len(thread)) :
        print('start{}'.format(thread[i].name))
        thread[i].start() #启动线程
    for i in range(len(thread))  :
        #等待所有的线程结束
        print('threads{}',format(i))
        thread[i].join()
    print('all DONE at:', ctime())

if __name__ == '__main__':

    main()