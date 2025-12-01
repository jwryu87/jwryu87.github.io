---
layout: default
title: 버퍼 관리 정책
parent: 6. 회복
grand_parent: DB (데이터베이스)
nav_order: 5
---

# 데이터베이스 버퍼 관리 정책
{: .fs-8 }

6.1 회복 기법
{: .label .label-yellow }

---

## 핵심 키워드

`STEAL(수정된 Dirty Page)` `FORCE(완료된 Dirty Page)` `No-Steal` `No-Force`

---

## 정의/개념

페이지 버퍼 관리자가 메모리 버퍼에 저장된 페이지를 언제 디스크에 기록할지 결정 정책

---

## 유형

### Database 버퍼관리 정책 유형

| 버퍼 관리 정책 | | 설명 |
|:-------------|:---------|:-----|
| **STEAL** | Steal 정책 | - 트랜잭션이 메모리 버퍼 사용할 때, 가장 오랫동안 사용되지 않은 Dirty Page를 디스크에 Flush하고 버퍼를 해제<br>- 수정된 Page가 언제든 Disk로 쓰여질 수 있으므로 Rollback을 위해 **Undo Logging이 필요** |
| | No-Steal 정책 | - 트랜잭션이 완료될 때까지 Dirty Page를 반드시 Buffer에 유지<br>- 수행중인 모든 트랜잭션이 Buffer에 유지되도록 충분한 Buffer 공간 필요 |
| **FORCE** | Force 정책 | - 트랜잭션이 commit할 때 트랜잭션이 갱신한 모든 Dirty Page를 Disk로 Flush<br>- 트랜잭션이 완료될 때마다 매번 Disk에 Write 수행을 하므로 Performance 이슈 발생 |
| | No-Force 정책 | - 트랜잭션이 완료되어 Commit하더라도 즉시 Disk로 반영하지 않는 정책<br>- 수정된 Dirty Page를 다른 트랜잭션이 또 수정할 경우 Disk로 Write 하는 동작은 줄어드나, 장애 발생과 데이터 변경 보장을 위해 반드시 **Redo Logging이 필요** |

---

## 정책 조합 및 특징

| 구분 | Steal + No-Force | No-Steal + Force |
|:-----|:-----------------|:-----------------|
| **Undo** | 필요 | 불필요 |
| **Redo** | 필요 | 불필요 |
| **복구 복잡도** | 복잡 | 단순 |
| **성능** | 높음 | 낮음 |
| **버퍼 관리** | 효율적 | 비효율적 |
| **대표 기법** | **ARIES** | Shadow Paging |

---

## 정책 요약

- **Steal 정책**: 수정된 Dirty Page가 언제 Disk로 Flush될지 결정
- **Force 정책**: 완료된 Transaction(Commit 완료)의 Dirty Page가 언제 Disk로 Flush될지 결정

---

## 연계 토픽

- [ARIES](/docs/db/06-recovery/aries)
- [로그 기반 회복](/docs/db/06-recovery/log-based-recovery)
- [체크포인트](/docs/db/06-recovery/checkpoint)

---

## 학습 체크리스트

- [ ] STEAL/No-Steal 정책 차이 이해
- [ ] FORCE/No-Force 정책 차이 이해
- [ ] 정책 조합에 따른 Undo/Redo 필요성 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료


