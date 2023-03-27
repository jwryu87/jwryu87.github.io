---
layout: post
title: (hive) 파티션 관련 tip
date: 2021-06-17 12:00:00 +09:00
tags: hive
comments: true
---

```
set hive.exec.dynamic.partition=true;
```
hive 가 동적 파티션을 사용할 수 있도록 하기 위한 설정  

```
set hive.exec.dynamic.partition.mode=nonstrict
```
동적 파티션만을 이용하기 위한 설정  
기본값은 strict 이다.  
동적 파티션을 사용하면 속도가 느려지므로 기본값보다 더 많은 동적 파티션을 생성하고 싶으면 추가로 설정이 필요하다.  

```
set hive.mapred.mode=nonstrict;
```
테이블 조회 시 파티션 조건이 where 절에 안들어가도 되는 설정  



