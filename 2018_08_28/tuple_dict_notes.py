
# coding: utf-8

# # 元组的函数
# 

# In[1]:


#len: 获取元组的长度
t = (1,2,3,4,5,6)
len(t)


# In[2]:


#max, min最大最小资
print(max(t))
print(min(t))


# In[5]:


#tuple:转换或创建元组
l = [1,2,3,4,5]
t = tuple(l)
print(t)
d = tuple()
print(d)


# # 元组的函数
# .基本跟list通用

# In[9]:


#count: 计算指定数据出现的次数
t = (1,2,2,3,1,4,4,2,3,4,5,5,6)
print(t.count(2))
#index: 求指定数据在元组的索引位置,如果有多个展示第一个
print(t.index(2))


# # 元组变量交换法
# 

# In[16]:


a = 1
b = 3
print(a)
print(b)
#java 程序员写法
c = a
a = b
b = c
print("a:%s, b:%s" %(a,b))
print('*' * 20)
#python 写法
a = 1
b = 3
a, b = b, a;
print('a:%s, b:%s' %(a,b))


# # 集合-set
# .一堆确定的无序的唯一数据,集合中每一个数据成为一个元素

# In[24]:


s = set()
print(type(s))
print(s)
#此时,大括号内一定要有值,否则定义出的是一个dict(字典)
t = {}
print(type(t))
s = {1,2,3,4,5,6}
print(type(s))
print(s)


# # 集合的特征
# .集合内数据无序,即无法使用索引和分片
# .集合内数据有唯一性,可以用来排除重复数据
# .集合内的数据,str,int,float,tuple,冰冻集合等,即内部只能放置可哈希数据

# In[29]:


#成员检测 无序
#in not in
s = {2,3,'a','dd',(1,2,3,),'i love pytho'}
print(s)
if 2 in s :
    print('我在我在')
if 4 not in s :
    print('我不在')


# In[36]:


#集合的遍历
s = {(1,2,3), ('a','b','c'),('i','love','python')}
print (s)
for x, y, z in s :
    print('x:%s,y:%s,z:%s ' %(x, y, z))
for x in s :
    print('x;%s' %str(x))


# # 集合的内涵
# 

# In[41]:


#集合的内涵
#集合在初始化时自动过滤重复的元素
s = {1,1,1,2,3,4,5,6,666,33,25,233,25,244,333}
print(s)
ss = {i for i in s if i %2 ==0}
print(ss)


# In[44]:


#多循环集合的内涵
s1 = {1,2,3,4}
s2 = {'i', 'love','pytho'}
s3 = {i * j for i in s2 for j in s1 }
print (s3)
s4 = {i * j for i in s2 for j in s1 if j == 2}
print(s4)


# In[46]:


#len ,max min 跟其他的基本函数一样
s = {1,2,3,4,5,55,66,3,2,2,4,5,6,9,0,10}
print(s)
print(min(s))
print(max(s))
print(len(s))


# In[47]:


#set生成一个集合
s = [1,2,3,4,5,6,7,8,0]
s = set(s)
print(s)


# In[50]:


# add:向集合添加元素
s.add(9)
print(s)
s.add('a')
print(s)


# In[54]:


#clear 删除元素内元素,占用的地址还是存在
s = {1,2,3,4}
print(s)
print(id(s))
s.clear()
print(s)
print(id(s)
#只清空集合的数据


# In[56]:


#
# s = {1,2,3,5}
# s.__len__


# In[74]:


#copy 拷贝值,拷贝的集合重新占用一个新的地址
#remove 移除集合中指定的数据 ,直接改变原有值,如果值不存在报异常
#discard:移除集合中指定的值,跟remove一样,但是如果删除的值不存在,不会报异常
s = {1,2,3,4,5,6,7,8,9}
print(s)
print(id(s))
t = s.copy()
print(t)
print(id(t))
s.remove(2)
print(s)
# s.remove(10)
# print(s)
s.discard(3)
print(s)
s.discard(3)
print(s)


# In[77]:


#集合减法,没有加法
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
s3 = s1 - s2
print(s3)
# s4 = s1 + s2
# print(s4)


# # frozenset 冰冻集合
# .不能修改的集合,是一种特殊的集合

# In[79]:


s = frozenset()
print(type(s))


# # dict 字典
# 字典是一种组合数据,没有顺序的组合数据,数据就是以键值对形式出现
# .字典是序列类型,但是是无序序列,所以没有分片和索引
# .key:必须是可哈希的值,比如int,stirng,float,bool,tuple,但是不能是set,list,dict
# value:可以是任何值

# In[82]:


#创建字典
d = {}
print(type(d))
#创建有值的字典
d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
print(d)


# In[88]:


d = {'a':1 , 'b' : 2, 'c' : 3}
print(d)
print(d['a'])
d['a'] = '3'
print(d['a'])
#del 通过key删除值
del d['a']
# print(d['a'])


# In[92]:


#成员检测, in, not in
d = {'a': 1, 'b':2, 'c': 3}
print(d)
if 'a' in d :
    print('key')


# In[95]:


#遍历字典
d = {'a': 1, 'b':2, 'c': 3}
for i in d.keys() :
    print(i, d[i])
#特殊写法
for i,j in d.items() :
    print(i, j)


# In[99]:


#字典生成式
d = {'a': 1, 'b':2, 'c': 3}
s = {i:j for i,j in d.items()}
print(s)
s = {i : j for i,j in d.items() if j%2 == 0}
print(s)

