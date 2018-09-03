
# if语句

### 判断两个值是否相等用(==)
### 常用的判断符号 ==, >= ,<=,!=, >, <


```python
a = 'a'
b = 'b'
print(a == b)
b = 'a'
print(a == b)
#考虑大小写
b = 'A'
print(a == b)
b = b.lower()
print(a == b)
```

    False
    True
    False
    True
    

### 判断两个值不相等用 !=


```python
a = 'a'
b = 'b'
print(a != b)
```

    True
    

#  使用and 和 or 关键字
### and关键字需要所有的条件都为true,结果才为true
### or关键字只需要其中的一个条件为true,结果就为true


```python
a = 21
b = 30
print('and:', a > 10 and b >20)
print('or:', a > 30 or b >20)
```

    and: True
    or: True
    

# 检查特定的值是否包含在列表中用 in 反之不包含用 not in


```python
# in的使用
t = [1,2,3,4,5,6,7,8,9]
print('in:', 1 in t)
# not in 的使用
print('not in :', 10 not in t)
```

    in: True
    not in : True
    

# if-else语句


```python
age = 18
if age > 15 :
    print('True')
else :
    print('False')
```

    True
    

# if-elif-else语句
    ### 可以使用多个elif模块


```python
age = 18 
if age > 18 :
    print('age > 18')
elif age == 18 :
    print('age = 18')
else :
    print('age < 18')
```

    age = 18
    
