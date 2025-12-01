---
layout: default
title: Hadoop 3.0
parent: 1. 빅데이터
grand_parent: DB (데이터베이스)
nav_order: 4
---

# Hadoop V3.0
{: .fs-8 }

1.2 처리·플랫폼
{: .label .label-yellow }

---

## 핵심 키워드

`Pig` `Hive` `HBase` `Job Tracker` `MapReduce` `Hadoop Common`

---

## 정의/개념

HDFS, MapReduce 사용 대용량 데이터 병렬처리 자바기반 오픈소스 프레임워크

---

## 아키텍처

```
┌─────────────────────────────────────────────────┐
│  개발    │ Pig │ Hive │ Chukwa │ HBase │ Zookeeper │
├─────────────────────────────────────────────────┤
│          │      master      │  slave  │  slave   │
│ Platform │   Job Tracker    │Task Tracker│Task Tracker│
│  Layer   ├──────────────────────────────────────┤
│          │   Name Node      │Data Node│Data Node │
├─────────────────────────────────────────────────┤
│  Hadoop  │      Hadoop Common (core library)     │
│  Core    │                                       │
└─────────────────────────────────────────────────┘
           Rack A        Rack B        Rack C
         마스터 서버      PC #1         PC #2
```

---

## 구성요소

| 구분 | 구성요소 | 특징 |
|:-----|:---------|:-----|
| **개발측면** | Pig, Hive, Chukwa,<br>HBase, Zookeeper | 개발 도구 |
| **플랫폼<br>측면** | Job Tracker | MapReduce Layer |
| | Name Node | Namespace, 블록매핑,<br>Metadata, 복제 |
| | Data Node | Read/Write 처리,<br>블록처리 |
| **코어 측면** | Hadoop Common | 코어 라이브러리 |

---

## 연계 토픽

- [HDFS](/docs/db/01-bigdata/data-lake)
- [MapReduce](/docs/db/01-bigdata/lambda-kappa)
- [빅데이터 입출력 구조](/docs/db/01-bigdata/data-fabric)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
