---
layout: default
title: DDoS 공격
parent: DDoS
grand_parent: 보안
nav_order: 2
---

# DDoS, DRDoS 공격
{: .fs-8 }

13.2 DDoS
{: .label .label-red }

---

## 핵심 키워드

### DDoS
`SYN Flood` `UDP Flood` `ICMP Flood` `HTTP GET Flood` `좀비PC` `봇넷`

### DRDoS
`SYN+ACK` `NTP` `DNS` `CLDAP` `반사서버` `IP Spoofing`

---

## 정의/개념

### DDoS (Distributed Denial of Service)

**좀비, Agent, 자원 고갈**, 서비스 거부 공격 기법

- 대량의 좀비(zombie) 감염시켜 에이전트를 통해 목표시스템의 자원을 고갈시켜 서비스 거부 유발 시키는 가용성 공격 기법

### DRDoS (Distributed Reflection DoS)

**Agent 설치 없이**, 네트워크 통신 프로토콜 구조 취약성 이용, **정상적 시스템 Agent 활용**, 서비스 거부 공격 기법

- 정상적인 서비스 요청을 위조된 타겟(target)에게 집중시키는 증폭 네트워크 기반의 가용성 공격 기법

---

## 개념 비교

### DDoS 공격과 DRDoS 공격 개념 비교

| 구분 | DDoS | DRDoS |
|:-----|:-----|:------|
| **공격 개념** | 대량의 좀비(zombie) 감염시켜 에이전트를 통해 목표시스템의 자원을 고갈시켜 서비스 거부 유발 시키는 가용성 공격 기법 | 정상적인 서비스 요청을 위조된 타겟(target)에게 집중시키는 증폭 네트워크 기반의 가용성 공격 기법 |

### 개념도

```
┌─────────────────────────────────────────────────────────────────────────┐
│            DDoS                          │           DRDoS              │
│                                          │                              │
│     C&C                                  │                              │
│      │                                   │                              │
│    좀비PC  ────┐      PPS증가            │         반사        증폭      │
│    좀비PC  ────┼─────▶ 공격대상          │  공격자 ───▶ Reflection ───▶ │
│    좀비PC  ────┤                         │         NTP  DNS  SNMP      │
│    좀비PC  ────┘        Request          │                  Amplification│
│      │                  Response         │              │               │
│   유포서버                               │         <경유지 서버>        │
│                                          │              │               │
│                                          │              ▼               │
│                                          │           공격대상           │
└─────────────────────────────────────────────────────────────────────────┘
```

- DDoS는 좀비 에이전트를 이용하고, DRDoS는 증폭 네트워크를 악용 공격

---

## 기법 비교

### DDoS 공격과 DRDoS 공격 절차와 기법 비교

| 구분 | DDoS | DRDoS |
|:-----|:-----|:------|
| **공격 절차 (좀비PC)** | 1) 명령제어서버 및 유포 서버 취약점 공격 확보<br>2) 악성코드 유포하여 에이전트(Agent) 설치<br>3) 악성 명령어 좀비PC로 전달 수행<br>4) 타겟 서버 서비스 마비 | 1) 소스 아이피(source-ip)를 타겟 아이피(target-ip)로 변조<br>2) 반사 서버(Reflection Server)로 대량 Request 발송<br>3) 타겟 서버로 증폭(Amplification) 되어 패킷 전송<br>4) 타겟 서버 서비스 마비 |
| **공격 기법** | - Flooding(UDP, ICMP, SYN, DNS, GET)<br>- Slow HTTP Header(Slowloris), Slow HTTP POST(RUDY) | - DNS 증폭, NTP(Network Time Protocol) 증폭<br>- SNMP(Simple Network Management Protocol) 증폭, CHARGEN 증폭 |
| **대응 기법** | - 불필요한 서비스 사전차단, 임계치(Clipping Level)<br>- 타임아웃설정, ACL(Access Control List) 정책<br>- BPS(Byte per second), PPS(Packet Per Second), CPS(Character Per Second) 추적 확인 조치<br>- 좀비PC IP 확보 차단, 사이버대피소 | - 아이피 스푸핑(IP Spoofing) 탐지, 타겟 서버 IP 및 포트 필터링(Port Filtering), 반사 서버 무차별 이용 차단<br>- ISP 필터링(Egress 필터링), 반사(Reflection Server) 보호<br>- 공격 플랫폼 통제 제한 |

---

## 공격 유형별 비교

| 공격 유형 | 프로토콜 | 특징 |
|:---------|:---------|:-----|
| **SYN Flood** | TCP | 3-way handshake 악용, 서버 자원 고갈 |
| **UDP Flood** | UDP | 대량 UDP 패킷으로 대역폭 고갈 |
| **ICMP Flood** | ICMP | Ping 대량 발송으로 대역폭 고갈 |
| **HTTP GET Flood** | HTTP | 웹서버 자원 고갈 |
| **DNS Amplification** | DNS | DNS 응답 증폭 공격 |
| **NTP Amplification** | NTP | NTP monlist 증폭 공격 |

---

## 대응 방안

| 방안 | 설명 |
|:-----|:-----|
| **대역폭 확보** | 공격 트래픽 수용 가능한 대역폭 확보 |
| **Rate Limiting** | 요청 빈도 제한 |
| **Blackholing** | 공격 트래픽 차단 |
| **Scrubbing Center** | 트래픽 정화 센터 활용 |
| **CDN 활용** | 분산 처리로 부하 분산 |

---

## 연계 토픽

- [DRDoS](/docs/sec/13-ddos/drdos)
- [랜섬 디도스](/docs/sec/13-ddos/ransom-ddos)
- [IDS/IPS](/docs/sec/19-detection/ids-ips)
- [방화벽](/docs/sec/16-network-security/)

---

## 학습 체크리스트

- [ ] DDoS와 DRDoS 개념 차이 이해
- [ ] 공격 절차 및 기법 비교 파악
- [ ] 대응 기법 차이점 이해

---

## 참고자료

- 정보관리기술사 보안 학습자료
- 최근 미라이 변종, 스마트카 및 스마트 팩토리 등의 IoT기기 환경에서 DRDoS 공격 급증 따라 대응이 필요


