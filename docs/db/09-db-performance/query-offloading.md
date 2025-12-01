---
layout: default
title: 쿼리오프로딩
parent: 9. DB 성능
grand_parent: DB (데이터베이스)
nav_order: 5
---

# 쿼리오프로딩 (Query Offloading)
{: .fs-8 }

9.5 쿼리 부하 분산
{: .label .label-purple }

---

## 핵심 키워드

`Update/Read 트랜잭션 분리` `Master DB` `Staging DB` `Slave DB` `CDC`

---

## 정의/개념

DB 트랜잭션에서 Update와 Read를 분리하여 DB 처리량을 증가시켜 DB 성능을 향상시키는 기법

---

## 개념도

```
                    APPLICATION
                         │
          ┌──────────────┴──────────────┐
          │                             │
    ┌─────┴─────┐                 ┌─────┴─────┐
    │Connection │                 │Connection │
    │   Pool    │                 │   Pool    │
    │(Update    │                 │(Read      │
    │ purpose)  │                 │ purpose)  │
    └─────┬─────┘                 │* Load     │
          │                       │ Balancing │
          │                       │ /HA       │
          │                       │ required  │
          │                       └─────┬─────┘
          │                             │
    ┌─────┴─────┐   ┌─────────┐   ┌─────┴─────┐
    │ Master DB │──▶│Staging  │──▶│ Slave DB  │
    │           │   │   DB    │   │           │
    └───────────┘   └────┬────┘   └───────────┘
                   Replication   Replication
                      (CDC)         (CDC)
```

---

## 구성요소

| 구분 | 구성요소 | 설명 |
|:-----|:---------|:-----|
| **DB** | Master DB | Update 트랜잭션(Create/Delete/Update)만 수행 |
| | Staging DB | Slave DB로 복제하기 위한 중간 경유지 역할<br>Master DB에서 다수의 Slave DB로 직접 복제 시 성능저하 유발을 방지 |
| | Slave DB | Read 트랜잭션만 수행하며, N개의 Slave DB로 구성<br>Slave DB 장애 시 다른 Slave DB 인스턴스에 접근할 수 있도록 HA 기능 제공 |
| **복제기술** | CDC<br>(Change Data Capture) | Source DB의 Back Log를 읽어서, Target DB에 replay 하는 형식<br>제품: Oracle의 Golden Gate, Quest의 Share Flex, 오픈소스 Galera |

---

## 연계 토픽

- [샤딩](/docs/db/09-db-performance/sharding)
- [파티셔닝](/docs/db/09-db-performance/partitioning)
- [분산 DB](/docs/db/02-db-basics/distributed-db)

---

## 학습 체크리스트

- [ ] 쿼리오프로딩 개념 이해
- [ ] Master/Staging/Slave DB 역할 암기
- [ ] CDC 개념 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료

