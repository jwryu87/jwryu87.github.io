---
layout: default
title: CAP 이론
parent: 2. 데이터베이스 기본
grand_parent: DB (데이터베이스)
nav_order: 2
---

# CAP 이론
{: .fs-8 }

2.1 DB 유형
{: .label .label-purple }

---

## 핵심 키워드

`Consistency` `Availability` `Partition Tolerance`

---

## 정의/개념

분산 데이터베이스 환경, 일관성, 가용성, 파티션 허용 이중 두가지 특성 가능 이론

---

## CAP 특성

| 특성 | 핵심 |
|:-----|:-----|
| **Consistency** | 모든 노드가 같은 시간에 같은 데이터를 보여준다. |
| **Availability** | 특정 노드가 장애 발생해도 서비스가 가능해야 한다.(노드 장애) |
| **Partition Tolerance** | 노드간에 통신 문제가 발생해도 동작해야 한다.(네트워크 장애) |

---

## CAP 이론

```
              A
             /\
      CA    /  \    AP
   - RDBMS /Pick\  NoSQL
   - Oracle\ Two/  - Dynamo
   - MySQL  \  /   - Cassandra
   - MS-SQL  \/    - CouchDB
            C────────P
              CP
            NoSQL
            - Hbase
            - MongoDB
            - Redis
```

| Pick Two | 핵심 |
|:---------|:-----|
| **C+A** | 미션 크리티컬 트랜잭션 |
| **A+P** | 비동기화 서비스 |
| **C+P** | 대용량 분산파일 시스템 |

---

## 한계

| 한계 | 핵심 |
|:-----|:-----|
| **일관성-가용성<br>선택문제** | 완벽한 CP, 완벽한 AP<br>미존재 |
| **정상상황 설명<br>불가능** | 정상상황에서도 분산<br>시스템 상충 특성 존재 |

---

## 연계 토픽

- [PACELC](/docs/db/02-db-basics/pacelc)
- [NoSQL](/docs/db/02-db-basics/nosql)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
