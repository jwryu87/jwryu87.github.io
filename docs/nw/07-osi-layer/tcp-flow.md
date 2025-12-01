---
layout: default
title: TCP 흐름제어
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 11
---

# TCP 흐름제어
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`Stop and Wait` `Sliding Window`

---

## 정의/개념

송신측과 수신 측의 데이터 속도 차이로 인한 데이터 손실 방지 위해, **송신 측 데이터 속도 통제 기법**

---

## 흐름제어 방식

### Stop-and-Wait 방식

| 구분 | 설명 |
|:-----|:-----|
| **설명** | 전송 측 1개의 세그먼트 전송<br>수신 측 1개의 세그먼트 수신 확인 후 ACK 전송<br>데이터 수신 완료 시까지 1, 2 번 과정 반복 |
| **동작절차** | 1. 전송 측 1개의 세그먼트 전송<br>2. 수신 측 1개의 세그먼트 수신 확인 후 ACK 전송<br>3. 데이터 수신 완료 시까지 1, 2 번 과정 반복 |

### Sliding Window 방식

| 구분 | 설명 |
|:-----|:-----|
| **윈도우 기반 방식 (Sliding Windows)** | 전송 및 ACK 수신 / 전송 및 ACK 미 수신 / 전송가능 데이터 / 닫힘 (Close) |
| **동작절차** | 1. 송신 윈도우크기 만큼 세그멘트 전송<br>2. Ack 수신 후 닫힘 동작 수행<br>3. 닫힘 동작 수행 후 윈도우크기 만큼 열린 동작 수행 |

{: .note }
> 흐름제어를 수행하는 중에도 네트워크가 혼잡한 경우 세그먼트의 손실이 발생할 수 있으므로 윈도우 사이즈를 통한 흐름제어와 혼잡제어를 동시 수행

---

## 연계 토픽

- [TCP](/docs/nw/07-osi-layer/tcp)
- [TCP 혼잡제어](/docs/nw/07-osi-layer/tcp-congestion)

---

## 학습 체크리스트

- [ ] 흐름제어 개념 이해
- [ ] Stop-and-Wait vs Sliding Window 비교
- [ ] 윈도우 기반 동작 원리 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


