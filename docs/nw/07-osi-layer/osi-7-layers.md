---
layout: default
title: OSI 7 Layers
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 1
---

# OSI 7 Layers (ISO/IEC 7498)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-blue }

---

## 핵심 키워드

`Application` `Presentation` `Session` `Transport` `Network` `Data Link` `Physical`

---

## 정의/개념

국제표준기구(ISO)에서 표준화된 네트워크 구조를 제시한 **기본 모델**

{: .note }
> OSI 7 Layer는 각 계층마다 특정한 서비스를 제공하고, 이를 위한 각각 프로토콜이 존재함
> 캡슐화 – 헤더 정보 등을 붙이는 과정 (송신측)
> 역캡슐화 – 헤더 뗏 맞는 과정 (수신측)

---

## 계층 상세 설명

| 계층 | 상세설명 | 프로토콜 |
|:-----|:---------|:---------|
| **7 계층<br>Application** | 사용자가 네트워크에 접근할 수 있도록 해주는 계층<br>사용자 인터페이스, 전자우편, 데이터베이스 관리서비스 | HTTP, SMTP, SNMP, FTP, Telnet, SSH&SCP, NFS, RTSP, NTP |
| **6 계층<br>Presentation** | 운영체제의 한 부분으로 I/O 데이터를 표현 형태로 변환<br>번역을 수행하여 두 장치가 일관되고 이해할 수 있음 | JPEG, MPEG, XDR, SMB, AFP |
| **5 계층<br>Session** | 통신세션을 구성하는 계층으로 포트연결 확인<br>통신장치간의 상호작용을 설정하고 유지하며 동기화 | TLS, SSH, RPC, NetBIOS, AppleTalk |
| **4 계층<br>Transport** | 전체 메시지를 발신지 대 목적지간 제어와 에러 관리<br>패킷들의 전송 유효확인, 실패한 패킷은 재전송하여 신뢰성 있는 통신 보장. 머리말에는 세그먼트가 포함 | TCP, UDP, RTP, SCTP, SPX |
| **3 계층<br>Network** | 다중 네트워크 링크에서 패킷을 목적지로 전달<br>패킷이 시작시점에서 최종 목적지까지 성공적으로 전달되도록 관리 | IP, ICMP, IGMP, X.25, CLNP, ARP, RARP, BGP, OSPF, RIP, IPX, DDP |
| **2 계층<br>Data Link** | 오류 없이 한 장치에서 다른 장치로 프레임을 전달<br>스위칭테이블을 참조하여 입력되는 패킷의MAC 주소를 보고 해당 포트로 패킷 전송 | PPP, HDLC, Ethernet, TokenRing, ISDN, FDDI |
| **1 계층<br>Physical** | 물리적 매체를 통해 비트(Bit)흐름 전송<br>장치간의 물리적 접속을 제어하기 위한 기능 제공 | RS-232C, 광섬유, 동축케이블, ISDN, DSL |

---

## 연계 토픽

- [캡슐화·역캡슐화](/docs/nw/07-osi-layer/encapsulation)
- [TCP](/docs/nw/07-osi-layer/tcp)

---

## 학습 체크리스트

- [ ] OSI 7계층 개념 및 역할 이해
- [ ] 각 계층별 프로토콜 구분
- [ ] 캡슐화/역캡슐화 과정 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


