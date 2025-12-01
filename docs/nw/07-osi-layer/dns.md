---
layout: default
title: DNS
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 23
---

# DNS (Domain Name System)
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`도메인 네임 공간` `리소스 레코드` `네임서버` `리졸버`

---

## 정의/개념

기억하기 쉬운 문자 형태의 도메인을 컴퓨터가 처리하기 용이한 **숫자 형태의 IP 주소로 변경하는 시스템**

---

## 구성요소

| 요소 | 설명 | 특징 |
|:-----|:-----|:-----|
| **도메인 네임 공간 (Domain Name Space)** | 도메인 네임을 중복되지 않게 네임을 생성하여 사용하도록 정의된 도메인 네임 구성 체계 | 계층적(트리) 구조<br>유연성, 확장성 |
| **리소스 레코드 (Resource Record)** | 유일성을 갖는 도메인이름에 설정할 수 있는 다양한 데이터 유형을 제공, 키 인덱스(Index) 역할 | 유일성 제공<br>다양한 데이터 타입 |
| **네임서버 (Name Server)** | 도메인 네임에 대한 데이터 질의가 있을 때, 보유하고 있는 도메인의 데이터를 조회하여 응답을 수행 | 도메인 이름과<br>레코드 데이터 저장 |
| **리졸버 (Resolver)** | 네임 서버에 원하는 호스트에 대한 정보를 조회(질의) 및 추출하는 DNS 클라이언트용 프로그램 | 레코드 데이터 조회<br>캐시 네임 서버 |

{: .note }
> 도메인 네임별 레코드 데이터를 준 파일 포맷으로 표현, 분산되어 있는 네임서버 DB에 저장

---

## 동작절차

| NO. | 동작 |
|:----|:-----|
| **①** | 웹브라우저에서Local DNS로 www.naver.com에대한 IP주소질의 |
| **②** | Local DNS: DNS cache에 해당 도메인에 대한 정보가 캐시에 존재하면클라이언트에 응답<br>없으면 root DNS에 www.naver.com에 대한 정보를 질의 |
| **③** | root DNS서버로부터 "com 도메인"을 관리하는 TLD(Top-Level Domain)이름서버 정보 응답 |
| **④** | Local DNS는 TLD에 www.naver.com질의 |
| **⑤** | TLD에서 "naver.com" 을 관리하는 DNS 정보를 전달 |
| **⑥** | Local DNS서 naver.com DNS에 www.naver.com 호스트네임에 대한 IP 주소를 질의 |
| **⑦** | naver.com DNS는 Local DNS서버에게 IP주소(222.122.195.6)를 응답 |
| **⑧** | Local DNS는 www.naver.com에 대한 IP주소를 캐싱하고 IP주소정보를 전달 |

{: .highlight }
> 최상위 도메인(Top-level domain, TLD)은 인터넷 도메인 네임의 가장 마지막 부분을 지칭
> DNS 는 악의적인 해커에 의해 정보가 쉽게 위·변조될 취약점과 서비스 거부(DoS)공격에 대한 취약점 존재

---

## 연계 토픽

- [DNSSEC](/docs/sec/16-network-security/dnssec)
- [IPv4·IPv6](/docs/nw/07-osi-layer/ipv4-ipv6)

---

## 학습 체크리스트

- [ ] DNS 개념 및 구성요소 이해
- [ ] DNS 동작 절차 파악
- [ ] DNS 보안 취약점 인지

---

## 참고자료

- 정보관리기술사 NW 학습자료


