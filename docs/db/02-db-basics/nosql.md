---
layout: default
title: NoSQL
parent: 2. 데이터베이스 기본
grand_parent: DB (데이터베이스)
nav_order: 1
---

# NoSQL
{: .fs-8 }

2.1 DB 유형
{: .label .label-purple }

> 암기: **구조(칼키도그), 절차(도쿼패키후최)**

---

## 핵심 키워드

`스키마 유연성` `복잡쿼리 불필요` `수평적 확장` `비관계형` `조인불가` `중복허용` `BASE` `CAP` `PACELC`

---

## 정의/개념

Schemaless, 비관계형, 조인불가, 중복허용, 수평적 확장, BASE 데이터베이스

---

## 구조

### NoSQL의 3가지 구조 설명

| 구조 | 개념도 | 구조 특성 |
|:-----|:-------|:---------|
| **Key-Value** | Key → Value<br>Key → Value | - 키-값 쌍 데이터 표현<br>- 단순구조 빠른 연산, but 비효율적 범위질의<br>- 세션 정보 및 사용자 프로파일등 설정정보 저장에 활용<br>- 유형: Dynamo, Redis |
| **Column<br>Family** | Key → Value → Value<br>      ↓<br>Key → Value → Value | - 값(Value) 열(Column) 기반 모델링 표현<br>- 값의 지속적 다차원 Map 구성<br>- 유형: HBase, Cassandra |
| **Document** | Key → Document<br>(XML, JSON) | - 값(Value) 부분에 문서 저장<br>- 암묵적 스키마 사용, 자유로운 속성 추가 가능<br>- 실시간 분석 등에 활용<br>- 유형: CouchDB, MongoDB |
| **Graph** | Node ── Relationship ── Node<br>Property | - 노드, 관계, 속성 통한 데이터 표현<br>- 높은 확장성 보장<br>- 유형: Neo4J, AgensGraph |

- RDBMS의 SQL 질의와 ACID 특성 대한 지원을 유지하고 NoSQL 같은 확장성과 유연성을 가지는 NewSQL 대두

---

## 패턴

### NoSQL의 주요 패턴

| 구성요소 | 설명 / 설정 |
|:---------|:-----------|
| **Denormalization<br>(비정규화)** | - NoSQL의 가장 기본적인 패턴<br>- 생성 초기부터 데이블 중복허용<br>- 성능향상, 쿼리복잡도 감소 효과 |
| **Aggregation<br>(집합)** | - 키값만 동일하다면 Row 구조는 상관없음<br>- RDB와 달리 구조에 종속지 않음<br>- Soft Scheme, Schemeless 특성 |
| **Application Side<br>Join<br>(프로그램 조인)** | - 프로그램 로직단에서 Join 하는 패턴<br>- Join 필요 테이블을 Req/Res 만큼 I/O발생<br>- 일관성 향상, 스토리지 절약효과 |
| **Atomic<br>Aggregation<br>(원자성 보장<br>집합)** | - 원자성을 보장하기 위한 비정규화 패턴<br>- 트랜잭션 보장으로 불일치성 해결<br>- 분산환경의 트랜잭션 보장위한 패턴 |
| **Adjacent Lists<br>(인접 리스트)** | - 전통적인 자료구조 형태를 지닌 패턴<br>- Linked List와 같은 구조형<br>- Tree, parentNode, childNode 포인터 저장 |

- 패턴은 데이터모델링 절차의 테이블설계에서 적용됨. 또한 NoSQL 모델을 분류시 크게 3가지로 압축.

---

## 모델링 절차

도메인 모델 파악 → 쿼리결과 디자인 → 패턴 이용 모델링 → 기능 최적화 → 후보 NoSQL 선정 → NoSQL 최적화

---

## 연계 토픽

- [RDBMS](/docs/db/02-db-basics/three-level-architecture)
- [NewSQL](/docs/db/02-db-basics/newsql)
- [CAP 이론](/docs/db/02-db-basics/cap-theorem)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
