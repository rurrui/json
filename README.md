# json
## [基本概念](#concept)
## [Json基于两种结构](#struct)
<p id='concept'>Json 是一种轻量级的数据交换格式</p>

<ol id="struct">
    <li>[数组](#array)</li>
    <li>[对象](#object)</li>
</ol>
<p id="array">以["a","b","c"]的形式组成，其中每个元素可以是数字，字符串，数组和对象</p>
<p id="object">以{}形式展现，{key:value,key:value}组成,value可以是数字，字符串，数组和对象</p>
```json
    {
        "Animal":{
            "Dog":[
                {
                    "name":"tom",
                    "age":15
                },
                {
                    "name":"joe",
                    "age":12
                }
            ]
        }
    }
```
