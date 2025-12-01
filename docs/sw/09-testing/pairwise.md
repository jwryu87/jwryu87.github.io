---
layout: default
title: 페어와이즈 테스팅
parent: 9. 소프트웨어 테스트
grand_parent: SW (소프트웨어공학)
nav_order: 20
---

# 페어와이즈 테스팅 (Pairwise Testing)
{: .fs-8 }

9.4 기타 테스트
{: .label .label-blue }

---

## 핵심 키워드

`절차: 그룹선정 → 입력값 파악 → Pair 조합 구성`

---

## 정의/개념

2가지 요소 개별 조합만을 고려, **적은 Test Set 구성**, SW 결함발견 **명세기반 테스트 기법**

---

## 절차

| 테스팅 절차 | 절차 설명 |
|:-----------|:---------|
| **① 그룹선정** | - 모든 테스트 케이스 경우의 수 확인<br>- 두 가지 요소의 조합 대상 그룹 선정 |
| **② 입력값 파악** | - 각 그룹 별 선택 가능한 입력 값(대표 값, 경계 값) 파악<br>- 각 파라미터의 각 값들을 중복되지 않게 배열 |
| **③ Pair 조합 구성** | - 각각 값과 순차적으로 중복되지 않게 배정<br>- 입력 값들 간의 최소한 한번씩 Pair한 조합 구성 |

---

## 테스트 케이스 예제

### 문제 설정

| 입력 변수 | Server | Browser | Network Type |
|:---------|:-------|:--------|:-------------|
| 입력 값 | Unix | Chrome | Wired |
| | Linux | Edge | Wireless |

- 문제의 입력 변수에 따른 입력 값 확인

---

### 단계별 테스트 케이스 도출

| 테스팅 절차 | 테스트 케이스 | 상세 설명 |
|:-----------|:-------------|:---------|
| **그룹 선정** | Server: Unix, Unix, Unix, Unix, Linux, Linux, Linux, Linux<br>Browser: Chrome, Chrome, Edge, Edge, Chrome, Chrome, Edge, Edge<br>Network Type: Wired, Wireless, Wired, Wireless, Wired, Wireless, Wired, Wireless | - 모든 테스트 케이스 경우의 수 확인<br>- 3가지 파라미터에 대한 모든 조합을 고려해 테스트 케이스 나열<br>- 3 가지 파라미터를 고려 시 총 8가지(2 X 2 X 2)의 테스트 케이스 도출 |
| **입력값 파악** | Server: Unix, Unix, Unix, Unix, Linux, Linux, Linux, Linux<br>Browser: Chrome, Chrome, Edge, Edge, Chrome, Chrome, Edge, Edge<br>Network Type: Wired, Wireless, Wired, Wireless, Wired, Wireless, Wired, Wireless | - 두 가지 요소의 개별 조합 (Discrete Combinations)만 고려<br>- 두 가지 요소(파라미터)의 각 값들을 중복되지 않게 배열 |
| **Pair 조합 구성** | Server: Unix, Unix, Linux, Linux<br>Browser: Chrome, Edge, Chrome, Edge<br>Network Type: Wired, Wireless, Wireless, Wired | - 3가지 파라미터를 고려 시 총 4가지의 테스트 케이스 도출 |

---

## 테스트 케이스 수 비교

| 방식 | 테스트 케이스 수 | 계산식 |
|:-----|:---------------|:-------|
| **전수 테스트** | 2³ = 8개 | 모든 조합 |
| **Pairwise 테스트** | 4개 | 2요소 조합만 |

{: .highlight }
> 입력 변수 및 값이 늘어나면 조합의 수가 기하급수적으로 늘어 수직업 오류 발생 가능성이 높아짐 → Pairwise로 효율적 테스트

---

## Pairwise 테스팅 장점

| 장점 | 설명 |
|:-----|:-----|
| **테스트 케이스 감소** | 전수 조합 대비 테스트 케이스 수 대폭 감소 |
| **결함 탐지율 유지** | 대부분의 결함은 2개 요소 조합에서 발생 |
| **비용 효율성** | 적은 테스트 케이스로 높은 커버리지 달성 |
| **도구 지원** | PICT, ACTS 등 자동화 도구 활용 가능 |

---

## Pairwise 테스팅 도구

| 도구 | 설명 |
|:-----|:-----|
| **PICT** | Microsoft 제공 무료 도구 |
| **ACTS** | NIST 개발 Combinatorial Testing 도구 |
| **AllPairs** | James Bach 개발 |
| **Hexawise** | 상용 Pairwise 테스팅 도구 |

---

## 연계 토픽

- [명세기반 테스트](/docs/sw/09-testing/specification-based)
- [테스트 케이스](/docs/sw/09-testing/test-case)

---

## 학습 체크리스트

- [ ] Pairwise 테스팅 3단계 절차 이해
- [ ] 전수 테스트 대비 케이스 수 감소 원리 이해
- [ ] 2요소 조합의 결함 탐지 효과 파악
- [ ] Pairwise 도구 종류 파악

---

## 참고자료

- 정보관리기술사 SW 학습자료

