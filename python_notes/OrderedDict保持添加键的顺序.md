
# OrderedDict保持添加键的顺序
    --collections.OrderedDict 这个类型在添加键的时候会保持顺序,因此键的迭代总是一致的
        OrderedDict的popitem方法默认删除并返回的是字典里的最后一个元素,但是如果像
        OrderedDict.popitem(last = False)这样调用它,那么它删除并返回第一个被添加进去的元素


```python
import collections
iter_str = 'abcdefg'
#创建一个OrderedDict的实例index
index = collections.OrderedDict()
#把字符串列表添加到index集合里面
for i in range(7) :
    index[i] = list(iter_str)[i]
print(index)
#删除index的第一个key-value
index.popitem(last = False)
print(index)
```

    OrderedDict([(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g')])
    OrderedDict([(1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g')])
    
