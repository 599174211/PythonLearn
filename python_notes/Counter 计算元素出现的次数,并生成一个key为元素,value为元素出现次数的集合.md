
# Counter 计算元素出现的次数,并生成一个key为元素,value为元素出现次数的集合
        ---需要导入collections模块


```python
import collections
str_a = 'avafesadefgdaccggeazqqggjqieowlleqqq'
#生成collections.Counter的实例
index = collections.Counter(str_a)
print(index)
#返回元素出现次数最多的3个
index.most_common(3)
```

    Counter({'q': 6, 'a': 5, 'e': 5, 'g': 5, 'f': 2, 'd': 2, 'c': 2, 'l': 2, 'v': 1, 's': 1, 'z': 1, 'j': 1, 'i': 1, 'o': 1, 'w': 1})
    




    [('q', 6), ('a', 5), ('e', 5)]


