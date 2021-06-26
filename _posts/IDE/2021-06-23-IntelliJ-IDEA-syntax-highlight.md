---
layout: post
title: (IDEA) IntelliJ에서 hql 문서 syntax highlight 적용하기
date: 2021-06-23 12:00:00 +09:00
tags: IDEA, IntelliJ
comments: true
---

IntelliJ 에서 초반 세팅에는 .hql 문서에 대해서는 syntax highlight가 적용되지 않을 수 있다.

.hql 문서에도 .sql 문서와 같이 하이라이팅을 주려고 한다.

아래와 같이 Editor 에서 file types 를 찾아가서 SQL 타입에 .hql 형식도 추가시킨다.

![editor]({{ site.url }}/assets/인텔리J_syntax_highlight.png)

하지만 이 방법은 하이브에 sql syntax highlight를 적용하는 임시방편일뿐이고  
Apache Hive 데이터 소스를 적용하는게 정석적인 방법일거 같다.