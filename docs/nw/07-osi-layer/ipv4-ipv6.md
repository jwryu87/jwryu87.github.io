---
layout: default
title: IPv4·IPv6
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 14
---

# IPv4, IPv6
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

- IPv4: 32비트, 비순차적 할당, 10진수 표시
- IPv6: 128비트, 순차적할당, 16진수 표시

---

## 정의/개념

- **IPv4**: 32비트 방식을 사용한 현재의 인터넷 주소 체계
- **IPv6**: 현재 사용하고 있는 IPv4의 주소길이(32비트)를 4배 확장하여 IETF가 1996년 표준화한 **128비트 차세대 인터넷 주소 체계**

---

## IPv4 와 IPv6의 헤더 비교

### IPv4 헤더

| 필드 | 크기 |
|:-----|:-----|
| Version | 4bits |
| IHL | 4bits |
| TOS | 8bits |
| Total Length | 16bits |
| Identification | 16bits |
| Flags | 3bits |
| Fragment Offset | 13bits |
| Time to Live | 8bits |
| Protocol | 8bits |
| Header Checksum | 16bits |
| Source Address | 32bits |
| Destination Address | 32bits |
| Options | 가변 |
| Padding | 가변 |

### IPv6 헤더

| 필드 | 크기 |
|:-----|:-----|
| Version | 4bits |
| Traffic Class | 8bits |
| Flow Label | 20bits |
| Payload Length | 16bits |
| Next Header | 8bits |
| Hop Limit | 8bits |
| Source Address | 128bits |
| Destination Address | 128bits |

{: .note }
> Flow Label 이 IPv6에 추가됨
> IHL, Identification, Flags, Fragment Offset, Header Checksum, Options, Padding 은 IPv4 에서만 사용

---

## IPv4 와 IPv6의 특징 비교

| 구분 | IPv4 | IPv6 |
|:-----|:-----|:-----|
| **주소 길이** | 32비트 | 128비트 |
| **표시 방법** | 8비트씩 4부분으로 10진수 표시<br>202.20.64.22 | 16비트씩 8부분으로 16진수로 표시<br>2001:0211:badc:ffff:0000:0000:ffff:1111 |
| **수소 개수** | 약 43억개 | 약(43억X43억X43억X43억)개<br>(거의 무한대) |
| **주소 할당** | A, B, C, D등 class 단위의 비순차적할당<br>(비효율적) | 네트워크 규모 및 단말기 수에 따른 순차적 할당(효율적) |
| **품질 제어** | Best Effort 방식으로 품질 보장이 곤란<br>(Type of Service에 의한 QoS 일부지원) | 등급별, 서비스별로 패킷을 구분할 수 있어 품질보장이 용이(Traffic Class, Flow Label에 의한 QoS 지원) |
| **보안 기능** | IPSec 프로토콜 별도 설치 | 확장기능에서 기본으로 제공 |
| **Plug & Play** | 없음 | 있음(자동 네트워킹 가능) |
| **Mobile IP** | 상당히 곤란(비효율적) | 용이(효율적) |
| **웹 캐스팅** | 곤란 | 용이(Scope Field 증가) |

{: .highlight }
> IPv6 는 IPv4 의 협소한 주소 공간을 해결

---

## 연계 토픽

- [NAT](/docs/nw/03-fundamentals/nat)
- [Subnetting/Supernetting](/docs/nw/06-management/subnetting)

---

## 학습 체크리스트

- [ ] IPv4 vs IPv6 차이점 이해
- [ ] 헤더 구조 비교
- [ ] IPv6 장점 파악

---

## 참고자료

- 정보관리기술사 NW 학습자료


