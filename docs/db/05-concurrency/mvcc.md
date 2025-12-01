---
layout: default
title: MVCC
parent: 5. 동시성 제어
grand_parent: DB (데이터베이스)
nav_order: 4
---

# MVCC (Multi Version Concurrency Control)
{: .fs-8 }

5.4 다중 버전
{: .label .label-purple }

---

## 핵심 키워드

`직렬 가능성 보장` `SCN(System Change Number)` `CR Copy` `Undo` `MGA` `Rollback Segment`

---

## 정의/개념

쓰기(Write) 세션이 읽기(Read) 세션을 블로킹(blocking)하지 않고, 읽기 세션이 쓰기 세션을 블로킹하지 않게 서로 다른 세션이 동일 데이터에 접근했을 때 각 세션마다 스냅샷 이미지를 보장해주는 메커니즘

---

## MGA(Multi Generation Architecture) : PostgreSQL 에서 사용하는 방식

### 레코드 갱신 처리 방식 사용

```
┌────┬──────────┐  ┌────┬──────────┐  ┌────┬──────────┐
│ id │ lastname │  │ id │ lastname │  │ id │ lastname │
├────┼──────────┤  ├────┼──────────┤  ├────┼──────────┤
│ 1  │ Tascioni │  │ 1  │ Tascioni │  │ 1  │ Tascioni │
│ 2  │ Agos     │  │ 2  │ Agos     │  │ 2  │ Agos     │
│ 3  │ Gold     │  │ 3  │ Gold     │  │ 3  │ Gold     │
│ 4  │ Sweeney  │  │ 4  │ Sweeney  │  │ 4  │ Sweeney  │
│    │          │  │Update│ lockhart │  │Commit│ lockhart│
└────┴──────────┘  └────┴──────────┘  └────┴──────────┘
```

1) 어떤 데이터에 업데이트가 일어나면 기존 데이터는 그대로 두고 새로운 데이터가 추가
2) 기존 데이터에 표시 (기존 데이터가 지워지지 않음)
3) 주기적으로 VACUUM
4) 업데이트가 발생한 데이터의 물리적 위치가 변경
5) 업데이트를 할 때마다 인덱스 수정작업이 항상 발생

---

## Rollback Segment : Oracle 에서 사용하는 방식

```
셀렉트... (SCN 1031)
         │
         │    CR 블록 생성
         ▼    ▼
┌──────┐      ┌───────────┐
│ 1011 │      │  롤백 세그먼트  │
├──────┤      │  ┌───────┐ │
│ 1033 │──────│  │이전이미지│ │
├──────┤  1021│  └───────┘ │
│ 1015 │──────│            │
├──────┤      │  ┌───────┐ │
│ 1035 │      │  │이전이미지│ │
├──────┤  1025│  └───────┘ │
│ 1021 │      │            │
└──────┘      └───────────┘
```

- 업데이트가 실행되면 기존 데이터 블록을 새로운 데이터로 변경하고 이전 데이터는 Rollback Segment 에 보관
- MGA 와의 차이점은 업데이트 시 데이터의 물리적인 위치가 변경되지 않음

---

## 연계 토픽

- [데이터베이스 병행제어](/docs/db/05-concurrency/locking)
- [Timestamp Ordering](/docs/db/05-concurrency/timestamp-ordering)

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악

---

## 참고자료

- 정보관리기술사 데이터베이스 학습자료
