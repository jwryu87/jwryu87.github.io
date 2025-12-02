---
layout: default
title: Cache Memory Write
parent: 5. 캐시메모리
grand_parent: CAOS (컴퓨터구조/OS)
nav_order: 4
---

# Cache Memory의 Write Through, Write Back
{: .fs-8 }

5.3 쓰기 정책
{: .label .label-green }

---

## 핵심 키워드

`동시변경` `우선변경` `VI 프로토콜` `MESI 프로토콜`

---

## 정의/개념

- **Write Through**: 프로세서에서 메모리 쓰기 요청 시, 캐시 내용-메인 메모리 **동시 변경** 캐시 쓰기 정책
- **Write Back**: 프로세서에서 메모리 쓰기 요청 시, 캐시 내용 **우선 변경**, 메인 메모리 블록 복사 후 작업 캐시 쓰기 정책

---

## Write-Through vs Write-Back 비교

| 비교항목 | Write-Through | Write-Back |
|:--------|:--------------|:-----------|
| **구성도** | CPU → 동시에 Write → 캐시 메모리 → 주기억장치 | CPU → Swap-Out시 Write → 캐시 메모리 → 주기억장치 |
| **동작원리** | 캐시와 메모리에 동시에 기록되는 방식 | 캐시 먼저 기록 후 나중에 메모리에 기록되는 방식 |
| **장점** | - 단순 구조 아키텍처<br>- 캐시와 주기억장치 간 일관성 유지 | - 기억장치 쓰기동작 횟수 최소화 및 쓰기시간 단축<br>- CPU의 메모리 접근 최소화 |
| **단점** | - 쓰기 동작으로 인한 버스의 트래픽 증가<br>- 빈번한 주기억장치 접근으로 쓰기 시간 증가 | - 상대적으로 복잡한 구조 아키텍처<br>- 캐시 일관성(Cache Coherence) 문제 발생 |
| **일관성 유지 기법** | VI Protocol (Valid-Invalid) | MESI Protocol |

---

## 일관성 문제

- 2가지방식 모두 캐시 일관성(Cache coherence) 불일치 현상발생 가능하며, 일관성 유지를 위한 기법 적용 필요

---

## 연계 토픽

- [캐시 일관성](/docs/caos/05-cache-memory/cache-coherence)
- [MESI 프로토콜](/docs/caos/05-cache-memory/mesi-protocol)

---

## 학습 체크리스트

- [ ] Write Through vs Write Back 차이
- [ ] 각 방식의 장단점
- [ ] 일관성 유지 기법

---

## 참고자료

- 정보관리기술사 컴퓨터구조/OS 학습자료

