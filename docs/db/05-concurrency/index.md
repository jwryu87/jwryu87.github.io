---
layout: default
title: 5. 동시성 제어
parent: DB (데이터베이스)
nav_order: 5
has_children: true
permalink: /docs/db/05-concurrency
---

# 동시성 제어 (Concurrency Control)

다중 트랜잭션의 동시 실행을 관리하는 기법에 관한 학습 자료입니다.

---

## 토픽 목록

| 토픽 | 설명 |
|:-----|:-----|
| [Locking](/docs/db/05-concurrency/locking) | 잠금 기반 동시성 제어 |
| [Two Phase Locking(2PL)](/docs/db/05-concurrency/two-phase-locking) | 2단계 잠금 프로토콜 |
| [Timestamp Ordering](/docs/db/05-concurrency/timestamp-ordering) | 타임스탬프 기반 순서화 |
| [MVCC](/docs/db/05-concurrency/mvcc) | 다중 버전 동시성 제어 |
| [Validation(낙관적 검증)](/docs/db/05-concurrency/validation) | 낙관적 동시성 제어 |
| [동시성 제어 시 문제점](/docs/db/05-concurrency/concurrency-problems) | 교착상태, 기아 현상 등 |

