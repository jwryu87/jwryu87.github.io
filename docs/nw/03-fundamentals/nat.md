---
layout: default
title: NAT
parent: 3. 네트워크 기본
grand_parent: NW (네트워크)
nav_order: 6
---

# NAT (Network Address Translation)
{: .fs-8 }

3.1 네트워크 기본
{: .label .label-purple }

---

## 핵심 키워드

`IP Masquerading` `Port Forwarding` `Load Balancing` `사설 IP` `공인 IP`

---

## 정의/개념

IPv4 주소 고갈 문제 해결, 내부 사설 주소, 외부 공인주소 매핑 기술

---

## 구성 유형

| 구성유형 | 설명 |
|:---------|:-----|
| **Static NAT**<br>(정적 NAT) | 내부 IP주소 하나에 외부 IP주소 하나를 할당하는 1:1 방식 변환 수행<br>특정 사설 IP가 지정된 공인 IP로만 사용되도록 매핑<br>1:1 매핑, 해킹 취약 |
| **Dynamic NAT**<br>(동적 NAT) | 내부의 사설 IP가 정해진 공인 IP Pool 내에서 자동으로 매핑<br>N:M 매핑<br>외부 IP가 내부 IP보다 적은 경우 사용 |
| **PAT**<br>(Port Address Translation) | 내부의 사설 IP 여러 개를 공인 IP 1개로 매핑<br>IP주소 뿐 아니라 포트 번호를 포함시켜 내부 호스트 구분<br>1:N 매핑<br>외부 IP가 내부 IP보다 적은 경우 사용 |

---

## 주요 기능

| 주요 기능 | 설명 |
|:---------|:-----|
| **IP Masquerading** | 내부 사설망의 모든 사설IP(호스트)가 대표로 하나의 공인 IP 사용<br>IP계층 상에서 IP주소 변환 기능으로 위장 효과 |
| **Port Forwarding** | 도착 Port 정보로 내부 사설 IP (호스트) 식별<br>내부 사설망의 여러 호스트들이 외부망과 트랜스포트 계층에서 각 별도로 연결 가능 |
| **Load Balancing** | 내부 사설망 내 특정 서버로의 부하 집중 방지 역할<br>각 포트 별로 트래픽을 균형 있게 연결 가능 |

{: .note }
> NAT의 기능 중 기본 역할과 Port Forwarding 기능의 역할에 대한 관계 설명
> NAT에는 IP Masquerading, Port Forwarding, Load Balancing 세가지 주요 기능 존재

---

## 연계 토픽

- [NAT Traversal](/docs/nw/03-fundamentals/nat-traversal)
- [IPv4·IPv6](/docs/nw/07-osi-layer/ipv4-ipv6)

---

## 학습 체크리스트

- [ ] NAT 개념 및 필요성 이해
- [ ] Static NAT, Dynamic NAT, PAT 차이 구분
- [ ] IP Masquerading, Port Forwarding, Load Balancing 기능 이해

---

## 참고자료

- 정보관리기술사 NW 학습자료


