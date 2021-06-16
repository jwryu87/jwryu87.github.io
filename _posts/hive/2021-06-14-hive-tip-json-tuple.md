---
layout: post
title: (hive) json_tuple 함수
date: 2021-06-14 17:00:00 +09:00
tags: hive
comments: true
---

json 형식의 컬럼을 열로 구분한다.

```
select json_tuple(body, 'col1', 'col2', 'col3') as (col1, col2, col3) from table;
```


![explode]({{ site.url }}/assets/hive_json_tuple.png)
