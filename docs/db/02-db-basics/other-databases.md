---
layout: default
title: 기타 데이터베이스
parent: 2. 데이터베이스 기본
grand_parent: DB (데이터베이스)
nav_order: 6
---

# 기타 데이터베이스
{: .fs-8 }

2.1 DB 유형
{: .label .label-purple }

---

## MongoDB

### 핵심 키워드

`JSON` `Document` `Collections`

### 정의/개념

JSON 데이터 구조, CRUD 위주 트랜잭션 처리, Memory Mapping 기반 Document 지향 NoSQL 데이터베이스

### 아키텍처 (RDBMS vs MongoDB)

| RDBMS | MongoDB |
|:------|:--------|
| Database | Database |
| Tables | Collections |
| Rows | Documents |
| Columns | Fields |

### 기능

| 구분 | 기능 | 핵심 |
|:-----|:-----|:-----|
| **쿼리** | Ad-hoc Query | 필드, 범위, 쿼리 검색 지원 |
| | Index | Primary/Secondary 인덱스 인덱싱 |
| **실행** | Server Side JavaScript | Query, Aggregation 사용 가능 |
| | 고정 크기 Collection | Capped collection 지원 |

### 기술

| 구분 | 기술 | 핵심 |
|:-----|:-----|:-----|
| **성능** | Load Balancing | 샤딩 이용 |
| | Replication | Replica Set 사용 |
| **파일관리** | File Storage | Chunk 단위 분리 |
| | Aggregation | MapReduce 사용 |

---

## BASE 이론

### 핵심 키워드

`Basically Available` `Soft State` `Eventually Consistent`

### 정의/개념

ACID에 상대적으로 가용성과 성능 향상을 중시하며, 최종적으로 데이터 일관성을 유지하는 상태가 되게 하는 분산 시스템의 특성

### BASE 트랜잭션(Transaction) 속성

| 속성 | 목적 | 설명 |
|:-----|:-----|:-----|
| **Basically Available** | 분산 시스템의<br>가용성 확보 | - 일부의 실패에도 항상 가용성을 중시<br>- 다수의Storage에 복사본을 저장 |
| **Soft State** | 분산Node간<br>Data | - 노드의 상태는 내부에 포함된 정보에 의해 결정되는 것이 아니라 외부에서 전송된 정보를 통해 결정<br>- 분산 노드간 업데이트는 데이터가 노드에 도달 시점에 수행 |
| **Eventually Consistent** | 일시적<br>비 일관성 허용 | - 데이터가 해당 노드에 도달 전까지는 데이터에 일관성이 없는 상태로Data도착 후 일관성 회복 |

### BASE와 ACID속성 비교

| 비교 속성 | BASE | ACID |
|:---------|:-----|:-----|
| **적용 분야** | - Cloud, NoSQL | - 일반RDBMS |
| **속성 범위** | - System전체 특성 | - Transaction한정 |
| **일관성 측면** | - Node간Data도달 전은 일관성이<br>유지 안 되는 약한 일관성 | - 항상 강한 일관성 보장 |
| **중점 사항** | - 언제나 접근 가능한Availability중시 | - Commit시의 일관성에 중시 |
| **시스템 측면** | - 접근성,성능성 | - 엄격한 데이터 관리 |
| **효율성** | - Query Design이 중요<br>- Application종속 설계 | - Table Design이 중요(정규화)<br>- Application독립적 설계 |

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
