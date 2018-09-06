
# 不可变映射类型,(字典)MappingProxyType
   
   python3.3开始,types模块中引入了一个封装类名叫MappingProxyType
   如果给这个类一个映射,它会返回一个只对映射视图.
   虽然是个只读的视图,但是它是动态的,这意味着如果对原映射做出了改动,
   我们可以通过这个视图观察到,但是无法通过这个视图对原映射做出修改
   


```python
#示例
from types import MappingProxyType
#创建一个集合
index_a = {'a' : 'b'}
#创建index_a的映射视图
a_proxy = MappingProxyType(index_a)
print(a_proxy)
a_proxy['a']
# #不能对a_proxy视图进行修改
# a_proxy['b'] = 'bb'
#但是可以对原映射进行修改
index_a['b'] = 'bb'
print(a_proxy)
```

    {'a': 'b'}
    {'a': 'b', 'b': 'bb'}
    
