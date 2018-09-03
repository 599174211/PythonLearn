
# list列表
    -列表是由一系列按特定顺序的元素组成,在Python中用[]来表示列表,并用逗号来分隔其中的元素
    -索引从0开始而不是1,正数左边开始
    -如果索引是负数则从右边开始,右边第一个元素的索引为-1
    


```python
t = ['a','b','c','d','e','f']
print('t列表索引为1的元素:{}'.format(t[1]))
print('t列表索引为-1的元素:{}'.format(t[-1]))
```

    t列表索引为1的元素:b
    t列表索引为-1的元素:f
    

# 修改/添加和删除元素


```python
#修改列表中的元素
t = ['a','b','c','d','e','f']
t[0] = 'q'
print(t)
```

    ['q', 'b', 'c', 'd', 'e', 'f']
    


```python
#添加元素
#append()在列表末尾添加元素
t = ['a','b','c','d','e','f'] 
t.append('g')
print(t)
```

    ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    


```python
#在列表中插入元素
#insert()可在列表的任何位置添加新元素,第一个参数是索引的位置,第二个参数添加的元素值
t = ['a','b','c','d','e','f']
t.insert(1,'a1')
print(t)
```

    ['a', 'a1', 'b', 'c', 'd', 'e', 'f']
    


```python
#在列表中删除元素
#del语句删除元素
#del 可以删除列表任何位置的元素,条件是知道其索引
t = ['a','b','c','d','e','f']
del t[1]
print(t)
```

    ['a', 'c', 'd', 'e', 'f']
    


```python
#使用pop()方法删除列表中的元素
#pop()默认删除最后一个元素,可以通过指定参数的所有,删除列表对应的参数
a = ['a','b','c','d','f']
#默认删除最后一个
print(a.pop())
print(a)
#删除指定位置的元素
print(a.pop(1))
print(a)
```

    f
    ['a', 'b', 'c', 'd']
    b
    ['a', 'c', 'd']
    


```python
#使用remove()方法根据值删除元素,无须知道其索引
t = ['a','b','c','d','e']
#根据值删除元素
print(t.remove('a'))
print(t)
```

    None
    ['b', 'c', 'd', 'e']
    

# 组织列表,对列表进行排序
       -使用sort()对列表进行永久性的排序


```python
#sort()对列表进行永久性排序
t = ['a','c','r','b','q','y','e']
#对列表排序
t.sort()
print('排序后的列表{}'.format(t))
#对列表进行反排序在sort()传入参数reverse = True
t.sort(reverse = True)
print('反排序后的列表:{}'.format(t))
```

    排序后的列表['a', 'b', 'c', 'e', 'q', 'r', 'y']
    反排序后的列表:['y', 'r', 'q', 'e', 'c', 'b', 'a']
    

# 倒着打印列表 
    -reverse()永久性的修改列表元素的排列顺序,可以随时恢复到原来的顺序,需要重新调用reverse()方法


```python
#倒着打印列表 
#reverse()永久性的修改列表元素的排列顺序,可以随时恢复到原来的顺序,需要重新调用reverse()方法
t = ['a','c','r','b','q','y','e']
print('按顺序打印:{}'.format(t))
t.reverse()
print('倒着打印:{}'.format(t))
print('列表现在的顺序:{}'.format(t))
```

    按顺序打印:['a', 'c', 'r', 'b', 'q', 'y', 'e']
    倒着打印:['e', 'y', 'q', 'b', 'r', 'c', 'a']
    列表现在的顺序:['e', 'y', 'q', 'b', 'r', 'c', 'a']
    

# 列表的长度
    -使用len()函数


```python
#len()使用
t = ['a','b','c','d','e','f','g','h']
print('len:{}'.format(len(t)))
```

    len:8
    

# 遍历整个列表
    -for循环遍历
    -使用range()函数


```python
#for循环使用
t = ['a','b','c','d','e','f','g','h']
for i in t :
    print('i:{}'.format(i), end="")
```

    i:ai:bi:ci:di:ei:fi:gi:h


```python
#使用range()函数
for i in range(0,5) :
    print('i:{}'.format(i),end = "")
```

    i:0i:1i:2i:3i:4


```python
#使用range()创建list列表
t = list(range(0,5))
print(t)
```

    [0, 1, 2, 3, 4]
    


```python
#使用range()函数可以指定歩长的参数
#生成0-9的数包含9,但是歩长为2
t = list(range(0,10,2))
print(t)
```

    [0, 2, 4, 6, 8]
    

# 对列表进行简单的统计
    --min()最小值
    __max()最大值
    __sum()求和


```python
t = [1,2,3,4,5,6,7,9]
print('min:{}'.format(min(t)))
print('max:{}'.format(max(t)))
print('sum:{}'.format(sum(t)))
```

    min:1
    max:9
    sum:37
    

# 切片
    -例如t[0:3]表示索引0-2的元素,包含2
    -可以有歩长例如,t[0:3:2}表示索引0-2的元素,歩长为2


```python
t1 = [1,2,3,4,5,6,7,8,9]
t2 = ['a','b','c','d','e','f','g','h']
t3 = t1[0:3]
print('t3:{}'.format(t3))
t4 = t2[0:7:2]
print('t4:{}'.format(t4))
#拼接数组
t5 = t3 + t4
print('t5{}'.format(t5))
```

    t3:[1, 2, 3]
    t4:['a', 'c', 'e', 'g']
    t5[1, 2, 3, 'a', 'c', 'e', 'g']
    

# 复制列表



```python
#copy() 深拷贝重新开辟一个空间储存值
t1 = [1,2,3,4,5,6,7]
print('t1Id:{}'.format(id(t1)))
t2 = t1.copy()
print('t2:{}'.format(t2))
print('t2Id:{}'.format(id(t2)))
t2[1] = 8
print('t1:{},t2{}'.format(t1,t2))
import copy

t3 = copy.copy(t1)
print('t3Id:{}'.format(id(t3)))
t3[1] = 9
print('t1Id:{},t3Id;{}'.format(t1,t3))
t4 = t1
print('t4Id:{}'.format(id(t4)))
t4[1] = 10
print('t1Id:{},t4Id;{}'.format(t1,t4))
```

    t1Id:2300959914888
    t2:[1, 2, 3, 4, 5, 6, 7]
    t2Id:2300960328456
    t1:[1, 2, 3, 4, 5, 6, 7],t2[1, 8, 3, 4, 5, 6, 7]
    t3Id:2300960962504
    t1Id:[1, 2, 3, 4, 5, 6, 7],t3Id;[1, 9, 3, 4, 5, 6, 7]
    t4Id:2300959914888
    t1Id:[1, 10, 3, 4, 5, 6, 7],t4Id;[1, 10, 3, 4, 5, 6, 7]
    


```python
#copy 当大列表嵌套小列表时
t1 = ['a','b',[1,2,3],'c','d','f']
print('t1:{},t1Id{}'.format(t1,id(t1)))
t2 = t1.copy()
print('t2:{},t2Id{}'.format(t2,id(t2)))
t2[2][1] = 0
print('t1:{},t2:{}'.format(t1,t2))
t2[3] = 'x'
print('t1:{},t2:{}'.format(t1,t2))
#使用copy()函数创建的列表,改变大列表的值不影响,原来的列别,改变大列表里面小列表的值,影响原来的列表
#深拷贝 copy.deepcopy() 开辟一个新的空间进行储存,改变大列表和小列表的元素都不影响原来的列表
t3 = copy.deepcopy(t1)
print('t3:{},t3Id:{}'.format(t3,id(t3)))
t3[2][1] = 9
print('t1:{},t1Id:{},t3:{},t3Id:{}'.format(t1,id(t1),t3,id(t3)))
```

    t1:['a', 'b', [1, 2, 3], 'c', 'd', 'f'],t1Id2300962074824
    t2:['a', 'b', [1, 2, 3], 'c', 'd', 'f'],t2Id2300961982088
    t1:['a', 'b', [1, 0, 3], 'c', 'd', 'f'],t2:['a', 'b', [1, 0, 3], 'c', 'd', 'f']
    t1:['a', 'b', [1, 0, 3], 'c', 'd', 'f'],t2:['a', 'b', [1, 0, 3], 'x', 'd', 'f']
    t3:['a', 'b', [1, 0, 3], 'c', 'd', 'f'],t3Id:2300960261640
    t1:['a', 'b', [1, 0, 3], 'c', 'd', 'f'],t1Id:2300962074824,t3:['a', 'b', [1, 9, 3], 'c', 'd', 'f'],t3Id:2300960261640
    
