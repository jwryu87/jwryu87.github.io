---
layout: default
title: PACELC 이론
parent: 2. 데이터베이스 기본
grand_parent: DB (데이터베이스)
nav_order: 3
---

# PACELC 이론
{: .fs-8 }

2.1 DB 유형
{: .label .label-purple }

---

## 핵심 키워드

`파티션(P)` `정상상황(C)` `Availability` `Latency` `Consistency`

---

## 정의/개념

CAP 이론 단점 보완, 네트워크 장애 상황, 정상상황 이론

---

## 특성

| 특성 | 핵심 |
|:-----|:-----|
| **파티션(P)** | A(Availability), C(Consistency) 고려 |
| **정상상황(C)** | L(Latency), C(Consistency) 고려 |

---

## 메커니즘

```
              EC
             /  \
    MongoDB /    \  VoltDB
           /      \  Megastore
          /        \  HBase
        PA──────────PC
       /              \
   Dynamo            PNUTS
   Cassandra
              EL
```

| Pick Two | NoSQL |
|:---------|:------|
| **PA+EL** | Cassandra, Dynamo |
| **PA+EC** | MongoDB |
| **PC+EL** | PNUTS |
| **PC+EC** | HBase, VoltDB |

---

## 연계 토픽

- [CAP](/docs/db/02-db-basics/cap-theorem)
- [NoSQL](/docs/db/02-db-basics/nosql)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
