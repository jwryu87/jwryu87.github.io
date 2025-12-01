---
layout: default
title: ACID
parent: 4. 트랜잭션
grand_parent: DB (데이터베이스)
nav_order: 1
---

# ACID (데이터베이스 트랜잭션)
{: .fs-8 }

4.1 트랜잭션 특성
{: .label .label-purple }

> 암기: **원일고영**

---

## 핵심 키워드

`원자성` `일관성` `고립성` `영속성`

---

## 정의/개념

데이터 정확성, 일관성, 무결성 보장 데이터베이스 논리적 작업 단위

---

## 특징 (데이터베이스 트랜잭션 특징 설명)

| 특징 | 개념도 | 설명 |
|:-----|:-------|:-----|
| **원자성<br>(Atomicity)** | Transaction<br>연산1 ─ 연산n → Commit<br>        └─→ Rollback | - 분해가 불가능한 수행 단위로 완전히 수행, 수행되지 않음<br>- 구현기법: All or Nothing, Commit or Rollback<br>- 기능: 회복 |
| **일관성<br>(Consistency)** | Database<br>일관된 상태 → Committed Transaction → 일관된 상태 | - 트랜잭션이 성공적으로 완료되면 언제나 모순이 없는 상태 유지<br>- 무결성 제약조건, 사용자가 요구하는 논리적 요건의 충족<br>- 구현기법: 도메인 무결성, 릴레이션 무결성<br>- 기능: 무결성 제약조건, 동시성 제어 |
| **격리성<br>(Isolation)** | Transaction 의한 갱신 중<br>Data → 접근 제어 | - 트랜잭션 실행 중에는 다른 트랜잭션 접근 불가<br>- 구현기법: isolation level<br>- 기능: 동시성 제어 |
| **영속성<br>(Durability)** | Commit 정보 기록<br>DB → 장애 시 회복 | - 트랜잭션이 실행이 성공적으로 완료하면 그 결과는 영속적임<br>- 구현기법: Archive, 로그, Redo/Undo 기반 회복<br>- 기능: 회복 |

- 데이터베이스는 4가지 특징으로 기본 동작 진행

---

## 연계 토픽

- [트랜잭션 상태 전이](/docs/db/04-transaction/transaction-state)
- [격리성(Isolation Level)](/docs/db/04-transaction/isolation-level)
- [동시성 제어](/docs/db/05-concurrency/locking)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
