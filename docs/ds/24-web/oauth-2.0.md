---
layout: default
title: OAuth 2.0
parent: 24. 웹 기술/검색엔진
grand_parent: DS (Digital Service)
nav_order: 7
---

# OAuth 2.0
{: .fs-8 }

24. 웹 기술/검색엔진
{: .label .label-purple }

---

## 정의

자원 접근 **권한을 위임**하는 OpenAPI 기반 보안 인증 기술

---

## 특징

- 비밀번호 불필요
- 제한된 권한
- 클라이언트별 관리
- 표준

---

## 인증 절차

| 단계 | 설명 |
|:-----|:-----|
| **권한** | 권한 요청 → 권한 승인 (Resource Owner) |
| **토큰** | Access Token 요청 → Access Token 발급 (Authorization Server) |
| **자원** | 보호된 자원 요청 → 서비스 제공 (Resource Server) |

---

## 구성요소

| 구성요소 | 설명 |
|:---------|:-----|
| **Client** | 클라이언트 애플리케이션 |
| **Resource Owner** | 자원 소유자 (사용자) |
| **Authorization Server** | 인증 서버 |
| **Resource Server** | 자원 서버 |
| **Access Token** | 접근 토큰 |

---

## 인증 흐름

```
Client → Resource Owner: 권한 요청
Resource Owner → Client: 권한 승인
Client → Auth Server: Token 요청
Auth Server → Client: Token 발급
Client → Resource Server: 자원 요청 (Token 포함)
Resource Server → Client: 서비스 제공
```

---

## 관련 개념

- [오픈 API](/docs/ds/13-api/오픈-api)

---

## 학습 체크리스트

- [ ] OAuth 2.0 정의 이해
- [ ] 인증 절차 3단계 (권한→토큰→자원) 암기
- [ ] 구성요소 5가지 파악

---

## 참고자료

- 정보관리기술사 DS 학습자료 
