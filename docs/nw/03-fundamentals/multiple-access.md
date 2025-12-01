---
layout: default
title: 다원접속·다중접속
parent: 3. 네트워크 기본
grand_parent: NW (네트워크)
nav_order: 5
---

# 다원접속 (Multiple Access), 다중접속
{: .fs-8 }

3.1 네트워크 기본
{: .label .label-purple }

---

## 핵심 키워드

`FDMA` `TDMA` `SDMA` `CDMA` `Random Access`

---

## 정의/개념

한정된 전송 자원을 다수 노드들이 공평 유지 위해, 시간 및 주파수 등을 여러 사용자가 공동으로 사용하는 전송 기술

---

## 다원접속 유형

### 고정할당 방식 (Fixed)

| 방식 | 설명 |
|:-----|:-----|
| **FDMA** | Frequency Division Multiple Access<br>각각의 사용자 신호를 서로 다른 주파수에 실어 보내는 방식<br>예) 이동통신 AMPS 방식 등 |
| **TDMA** | Time Division Multiple Access<br>각각의 사용자 신호를 서로 다른 시간슬롯에 할당하여 실어 보내는 방식 |
| **SDMA** | Spatial Division Multiple Access<br>서로 분리된 다른 공간을 다른 사용자에게 할당하는 방식<br>SDMA 방식 자체 만으로 독립 사용되지 않고 FDMA, TDMA, CDMA방식들과 연계 사용 |
| **CDMA** | Code Division Multiple Access<br>각각의 사용자 신호를 서로 다른 코드를 곱하여 (직교성 보장) 달리 구분<br>예) 이동통신 cdmaOne, WCDMA 등 더 욱 효율적으로 이용하는 기술 |

### 동적할당 방식 (Dynamic)

| 방식 | 설명 |
|:-----|:-----|
| **Random Access** | ALOHA: 역사적 최초 pure aloha, slotted aloha, controlled aloha 등<br>Carrier Sensing 방식: Ethernet (CSMA/CD) 등 |
| **비경쟁방식** | 예약방식: 토큰 버스, 토큰 링 등의 토큰 방식<br>비예약방식: 폴링 방식 |
| **하이브리드** | 경쟁, 비경쟁 방식의 합성한 방식 |

---

## 연계 토픽

- [다중화](/docs/nw/03-fundamentals/multiplexing)
- [접근제어](/docs/nw/03-fundamentals/access-control)

---

## 학습 체크리스트

- [ ] FDMA, TDMA, SDMA, CDMA 개념 이해
- [ ] 고정할당 vs 동적할당 방식 차이 구분
- [ ] Random Access 방식의 종류 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


