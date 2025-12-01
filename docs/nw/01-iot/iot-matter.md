---
layout: default
title: IoT Matter
parent: 1. IoT
grand_parent: NW (네트워크)
nav_order: 1
---

# IoT Matter
{: .fs-8 }

1.1 IoT
{: .label .label-purple }

---

## 핵심 키워드

`스마트홈` `IP 기반 IoT 프로토콜` `Wi-Fi` `Thread` `CSA`

---

## 정의/개념

CSA(Connectivity Standards Alliance) 단체가 개발한 IoT 기기간 연결과 연동을 제공하는 **IP 기반 응용계층 개방형 IoT 통합 표준 프로토콜**

---

## 프로토콜 스택

| 계층 | 기술요소 | 설명 |
|:-----|:---------|:-----|
| **Application** | Matter Application | IP기반으로 통신, 어플리케이션 계층에서 서비스 처리하여, 다양한 스마트홈 디바이스 연동문제를 해결 |
| **Transport** | TCP/IP | 연결지향성을 통해 신뢰성 있는 전송계층 프로토콜, 매터의 안전성 제공 |
| | UDP | 대량의 데이터 전송 가능한 비연결지향 통신 프로토콜 |
| **Network** | IPv6 | IoT 기기별 IP주소제공, 확장헤더를 가지는 128bit 인터넷 주소체계 |
| **Radio** | Wi-Fi (802.11) | Wi-Fi 6 기반, 댁내 밀집된 사용자 환경에서 기기간 영향 최소화<br>동영상 등 고속 통신이 필요한 디바이스를 위해 사용함 |
| | Thread (802.15.4) | 메쉬(Mesh) 지원으로 SPOF 방지, 최대 64개 라우터 메쉬 구성 가능<br>IPv6을 사용하며, 배터리로 동작하는 저전력 디바이스를 위해 사용 |
| | BLE | 스마트홈 플랫폼에 디바이스 provisioning 용도로 사용 |
| **IoT Devices** | Matter-enabled Products | Matter 지원 IoT 제품들 |

---

## 연계 토픽

- [네트워크 캡슐화](/docs/nw/07-osi-layer/encapsulation)
- [IPv4·IPv6](/docs/nw/07-osi-layer/ipv4-ipv6)

---

## 학습 체크리스트

- [ ] Matter 프로토콜 개념 이해
- [ ] 프로토콜 스택 구조 파악
- [ ] Wi-Fi, Thread, BLE 각각의 용도 구분

---

## 참고자료

- 정보관리기술사 NW 학습자료


