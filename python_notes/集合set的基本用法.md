
# 集合set的基本用法



```python
set_a = {1,2,3,4,5}
set_b = {3,4,5,6,7,8}
#集合a与b的差集
print (set_a - set_b)
#集合a与b的并集
print(set_a | set_b)
#集合a与b的交集
print(set_a & set_b)
#集合a与集合b的对称集
print(set_a ^ set_b)
```

    {1, 2}
    {1, 2, 3, 4, 5, 6, 7, 8}
    {3, 4, 5}
    {1, 2, 6, 7, 8}
    


```python
# 集合的比较运算符
z = {1,2,3,4,5,6,7,8}
s = 5
#元素s是否属于z
print(s in z)
s = {5}
#s是否为z的子集
print(s <= z)
#s是否为z的真子集
print(s < z)
#s是否为z的父集
print(s >= z)
#s是否为z的真父集
print(s > z)
```

    True
    True
    True
    False
    False
    


```python
# 集合的其他方法
s = {1,2,3,4,5,6,7}
a = 8
#集合添加元素a
s.add(a)
print(s)
s.copy() #s的浅拷贝
s.discard(a) #如果集合s里面有a这个元素就把它移除
print(s)
#对集合s进行迭代
for i in s.__iter__() :
    print(i, end = "")
#集合s的元素个数
print('\n',s.__len__())
#删除集合中某个元素
s.remove(4)
print(s)
#删除集合中的一个并返回他的值
print(s.pop())
```

    {1, 2, 3, 4, 5, 6, 7, 8}
    {1, 2, 3, 4, 5, 6, 7}
    1234567
     7
    {1, 2, 3, 5, 6, 7}
    1
    
