---
layout: default
title: NFT
parent: 3. 블록체인
grand_parent: DS (Digital Service)
nav_order: 17
---

# NFT (Non Fungible Token)
{: .fs-8 }

3.2 블록체인 활용
{: .label .label-green }

---

## 핵심 키워드

`ERC-721` `Metadata` `Oracle` `IPFS`

---

## 정의/개념

ERC-721, **위·변조 불가**, 부분 소유 가능, 추적 용이, 디지털 자산 **대체 불가능 토큰**

---

## NFT 아키텍처

| 구분 | 주요요소 | 설명 |
|:-----|:---------|:-----|
| **On-Chain** | ERC-721 | ERC-721 기반 Non-Fungible Token (소유자 정보 기록)<br>콘텐츠 핵심 정보 TAG (이미지, 음악, 게임 등) |
|  | ERC-721 Contract | 소유자의 주소 정보 획득<br>Metadata와 연결을 위한 URL 정보 획득 |
|  | Metadata | 토큰의 콘텐츠에 대한 상세 TAG<br>실제 데이터는 블록체인 내부 저장 시 용량의 한계 존재 |
|  | Oracle | Off-Chain의 디지털 자산을 On-Chain으로 확장 중계 시스템 |
| **Off-Chain** | IPFS | 분산환경에서 데이터를 저장하기 위한 파일 시스템 |
|  | NFT Owner/Creator | 디지털 자산 소유자와 생성자 |
|  | NFT Buyer | 디지털 자산 구매자 |

---

## NFT 프로토콜

| 프로토콜 | 내용 |
|:---------|:-----|
| **NFT Digitize (디지털화)** | - NFT 소유자는 파일, 제목, 설명이 완전히 일치하는지 확인<br>- 소유자는 적합한 포맷으로 raw data 를 디지털 정보로 전환 |
| **NFT Store (저장)** | - NFT 소유자는 블록체인 외부의 데이터베이스에 raw data 를 저장<br>- 소유자는 가스를 소비하는 명령 을 통해 raw data 를 블록체인 내부에 저장할 것을 결정 |
| **NFT Sign (서명)** | - NFT 소유자는 NFT 데이터를 포함한 거래내역에 서명하고, 스마트 컨트랙트에 거래내역을 전송 |
| **NFT Mint (발행)** | - 스마트 컨트랙트는 NFT 데이터가 담긴 거래내역을 받아 NFT 를 발행한다. NFT 의 내부 기능은 토큰 표준에서 정의 |
| **NFT Confirm (확인)** | - 발행 프로세스는 한 번 거래내역이 확인되면 완료<br>- NFT 는 영속적인 증거(Proof)로서 유일한 블록 체인 주소와 연결 |

- NFT 는 이더리움 블록체인 기술과 **ERC-721 표준**을 기반으로 구현

---

## 연계 토픽

- [NFT Minting](/docs/ds/03-blockchain/)
- [블록체인](/docs/ds/03-blockchain/블록체인)

---

## 학습 체크리스트

- [ ] NFT 정의 이해
- [ ] ERC-721 표준 이해
- [ ] On-Chain vs Off-Chain 구분
- [ ] NFT 프로토콜 5단계 (Digitize → Store → Sign → Mint → Confirm) 숙지

---

## 참고자료

- 정보관리기술사 DS 학습자료
