---
layout: default
title: 격리성 (Isolation Level)
parent: 4. 트랜잭션
grand_parent: DB (데이터베이스)
nav_order: 3
---

# 격리성 (Isolation Level)
{: .fs-8 }

4.3 격리 수준
{: .label .label-purple }

---

## 핵심 키워드

`Read Uncommitted` `Read Committed` `Repeatable Read` `Serializable`

---

## 정의/개념

병행 트랜잭션 실행 시 일관성 있게 데이터를 읽을 수 있도록 고립성을 유지하기 위한 데이터를 허용하는 수준

---

## 특징 (고립화 수준, Isolation level 설명)

| Isolation level | 설명 | 특징 |
|:----------------|:-----|:-----|
| **Read Uncommitted<br>(Level 0)** | - 아직 커밋 되지 않은 데이터를 다른 트랜잭션이 읽는 것을 허용<br>- 고립 수준이 가장 낮은 명령어로 자신의 데이터에 공유락 걸지 않음 | - 모든 이상 현상 발생<br>- 오라클 지원 안함 |
| **Read Committed<br>(Level 1)** | 트랜잭션이 커밋되어 확정된 데이터만 읽는 것을 허용<br>- 데이터를 읽는 동안 공유락 설정 | - Dirty read 현상 해결<br>- 오라클 기본 설정(default) |
| **Repeatable Read<br>(Level 2)** | - 공유락과 배타락을 트랜잭션이 종료할 때까지 유지하여 다른 트랜잭션이 자신의 데이터를 update 또는 delete 할 수 없도록 함 | - Non-Repeatable Read 해결 |
| **Serializable<br>(Level 3)** | - 고립수준이 가장 높은 레벨로 타 트랜잭션의 insert 금지<br>- index에 공유락을 설정하거나 undo 데이터를 사용하여 구현 | - Phantom Read 해결<br>- 데이터의 동시성 제일 낮음 |

- SET TRANSACTION ISOLATION LEVEL "Isolation level" 을 실행하여 레벨 설정

---

## 이상 현상과 격리 수준 관계

| 격리 수준 | Dirty Read | Non-Repeatable Read | Phantom Read |
|:---------|:-----------|:--------------------|:-------------|
| **Read Uncommitted** | 발생 | 발생 | 발생 |
| **Read Committed** | 해결 | 발생 | 발생 |
| **Repeatable Read** | 해결 | 해결 | 발생 |
| **Serializable** | 해결 | 해결 | 해결 |

---

## 연계 토픽

- [ACID](/docs/db/04-transaction/acid)
- [동시성 제어](/docs/db/05-concurrency/locking)
- [MVCC](/docs/db/05-concurrency/mvcc)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
