---
layout: default
title: Traffic Shaping·Policing
parent: 5. 네트워크 품질
grand_parent: NW (네트워크)
nav_order: 2
---

# Traffic Shaping, Traffic Policing
{: .fs-8 }

5.1 네트워크 품질
{: .label .label-purple }

---

## 핵심 키워드

### Traffic Shaping
`CBS` `CIR` `EBS` `Leaky Bucket` `Token Bucket`

### Traffic Policing
`Meter` `Drop` `Mark` `RED` `WRED` `Tail Drop`

---

## 정의/개념

- **Traffic Shaping**: 네트워크 성능 최적화 위해, 네트워크 내부 유입 트래픽 양과 유출 트래픽 속도를 버퍼를 통해 조절 QoS 기술
- **Traffic Policing**: 네트워크 서비스 보장 위해, 미리 정의된 기준 초과 트래픽은 버림으로써 트래픽 대역폭 제어 QoS 기술

---

## Traffic Shaping vs Traffic Policing 비교

| 비교 | Traffic Shaping | Traffic Policing |
|:-----|:----------------|:-----------------|
| **동작방식** | 트래픽이 대역폭 이상 발생시 버퍼에 패킷을 저장후 대역폭 이하 발생시 전송 | 트래픽이 정해진 대역폭 이 발생하면 Drop 처리 하여 대역폭 제어 |
| **단점** | 버퍼 추가 지연 발생, 메모리를 많이 점유<br>구현이 어려움, 실시간 응용 부적합 | TCP 기반 흐름에서 패킷 손실이 발생<br>전체 출력 속도 저하 |
| **알고리즘** | Leaky Bucket: 용량제어<br>Token Bucket: 속도제어<br>Hybrid Bucket: 용량제어+속도제어 | RED(Random Early Detection): 혼잡상황 사전 감지 Drop<br>WRED(Weighted Random Early Detection): 패킷의 가중치에 따라 Drop<br>Tail Drop: 버퍼 임계치 초과시 모두 Drop |
| **구성요소** | CBS(Committed Burst Size): 허용 버스트 크기<br>CIR(Committed Information Rate): 허용 정보율<br>EBS(Excess Burst Size): 초과 버스트 크기 | Meter: 수신되는 패킷 유입률 측정<br>Drop: 대역폭 이상시 패킷 제거<br>Mark: 대역폭 이하시 마킹후 포워딩 |
| **적용** | 유입된 Packet을 잠시 저장함<br>주로 Outbound에 적용 | Inbound / Outbound 모두 적용 가능<br>주로 Inbound에 적용 |
| **장점** | 초과 패킷 버퍼링 패킷 삭제 가능성 낮음<br>TCP 응용에 적합 | 구현이 용이함, 실시간 응용에 적합<br>패킷 Drop을 통한 Queue 지연 방지 |

{: .note }
> Traffic Shaping이 버퍼 관리에 메모리를 많이 점유하지만 안정적인 네트워크 서비스 지원이 가능하며 Traffic Policing은 구현이 용이하며 지연을 방지 가능

---

## 연계 토픽

- [QoS](/docs/nw/05-qos/qos)
- [DiffServ·IntServ](/docs/nw/05-qos/diffserv-intserv)

---

## 학습 체크리스트

- [ ] Traffic Shaping과 Policing 차이 이해
- [ ] Leaky Bucket, Token Bucket 알고리즘 파악
- [ ] RED, WRED, Tail Drop 특징 구분

---

## 참고자료

- 정보관리기술사 NW 학습자료


