---
layout: default
title: 네트워크 슬라이싱
parent: 6. 네트워크 관리
grand_parent: NW (네트워크)
nav_order: 1
---

# 네트워크 슬라이싱 (Network Slicing)
{: .fs-8 }

6.1 네트워크 관리
{: .label .label-purple }

---

## 핵심 키워드

`Application` `Presentation` `Session` `Transport` `Network` `Data Link` `Physical`

---

## 정의/개념

물리적으로 하나의 네트워크를 논리적으로 분리하여, 서로 다른 특성을 갖는 다양한 서비스에 특화된 전용 네트워크를 제공하는 **5G 네트워크 핵심기술**

---

## 개념도

| 네트워크 슬라이싱 전 | 네트워크 슬라이싱 후 |
|:-------------------|:-------------------|
| 4G망: 폰, 통신서비스, 통신산업<br>통신 서비스(음성, 문자, 인터넷) | Mobile Broadband: 하나의 물리적 코어 (논리적 분리) - 통신 산업<br>UHD, 홀로그램 통신<br>센서 네트워크(물류, 농업): 공장자동화, Smart-Grid - 물류, 농업 기술<br>Massive IoT |
| 4G망 | Mission-critical IoT - 자동차 |

---

## 핵심기술

| 기술 영역 | 세부 기술 | 설명 |
|:---------|:---------|:-----|
| **SDN** | Application | Network OS 상에서 사용자 서비스를 지원하는 프로그램 |
| | Network OS | 전체 망에 대한 Global View 를 갖고 전체 망을 제어<br>Openflow Controller 는 Openflow protocol 을 통해 Data plane 에 있는 네트워크 장비의 Flow Table 제어 |
| | Data Plane | 단순 패킷 포워딩, 스위칭 기능만 구현<br>기존 스위치 또는 Layer2(스위칭), Layer3(라우팅) 기능 지원 스위치에 OpenFlow 의 기능을 추가 |
| **NFV** | NFVI | 컴퓨팅, 저장소, 네트워크 기능을 지원하는 물리적 하드웨어 지원, 가상화 지원 기능 및 VNF 실행을 지원하는 기능 제공 |
| | NFVs | 여러 응용 프로그램을 지원하기 위한 SW로 개발된 네트워크 기능들의 집합 |

---

## 연계 토픽

- [SDN](/docs/nw/06-management/sdn)
- [NFV](/docs/nw/06-management/nfv)

---

## 학습 체크리스트

- [ ] 네트워크 슬라이싱 개념 이해
- [ ] SDN, NFV와의 관계 파악
- [ ] 5G에서의 활용 사례 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


