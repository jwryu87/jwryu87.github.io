---
layout: post
title: (hive) 맵리듀스를 사용하지 않고 로컬에서 동작하도록 설정
date: 2021-06-16 12:00:00 +09:00
tags: hive
comments: true
---

```
set hive.exec.mode.local.auto=true;
```

쿼리 수행 시 맵리듀스를 사용하지 않고 로컬에서 동작하도록 하기 위해서 위와 같이 설정하고 쿼리를 수행하면 된다.  

참고로 hive에서 무조건 맵리듀스를 실행하는 건 아니다.  
일부 쿼리에선 로컬에서 동작하기도 한다.  
아래와 같은 경우 맵리듀스를 사용하지 않는다.  
1. select * from table; 과 같은 단순한 쿼리 
2. where 절이 오직 파티션 키만 걸러낼 때

