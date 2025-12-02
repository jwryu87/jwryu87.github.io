---
layout: default
title: 페이지 교체 알고리즘
parent: 4. 가상메모리
grand_parent: CAOS (컴퓨터구조/OS)
nav_order: 7
---

# 페이지 교체 알고리즘 (Replacement Algorithm)
{: .fs-8 }

4.3 문제/최적화
{: .label .label-yellow }

---

## 핵심 키워드

`주기억장치 공간 확보` `페이지 프레임` `FIFO` `OPT` `LRU` `LFU` `NUR` `Second Chance` `MFU`

---

## 정의/개념

**페이지 교체 알고리즘**은 주기억장치 공간 확보 위해 어떤 **페이지 프레임**을 선택하여 교체할 것인지 결정하는 **알고리즘 기법**(Page-in, Page-out)입니다.

---

## 기초개념

- **페이지 부재(Page Fault)**: CPU가 접근하려는 페이지가 메모리에 없는 경우 → 페이지 테이블의 Valid bit=0
- **페이지 교체 알고리즘**: 주기억장치 공간 확보 위해 어떤 페이지 프레임을 선택하여 교체할 것인지 결정하는 알고리즘 기법(Page-in, Page-out)
- **프레임**: 물리 메모리를 일정한 크기로 나눈 블록
- **페이지**: 가상 메모리를 일정한 크기로 나눈 블록

---

## 페이지 교체 알고리즘 유형

```
                    페이지 교체 알고리즘
    ┌──────┬──────┬──────┬──────┬──────┬──────┐
    │ OPT  │ FIFO │ LRU  │ LFU  │ NUR  │ SCR  │
    │Optimal│First-In│Least │Least │Not   │Second│
    │Replace│First-│Recently│Frequently│Used │Chance│
    │ment  │ Out  │ Used │ Used │Recently│Replace│
    └──────┴──────┴──────┴──────┴──────┴──────┘
     향후   메모리   페이지  페이지  참조/   큐구조
     가장   적재 순  참조 시 참조 횟 수정   참조 
     사용   서 기반  간 기반 수 기반 비트   사용
     되지        지 교체        사용
     않을
     페이
     지 교체
```

---

## 알고리즘 상세

| 알고리즘 | 설명 | 기준 |
|:---------|:-----|:-----|
| **FIFO (First In First Out)** | Time Stamp 방식, 선입선출 방식 | - |
| **OPT (Optimal)** | 가장 오랫동안 사용하지 않을 페이지 교체 | **미래 기준** |
| **LRU (Least Recently Used)** | 가장 오랫동안 사용되지 않은 페이지 교체 | **현재 기준** |
| **LFU (Least Frequently Used)** | 가장 참조횟수가 가장 적은 페이지 교체 | **현재 기준** |
| **NUR (Not Used Recently)** | 최근에 사용하지 않은 페이지를 2개 비트(참조, 변형) 이용 교체 | **현재 기준** |
| **Second Chance** | FIFO 페이지 교체 보완 기법 | - |
| **MFU (Most Frequently Used)** | 참조 횟수가 가장 많은 페이지 교체 | - |
| **무작위 교체** | 임의 선택 | - |

---

## 연계 토픽

- [Belady's Anomaly (FIFO 이상현상)](/docs/caos/04-virtual-memory/beladys-anomaly)
- [지역성](/docs/caos/04-virtual-memory/locality)
- [스레싱](/docs/caos/04-virtual-memory/thrashing)

---

## 학습 체크리스트

- [ ] 페이지 폴트 개념
- [ ] 각 알고리즘 동작 방식
- [ ] 미래/현재 기준 구분
- [ ] LRU vs LFU 차이

---

## 참고자료

- 정보관리기술사 컴퓨터구조/OS 학습자료

