---
layout: default
title: SCTP
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 13
---

# SCTP (Stream Control Transmission Protocol)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`멀티호밍` `멀티 스트리밍` `고 신뢰성` `혼잡/흐름제어` `경로 선정 및 감시`

---

## 정의/개념

TCP의 연결형 및 신뢰성의 특성과 UDP의 메시지 지향 특성을 조합한 **멀티 스트리밍과 멀티 호밍을 제공하는 프로토콜**

---

## 프로토콜 구조

| 구성요소 | 설명 |
|:---------|:-----|
| **SCTP User Application** | SCTP 사용자 애플리케이션 |
| **API's** | 응용 프로그램 인터페이스 |
| **SCTP Transport Service** | SCTP 전송 서비스 |
| **IP Network Service** | IP 네트워크 서비스 |

---

## 패킷 구조

| 필드 | 설명 |
|:-----|:-----|
| **Source port** | 송신자 포트번호 (16 bits) |
| **Destination port** | 수신자 포트번호 (16 bits) |
| **Verification tag** | 검증 태그 (32 bits) |
| **Checksum** | 전체 패킷에 대한 Checksum (32 bits) 정보가 포함 |
| **Chunk-1 ~ Chunk-n** | 하나의 SCTP 패킷은 여러 개의 데이터 및 제어 chunks를 포함할 수 있음 |

### Chunk 구조

| 필드 | 설명 |
|:-----|:-----|
| **Type** | Chunk 유형 |
| **Flag** | 플래그 |
| **Length** | 길이 |
| **Stream ID** | 스트림 식별자 |
| **SSN** | 스트림 순서 번호 |
| **Protocol ID** | 프로토콜 식별자 |
| **User data** | 사용자 데이터 |

{: .note }
> SCTP는 응용계층과 네트워크 계층 사이에 위치하며, SCTP peers 간에 응용 데이터를 API로 전달받아 IP망을 통해 전송하는 기능 수행
> SCTP 패킷의 헤더에는 송신자 포트번호(16 bits), 수신자 포트번호 (16 bits), verification tag (32 bits) 및 전체 패킷에 대한 Checksum (32 bits) 정보가 포함
> 하나의 SCTP 패킷은 여러 개의 데이터 및 제어 chunks를 포함할 수 있음

---

## 연계 토픽

- [TCP](/docs/nw/07-osi-layer/tcp)
- [UDP](/docs/nw/07-osi-layer/tcp-udp)

---

## 학습 체크리스트

- [ ] SCTP 개념 및 특성 이해
- [ ] 멀티호밍/멀티스트리밍 개념 파악
- [ ] 패킷 구조 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


