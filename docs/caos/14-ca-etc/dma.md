---
layout: default
title: DMA
parent: 14. CA 기타
grand_parent: CAOS (컴퓨터구조/OS)
nav_order: 2
---

# DMA (Direct Memory Access)
{: .fs-8 }

14.1 기타
{: .label .label-yellow }

---

## 핵심 키워드

`CPU 오프로드` `고속 데이터 전송` `DMA 컨트롤러`

---

## 정의/개념

**DMA(Direct Memory Access)**는 CPU의 개입 없이 주변장치와 메모리 간에 **직접 데이터를 전송**하는 방식입니다.

---

## DMA vs CPU 제어 전송

| 구분 | CPU 제어 전송 | DMA 전송 |
|:-----|:-------------|:---------|
| **CPU 부하** | 높음 | 낮음 |
| **전송 속도** | 느림 | 빠름 |
| **효율성** | 낮음 | 높음 |

---

## DMA 전송 모드

| 모드 | 설명 |
|:-----|:-----|
| **버스트 모드** | 전체 블록 연속 전송 |
| **사이클 스틸링** | 한 워드씩 전송 |
| **투명 모드** | CPU 미사용 시 전송 |

---

## 연계 토픽

- [인터럽트](/docs/caos/10-interrupt/interrupt)
- [메모리 인터리빙](/docs/caos/14-ca-etc/memory-interleaving)

---

## 학습 체크리스트

- [ ] DMA 개념 및 장점
- [ ] 전송 모드 3가지

---

## 참고자료

- 정보관리기술사 컴퓨터구조/OS 학습자료

