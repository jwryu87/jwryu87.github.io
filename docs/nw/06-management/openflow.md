---
layout: default
title: Openflow
parent: 6. 네트워크 관리
grand_parent: NW (네트워크)
nav_order: 5
---

# Openflow
{: .fs-8 }

6.1 네트워크 관리
{: .label .label-yellow }

---

## 핵심 키워드

`OpenFlow Controller` `Switch` `Flow Table` `Group Table` `OpenFlow Channel` `Pipelining`

---

## 정의/개념

네트워크 장비의 패킷 포워딩 기능과 컨트롤러 기능을 표준 인터페이스로 분리하여 네트워크 개방성을 제공하는 기술로서 **SDN(Software Defined Network) 컨트롤러와 네트워크 장치간의 인터페이스 규격**

---

## 개념도

```
┌─────────────┐     ┌─────────────┐
│ Controller  │     │ Controller  │
└──────┬──────┘     └──────┬──────┘
       │                   │
       └─────────┬─────────┘
                 │ OpenFlow Protocol
                 ▼
┌──────────────────────────────────────────────┐
│              OpenFlow Switch                  │
│  ┌──────────────────────────────────────────┐│
│  │                Datapath                   ││
│  │ ┌────────────┐  ┌────────────┐           ││
│  │ │ OpenFlow   │  │ OpenFlow   │  ┌───────┐││
│  │ │ Channel    │  │ Channel    │  │ Group |||
│  │ └────────────┘  └────────────┘  │ Table |||
│  │      Control Channel            │       |||
│  │ ┌──────┐ ┌──────┐     ┌──────┐ │ Meter |||
│  │ │ Port │ │ Flow │ ... │ Flow │ │ Table |||
│  │ └──────┘ │ Table│     │ Table│ └───────┘││
│  │ ┌──────┐ └──────┘     └──────┘          ││
│  │ │ Port │        Pipeline                 ││
│  │ └──────┘                                 ││
│  └──────────────────────────────────────────┘│
└──────────────────────────────────────────────┘
```

---

## 구성요소

| 구분 | 구성요소 | 설명 |
|:-----|:---------|:-----|
| **Controller** | OpenFlow Controller | OpenFlow Protocol을 통하여 OpenFlow Switch와 상호작용<br>다수의 OpenFlow 논리적 스위치를 제어하는 소프트웨어 |
| **Protocol** | OpenFlow Protocol | OpenFlow Switch와 OpenFlow Controller사이의 통신 규약<br>3개의 메시지 타입 지원<br>① Controller-to-Switch: Controller에 의해 시작, Switch 상태 확인, 제어(전송, 수정, 폐기 등) 처리<br>② Asynchronous: Switch에 의해 시작, 네트워크와 스위치 상태 변경 등을 Controller에 Update<br>③ Symmetric: Switch나 Controller에 의해 시작, 요청없이 전송 |
| | OpenFlow Channel | Controller가 Switch를 관리하기 위하여 사용하는 OpenFlow Control와 OpenFlow Switch 사이의 인터페이스 |
| **Switch** | Flow Table | 다수의 Flow entry로 구성되었으며, 파이프라인(Pipeline)으로 처리<br>Flow entry 구성: match fields(패킷일치), counters(통계), instructions(패킷과 entry 일치시 실행 내용) |
| | Group Table | 다수의 Group entry로 구성<br>Group entry 구성: Group Identifier, Group Type, Counters(패킷처리통계), Action Buckets (실행집합과 변수 등) |

---

## 연계 토픽

- [SDN](/docs/nw/06-management/sdn)
- [NFV](/docs/nw/06-management/nfv)

---

## 학습 체크리스트

- [ ] Openflow 개념 이해
- [ ] Controller, Switch, Protocol 구성요소 파악
- [ ] Flow Table, Group Table 역할 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


