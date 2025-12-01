---
layout: default
title: CQRS
parent: 4. 아키텍처
grand_parent: SW (소프트웨어공학)
nav_order: 2
---

# CQRS (Command and Query Responsibility Segregation)
{: .fs-8 }

4.1 아키텍처 패턴
{: .label .label-purple }

---

## 핵심 키워드

`MSA` `CUD와 R의 분리` `Command` `Query`

---

## 정의/개념

데이터를 변경하는 삽입·삭제·입력 처리와 데이터를 조회는 쿼리의 책임을 분리하는 패턴

---

## 개념도

```
┌─────────────────────────────────────────────────────┐
│              Customer Command service                │
│  ┌─────────────┐      ┌───────────────────┐        │
│  │   Command   │      │     Customer      │        │
│  │   service   │─────►│   Command model   │        │
│  │  interface  │      │                   │        │
│  └─────────────┘      └─────────┬─────────┘        │
│                                 │ ①                 │
│                                 ▼                   │
│                          ┌──────────┐               │
│                          │ Database │               │
│                          └──────────┘               │
│                                 │ ②                 │
│  ┌─────────────┐      ┌────────┴──────────┐        │
│  │   Query     │      │     Customer      │        │
│  │   service   │◄─────│    Query model    │        │
│  │  interface  │      │                   │        │
│  └─────────────┘      └───────────────────┘        │
│              Customer Query service                  │
└─────────────────────────────────────────────────────┘
           │
     Application
```

---

## 구성요소

| 구성요소 | 설명 |
|:---------|:-----|
| **Event Sourcing** | Application 내의 모든 Activity를 이벤트로 전환해서 이벤트 스트림(Event Stream)을 별도의 Database에 저장하는 방식 |
| **Message Queue** | - Event Sourcing 저장소<br>- 직접 구현 or Kafka 등 |
| **ORM** | - Object Relational Mapping, 객체-관계 매핑<br>- DB Table ← 매핑 → Model Object<br>- 비즈니스 로직 분리 집중<br>- 재사용성 및 유지보수성 증가<br>- DBMS 종속성 감소 |
| **Polyglot DB** | 상이한 데이터 저장 요건에 맞추어 상황에 따라 다른 데이터 저장소 기술을 사용 |

---

## 연계 토픽

- [MSA](/docs/sw/04-architecture/msa)
- [SAGA](/docs/sw/04-architecture/saga)
- [Event Storming](/docs/sw/04-architecture/event-storming)

---

## 학습 체크리스트

- [ ] CQRS 정의 및 개념 이해
- [ ] Command와 Query 분리 이유 이해
- [ ] Event Sourcing, Message Queue, ORM, Polyglot DB 이해
- [ ] MSA와의 관계 이해

---

## 참고자료

- 정보관리기술사 SW 학습자료

