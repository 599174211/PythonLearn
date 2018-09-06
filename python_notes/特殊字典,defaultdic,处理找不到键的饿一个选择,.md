
# 特殊字典,处理找不到键的时候一个选择,defaultdict
    --如果这个键在字典里不存在,defaultdict会把这个键添加到集合里面去,
    并把他的value设置为空列表[],如果设置设置了value,就使用设置的值
    


```python
import collections

#创建一个collections.defaultdict的实例
index = collections.defaultdict(list)
# index['not_key'] = ['a','a']
print(index)
#在index字典里面找一个not_key的key并给他的value赋值为设置为[]空列表,并把value追加到空列表中
key = 'not_key'
not_key_value = ('a', 'b')
index[key].append(value)
#字典推导表达式生成index_a
index_a = {key : value for key, value in index.items()}
print(index_a)
for key, value in index_a.items() :
    print('key:{},value:{}'.format(key, value))
```

    defaultdict(<class 'list'>, {})
    {'not_key': [[('a', 'b')]]}
    key:not_key,value:[[('a', 'b')]]
    
