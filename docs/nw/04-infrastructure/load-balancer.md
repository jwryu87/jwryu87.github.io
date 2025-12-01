---
layout: default
title: 로드밸런서
parent: 4. 네트워크 구축
grand_parent: NW (네트워크)
nav_order: 4
---

# 로드밸런서 (Load Balancer)
{: .fs-8 }

4.1 네트워크 구축
{: .label .label-purple }

---

## 핵심 키워드

`L4 로드밸런서` `L7 로드밸런서` `Round Robin` `Hashing` `Scale-up` `Scale-out`

---

## 정의/개념

클라이언트와 서버 사이에 위치하여 서버 부하가 집중되지 않도록 **부하 분산 기술**

---

## L4 vs L7 로드밸런서 비교

| 구분 | L4 로드밸런서 | L7 로드밸런서 |
|:-----|:-------------|:-------------|
| **개념** | 네트워크 계층(IP, IPX)이나 트랜스포트 계층 (TCP, UDP)의 정보를 바탕으로 로드 분산 | 애플리케이션 계층(HTTP, FTP, SMTP)에서 HTTP 헤더, 쿠키 등과 같은 사용자 요청을 기준으로 트래픽 분산 |
| **Layer** | Layer 4 (Transport Layer) | Layer 7 (Application Layer) |
| **장점** | 패킷 레벨 부하 분산으로 속도가 빠름<br>복호화 불필요하고 가격이 저렴 | 상위계층에서 상세한 라우팅 가능<br>캐싱 기능, 비정상 트래픽 필터링 가능 |
| **단점** | IP가 변경되는 경우 연속적인 서비스 불가<br>패킷 내용 기반 라우팅 불가 | 패킷 내용의 복호화를 위한 비용 발생<br>인증서 공유로 보안상의 위험 존재 |

{: .note }
> 동작하는 네트워크 계층에 따라 L4 로드밸런서와 L7 로드밸런서로 구분

---

## 기술요소

### 알고리즘

| 기술요소 | 설명 |
|:---------|:-----|
| **Round Robin** | 클라이언트의 요청을 단순하게 순서대로 순환하여 처리<br>응답시간이 빠르고 구성이 단순한 장점 |
| **Hashing** | 클라이언트의 Source IP, Port 정보를 바탕으로 hash한 결과 값을 토대로 로드밸런싱을 수행<br>동일한 클라이언트 요청을 동일한 back-end 서버에서 처리하고자 할 때 주로 사용 |
| **Least Response** | 가장 빠른 Response Time을 제공하는 웹서버로 로드밸런싱 |
| **Least Connection** | back-end 서버 중 Active되어 있는 연결 수를 계산하여 가장 적은 커넥션 수를 보유한 서버로 로드밸런싱<br>일반적인 웹 서비스 환경에서 최적의 성능을 제공 |

### 확장방법

| 기술요소 | 설명 |
|:---------|:-----|
| **Scale-up** | 서버 자체의 성능을 확장 |
| **Scale-out** | 기존 서버와 동일하거나 낮은 성능의 서버를 두 대 이상 증설하여 운영 |

---

## 연계 토픽

- [리버스 프록시](/docs/nw/04-infrastructure/reverse-proxy)
- [고가용성(HA)](/docs/sw/04-architecture/high-availability)

---

## 학습 체크리스트

- [ ] 로드밸런서 개념 이해
- [ ] L4 vs L7 로드밸런서 차이 구분
- [ ] 알고리즘(RR, Hashing, Least Response/Connection) 특징 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


