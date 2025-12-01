---
layout: default
title: 캡슐화·역캡슐화
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 2
---

# 네트워크 캡슐화, 역캡슐화
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-blue }

---

## 핵심 키워드

### 캡슐화
`Payload Header 추가`

### 역캡슐화
`전송 패킷` `Header 제거`

---

## 정의/개념

- **캡슐화**: Payload Header 추가, PDU 전송 패킷 생성 과정
- **역캡슐화**: 전송 패킷, Header 제거 Payload 복원 과정

---

## 구성도

```
캡슐화(Encapsulation)                    역캡슐화(Decapsulation)
        ↓                                        ↑
┌─────────────────┐                    ┌─────────────────┐
│    Application  │ App Data           │    Application  │
├─────────────────┤                    ├─────────────────┤
│   Presentation  │                    │   Presentation  │
├─────────────────┤                    ├─────────────────┤
│     Session     │                    │     Session     │
├─────────────────┤                    ├─────────────────┤
│    Transport    │ Segments/Datagram  │    Transport    │
├─────────────────┤                    ├─────────────────┤
│     Network     │ Packets            │     Network     │
├─────────────────┤                    ├─────────────────┤
│    Data Link    │ Frames             │    Data Link    │
├─────────────────┤                    ├─────────────────┤
│    Physical     │ Bits               │    Physical     │
└─────────────────┘                    └─────────────────┘
     Transmit                              Receive
```

{: .note }
> 데이터링크 계층에서는 오류 검출을 위하여 FCS Trailer를 추가

---

## 메커니즘

| 메커니즘 | 설명 |
|:---------|:-----|
| **캡슐화 과정** | 상위 계층의 데이터와 헤더를 모두 하위 계층의 데이터 부분에 포함시키고 해당 계층의 헤더를 앞에 삽입한다. IP 헤더와 데이터는 하위 이더넷 프레임의 데이터 부분에 포함되고 이더넷 헤더를 붙이는 캡슐화 과정을 통해 하나의 완성된 데이터가 전송 |
| **FCS로 에러 체크** | FCS(Frame Check Sequence)는 데이터가 오류 여부를 확인하기 위한 필드<br>데이터 송신 시 헤더와 데이터에 대한 일정한 계산(Checksum, CRC)을 실시하여 FCS에 추가하며, 이 FCS가 데이터 링크에 대한 오류 제어의 역할을 담당 |
| **역캡슐화 과정** | 반대로 수신지에서는 역캡슐화 과정을 통해 각 계층의 헤더를 제거하고 데이터 부분을 상위 계층으로 전달함 |

{: .highlight }
> 데이터링크 계층에서는 오류 검출을 위하여 FCS Trailer를 추가

---

## 연계 토픽

- [OSI 7 Layers](/docs/nw/07-osi-layer/osi-7-layers)
- [TCP 헤더](/docs/nw/07-osi-layer/tcp-header)

---

## 학습 체크리스트

- [ ] 캡슐화/역캡슐화 개념 이해
- [ ] 각 계층별 PDU(Segment, Packet, Frame, Bit) 구분
- [ ] FCS를 통한 오류 검출 원리 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


