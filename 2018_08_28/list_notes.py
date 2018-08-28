
# coding: utf-8

# In[31]:


#汉诺塔
def hannuota(n, i,a, b, c) :
    i += 1
    print('i:%s, n:%s' %(str(i), n))
    #只有一个盘子的时候
    if n == 1 :
        print(a + '->' + c)
        return None;
    #有两个盘子的时候 '''
    '''
    if n ==2 :
        #第一步从a移动到b
        #第二步从a移动到c
        #第三部从b移动c
        print(a + '2->' + b)
        print(a + '2->' + c)
        print(b + '2->' + c)    
        return None;
    '''
    #盘子大于2个的时候
    #第一步把n-1个盘子从a借助于c移动到b
    hannuota(n-1,i, a, c, b)
    #第二步把a上的一个盘子移动到c
    print('i1:%s, n1:%s' %(str(i), n))
    print(a + '1->' + c)
    #第三步把b上的n-1个盘子借助a移动到c     
    hannuota(n-1, i, b, a, c)a
n = 3
i = 0
hannuota(n, i, 'A', 'B', 'C')


# In[19]:


n = 2;
hannuota(n, 'A', 'B', 'C')


# In[35]:


#列表
a = [1,2,3,4]
print (a)


# In[37]:


#列表相加
a = [1,2,3,4]
b = ['a', 'b','c','d']
print (a +b )


# In[38]:


#列表的乘法
a = [1,2,3,4,5]
print(a * 5)


# In[39]:


#判断一个元素是否在列表里面
a = [1,2,3,4,5]
b = 2
print(b in a)


# In[40]:


#判断一个元素不在列表里面
a = [1,2,3,4,5]
b = 6
print(b not in a)


# # 列表的遍历
# for
# while

# In[73]:


b = ['i','l','o','v','e']
for i in b :
    print('i' + i)


# In[75]:


#使用range
b = range(0,5)
for i in b :
    print(i)


# # 用while循环访问list 一般不推荐

# In[77]:


a = [1,2,3,4,5]
a_len = len(a)
index = 0
while index < a_len :
    print(a[index])
    index += 1


# In[83]:


#双层列表
a = [['a',1,'one'] , ['b',2,'two'], ['c',3,'three']]
#i,j 要与嵌套的列表里面的个数对应
for i,j,k in a :
    print('i:%s,j:%s,k%s' %(i,j,k))


# In[100]:


a = [i for i in range(0,4)]
print(a)
b = [i for i in range(100,1000) if i%400 == 0]
print(b)
c = [m + n for m in a for n in b if (m+n) < 800]
print(c)


# # 关于列表的函数
# #len() 求列表的长度
# #max()求最大值
# #min()求最小值
# 

# In[102]:


a = [i for i in range(0,100)]
print(len(a))
print(min(a))
print(max(a))


# In[109]:


#在列表后面追加元素
a = ['a', 'b', 'c','d']
print(a)
a.append('e')
print(a)


# In[111]:


#用insert指定位置插入元素
a = ['a','b','c','d','e']
print(a)
a.insert(3,4)
print(a)


# In[125]:


#s删除
# del 删除列表
#pop把最后一个元素从列表里面拿出来

print(a)
pop_a = a.pop();
print(pop_a)
del a
print(a)


# In[133]:


#remove:在列表中删除指定的元素

a = ['a,','b','c,','d','e','f']
print(a)
print(id(a))
a.remove('e')
print(id(a))
print(a)


# In[136]:


#clear 删除列表里的值,但是占用的地址还在
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))


# In[144]:


#reverse 翻转地址内容,在原来的地址里面翻转
a = [1,2,3,4,5,6,7]
print(a)
print(id(a))
a.reverse()
print(a)
b = [8,9,10]
print(id(b))
a.extend(b)
print(a)
print(id(a))


# In[146]:


#count;返回列表的长度
print(a)
a_len = len(a)
print(a_len)


# In[163]:


#copy 拷贝 浅拷贝 
# b=a赋值直接把地址指向b,a和b共用同一个地址,修改其中一个另一个也变化
# b =a 
a =[1,2,3,4,5,6,7]
print(a)
b = a
b.append(8)
print(a)
print(b)
print('*' *20)
#copy a 只是赋值,没有传地址
a = [1,2,3,4,5]
print(a)
print(id(a))
b = a.copy()
print(b)
print(id(b))
#copy 只能拷贝一层,里面另外一层的地址还是在a
print('*' *20)
a = [1,2,3,4,[1,2,3,4]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[4]))
print(id(b[4]))
if id(b[4])== id(a[4]) :
    print('true')


# # tuple 元组
# .是序列表有序
# .元组数据可以访问不能修改
# .元组数据可以是任意类型
# .总之list所有特性,除了不能修改之外,元组都有
# .也就意味着,list具有的一些操作,比如索引,分片,序列相加,相乘,成语这个操作等,一模一样

# In[171]:


a = 1,;
print(type(a))
a = (1,)
print(type(a))
#使用其他结构创建数组
a = 1,2,3,4,5
b = tuple(a)
print(type(b))
print('*' * 8)
a = ['a','b','c','d','e']
b = tuple(a)
print(type(b))


# In[172]:


print(a)


# In[173]:


a.append('f')
print(a)


# In[174]:


len(a)
print(len(a))


# In[8]:


#list 切片功能
a = ['a', 'b','c','d','e','f','g']
#切下标0到4的数组不包括5
b = a[0:5]
print(b)
#2表示步长间隔2个数值进行切片
c = a[0:6:2]
print(c)
#歩长可以超过列表的长度
c = a[0:6:100]
print(c)

