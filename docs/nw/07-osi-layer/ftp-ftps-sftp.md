---
layout: default
title: FTP·FTPS·SFTP
parent: 7. OSI 7 Layer
grand_parent: NW (네트워크)
nav_order: 5
---

# FTP·FTPS·SFTP
{: .fs-8 }

7.1 OSI 7 Layer
{: .label .label-purple }

---

## 핵심 키워드

`FTP` `TCP` `파일 전송` `FTPS` `SSL/TLS` `SFTP` `SSH` `터널링`

---

## 정의/개념

- **FTP**: TCP/IP 프로토콜 기반, 서버-클라이언트 사이에서 파일 송수신 위한 프로토콜
- **FTPS**: 보안기능 제공 위해 SSL/TLS 암호화 프로토콜 기반에서 동작하도록 설계된 FTP
- **SFTP**: SSH를 통해 동작, TCP 터널링을 형성하여 데이터 안전 전송 가능하게 하는 FTP

---

## FTP (File Transfer Protocol)

| 구분 | 설명 |
|:-----|:-----|
| **형식** | Format: MAC-header / IP-header / TCP header / data |
| **특징** | 서버와 클라이언트 모두 2개 이상의 포트 사용<br>데이터 전송 중간에 종료, 이어받기 가능<br>사용자 관리: 익명사용자 접속 가능 시간 제한 |
| **기능** | 파일: 파일 종류 선택<br>권한 관리: 접근가능 디렉토리 정의<br>특정 사용자 IP제한하기 |
| **구조** | 제어 신호를 전달하기 위한 Control Channel, 데이터 전송을 위한 Data Channel이 설정 |
| **전송모드** | Active 모드: 서버에서 클라이언트의 특정 포트 접속 데이터 전송 (명령 21, 데이터 20 포트)<br>Passive 모드: 클라이언트에서 서버의 특정 포트 접속 데이터 전송 (명령 21, 데이터 1024 이후) |

---

## FTPS (FTP Secure)

| 구분 | 설명 |
|:-----|:-----|
| **특징** | 인증, 암호화, 무결성을 보장 |
| **기능** | 암호기 기반 인증 방식 3가지 인증모드 지원, 다양한 암호 알고리즘 지원, 핸드 쉐이크 통신 |
| **구조 (스택)** | HTTP / FTP / Telnet / SMTP → SSL/TLS → TCP |

{: .note }
> Change Cipher Spec Protocol: 암호화 알고리즘과 보안 정책을 송수신 측간에 조율

---

## SFTP (SSH FTP)

| 구분 | 설명 |
|:-----|:-----|
| **특징** | 인증과 기밀성 유지 보안 우수 + FTP 장점 수용<br>패킷 형식: length / padding type / data / CRC |
| **기능** | 키 구성: 호스트 키, 세션키<br>암호화(encryption), 무결성, 압축, 포트 포워딩(터널링) |
| **구조 (스택)** | SSH 응용 → SSH-Auth (인증) / SSH-Conn (연결) → SSH-Trans (전송) → TCP |

{: .highlight }
> FTP는 사용자 인증정보에 대한 암호화가 되지 않고, 평문으로 전송되는 취약점으로 인해 기능적인 측면에서 FTPS, SFTP 와의 차이점이 명확하게 존재

---

## 연계 토픽

- [TLS](/docs/nw/07-osi-layer/tls)
- [TCP](/docs/nw/07-osi-layer/tcp)

---

## 학습 체크리스트

- [ ] FTP, FTPS, SFTP 개념 이해
- [ ] 각 프로토콜의 보안 특성 비교
- [ ] Active/Passive 모드 차이 구분

---

## 참고자료

- 정보관리기술사 NW 학습자료


