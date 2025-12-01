---
layout: default
title: 키 스트레칭 (Key Stretching)
parent: 암호화
grand_parent: 보안
nav_order: 7
---

# 키 스트레칭 (Key Stretching)
{: .fs-8 }

10.7 암호화
{: .label .label-purple }

---

## 핵심 키워드

`해시함수 N번 반복` `Salt` `PEPPER` `Iteration Count` `Rainbow Table 방어`

---

## 정의/개념

**Rainbow Table, Brute Force Attack 회피** 위해, 해시함수 **N번 반복 다이제스트 생성** 기법

- 비밀번호 해시 계산 시간을 의도적으로 늘려 공격자의 무차별 대입 공격 비용 증가

---

## 메커니즘

### 키 스트레칭의 구성도

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│         메시지                  반복수행                       │
│            │                 Iteration Count                │
│            ↓                      │                         │
│     평문(PlainText)               ↓                         │
│            │              ┌────────────┐                    │
│     ┌──────┼──────┐       │   해시함수   │                    │
│     │      │      │       │   알고리즘   │──> Digest ──> 결과  │
│   SALT     │   PEPPER     └────────────┘                    │
│            │                                                │
└─────────────────────────────────────────────────────────────┘

- 키 스트레칭은 다양한 조합의 메시지를 해시함수 알고리즘을 통해 
  Iteration Count 만큼 반복해서 생성
```

---

## 구성요소

| 구분 | 구성요소 | 특징 |
|:-----|:---------|:-----|
| **메시지** | 평문 | 입력 메시지 |
| | Salt | 랜덤 생성 값 |
| | PEPPER | DB 미저장 고정값 |
| **알고리즘** | MD5 | 임의 길이(평문) → 128비트(암호문) |
| | SHA | 임의 길이(평문) → 160비트(암호문) |
| | CRC32 | 빠른 속도 해시 계산 |
| **키 스트레칭** | Iteration Count | **N번 이상 반복** |
| | 다이제스트 | 생성 출력값 |

---

## 주요 알고리즘

| 알고리즘 | 특징 |
|:---------|:-----|
| **PBKDF2** | Password-Based Key Derivation Function 2<br>HMAC 기반, 반복 횟수 지정 가능 |
| **bcrypt** | Blowfish 기반, 비용 계수로 속도 조절<br>Salt 내장, 적응형 해시 |
| **scrypt** | 메모리 집약적 설계<br>GPU/ASIC 공격 저항 |
| **Argon2** | 2015년 암호 해싱 대회 우승<br>메모리, 시간, 병렬성 조절 가능 |

---

## 키 스트레칭 효과

| 항목 | 효과 |
|:-----|:-----|
| **계산 비용 증가** | 한 번의 해시에 N번 반복 필요 |
| **공격 비용 증가** | 무차별 대입 공격 시간/비용 N배 증가 |
| **레인보우 테이블 무력화** | Salt 조합으로 사전 계산 무효화 |
| **적응성** | 하드웨어 발전에 따라 반복 횟수 증가 가능 |

---

## 반복 횟수 권장 값

| 알고리즘 | 권장 반복 횟수 |
|:---------|:---------------|
| **PBKDF2** | 최소 10,000회 (NIST 권장) |
| **bcrypt** | Cost Factor 10~12 |
| **scrypt** | N=16384, r=8, p=1 |
| **Argon2** | 메모리 1GB, 시간 1초 이상 |

---

## Salt vs Pepper vs Key Stretching

| 구분 | Salt | Pepper | Key Stretching |
|:-----|:-----|:-------|:---------------|
| **저장** | DB | 코드/환경변수 | - |
| **고유성** | 사용자별 | 시스템 공통 | - |
| **목적** | 레인보우 테이블 방어 | 추가 보안 계층 | 무차별 대입 방어 |
| **방식** | 해시 입력에 추가 | 해시 입력에 추가 | 해시 N번 반복 |

---

## 연계 토픽

- [해시 솔트](/docs/sec/10-cryptography/hash-salt)
- [해쉬 함수](/docs/sec/10-cryptography/hash-function)
- [비밀번호 보안](/docs/sec/09-certification/identification-authentication)

---

## 학습 체크리스트

- [ ] 키 스트레칭 메커니즘 이해
- [ ] PBKDF2, bcrypt, scrypt, Argon2 특징 파악
- [ ] Salt, Pepper, Key Stretching 차이점 이해

---

## 참고자료

- 정보관리기술사 보안 학습자료

