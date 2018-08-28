import  os
from sys import  argv
readFile = open('E:\\python_work\\PythonLearn\\2018_08_28\\readTest.txt')
text = ''
for lin in readFile :
    text += lin
    print(lin , end='')
try:
    #要写入的文件
    writeFile = open('E:\\python_work\\PythonLearn\\2018_08_28\\writeTest.txt', 'w')
except :
    #创建文件
    os.mkdir('E:\\python_work\\PythonLearn\\2018_08_28\\writeTest.txt', 'w')
writeFile.write(text)
readFile.close()
writeFile.close()
t = argv
print('\nt' + str(t))
argvStr = open(str(t[0]))
print('argvStr' + str(argvStr))