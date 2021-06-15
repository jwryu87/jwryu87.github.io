---
layout: post
title: (hive) explode 함수
date: 2021-06-02
tags: hive
comments: true
---

```
select array(1, 2, 3);
select explode(array(1, 2, 3));
```

1개의 열을 받아서 N개의 열을 반환  
array, map, struct 형식의 테이터를 테이블 형태로 반환

![explode]({{ site.url }}/assets/hive_explode.png)
