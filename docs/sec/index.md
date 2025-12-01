---
layout: default
title: SEC (정보보안)
nav_order: 5
has_children: true
permalink: /docs/sec
---

# SEC (정보보안)
{: .fs-9 }

정보보안 관련 학습 자료입니다. 총 **106개** 항목
{: .fs-6 .fw-300 }

---

## 1. 암호 기술 (17개)

| 구분 | 토픽 |
|:-----|:-----|
| 1-1. 기본 암호 기술 | [암호화](/docs/sec/01-cryptography/encryption) \| [블록 암호](/docs/sec/01-cryptography/block-cipher) \| [해시 함수](/docs/sec/01-cryptography/hash) \| [해시 솔트](/docs/sec/01-cryptography/hash-salt) \| [키 스트레칭](/docs/sec/01-cryptography/key-stretching) \| [MAC/MDC](/docs/sec/01-cryptography/mac-mdc) \| [디피-헬만](/docs/sec/01-cryptography/diffie-hellman) \| [RSA](/docs/sec/01-cryptography/rsa) \| [전자서명](/docs/sec/01-cryptography/digital-signature) \| [이중서명](/docs/sec/01-cryptography/dual-signature) \| [블록 암호화 모드](/docs/sec/01-cryptography/block-cipher-mode) |
| 1-2. 최신 암호 기술 | [동형암호](/docs/sec/01-cryptography/homomorphic-encryption) \| [영지식증명](/docs/sec/01-cryptography/zero-knowledge-proof) \| [형태보존암호(FPE)](/docs/sec/01-cryptography/fpe) \| [순서보존암호(OPE)](/docs/sec/01-cryptography/ope) |
| 1-3. 양자 암호 | [양자암호(QKD)](/docs/sec/01-cryptography/qkd) \| [큐비트](/docs/sec/01-cryptography/qubit) \| [양자내성암호(PQC)](/docs/sec/01-cryptography/pqc) |

---

## 2. 인증·접근통제·식별 (6개)

| 구분 | 토픽 |
|:-----|:-----|
| 2-1. 인증 기술 | [PKI](/docs/sec/02-iam/pki) \| [전자봉투](/docs/sec/02-iam/digital-envelope) \| [FIDO/생체인증](/docs/sec/02-iam/fido) \| [LDAP](/docs/sec/02-iam/ldap) |
| 2-2. 접근통제 | [접근통제 모델](/docs/sec/02-iam/access-control) \| [SSO(SAML/OIDC)](/docs/sec/02-iam/sso) |

---

## 3. 네트워크 보안 (6개)

| 토픽 |
|:-----|
| [VPN(IPSec/SSL/MPLS)](/docs/sec/03-network-security/vpn) \| [SSL/TLS](/docs/sec/03-network-security/ssl-tls) \| [IP 터널링](/docs/sec/03-network-security/ip-tunneling) \| [Tor 네트워크](/docs/sec/03-network-security/tor) \| [SDP](/docs/sec/03-network-security/sdp) \| [Zero Trust Architecture](/docs/sec/03-network-security/zero-trust-architecture) |

---

## 4. 클라우드 / IoT / 스마트 보안 (14개)

| 구분 | 토픽 |
|:-----|:-----|
| 4-1. 클라우드 보안 | [CASB](/docs/sec/04-cloud-iot-smart/casb) \| [SASE](/docs/sec/04-cloud-iot-smart/sase) \| [클라우드 취약점 및 대응](/docs/sec/04-cloud-iot-smart/cloud-vulnerability) \| [클라우드 포렌식](/docs/sec/04-cloud-iot-smart/cloud-forensics) |
| 4-2. IoT/스마트 시스템 보안 | [IoT 보안](/docs/sec/04-cloud-iot-smart/iot-security) \| [AIoT 보안](/docs/sec/04-cloud-iot-smart/aiot-security) \| [스마트팩토리 취약점](/docs/sec/04-cloud-iot-smart/smart-factory-vulnerability) \| [스마트카 취약점](/docs/sec/04-cloud-iot-smart/smart-car-vulnerability) \| [UAM 취약점](/docs/sec/04-cloud-iot-smart/uam-vulnerability) \| [드론 취약점](/docs/sec/04-cloud-iot-smart/drone-vulnerability) \| [MEC 보안](/docs/sec/04-cloud-iot-smart/mec-security) \| [메타버스 보안](/docs/sec/04-cloud-iot-smart/metaverse-security) \| [블록체인 보안](/docs/sec/04-cloud-iot-smart/blockchain-security) \| [NFT/가상화폐 취약점](/docs/sec/04-cloud-iot-smart/nft-vulnerability) |

---

## 5. 사이버 공격 · 위협 분석 (13개)

| 구분 | 토픽 |
|:-----|:-----|
| 5-1. 공격 기법 | [DoS/DDoS](/docs/sec/05-cyber-attack/dos-ddos) \| [랜섬 DDoS(RDoS)](/docs/sec/05-cyber-attack/ransom-ddos) \| [LAND Attack](/docs/sec/05-cyber-attack/land-attack) \| [미러링 봇넷](/docs/sec/05-cyber-attack/mirroring-botnet) \| [공급망 공격](/docs/sec/05-cyber-attack/supply-chain-attack) \| [인포스틸러](/docs/sec/05-cyber-attack/infostealer) \| [소셜 엔지니어링](/docs/sec/05-cyber-attack/social-engineering) \| [RaaS](/docs/sec/05-cyber-attack/raas) \| [랜섬웨어](/docs/sec/05-cyber-attack/ransomware) \| [버전 조작/위조](/docs/sec/05-cyber-attack/fabrication) |
| 5-2. 공격 프레임워크 | [MITRE ATT&CK](/docs/sec/05-cyber-attack/mitre-attack) \| [Cyber Kill Chain](/docs/sec/05-cyber-attack/cyber-kill-chain) \| [APT 공격](/docs/sec/05-cyber-attack/apt) |

---

## 6. 보안 취약점 (14개)

| 구분 | 토픽 |
|:-----|:-----|
| 6-1. 소프트웨어 취약점 | [OWASP Top 10](/docs/sec/06-vulnerability/owasp-top10) \| [Injection](/docs/sec/06-vulnerability/injection) \| [XSS](/docs/sec/06-vulnerability/xss) \| [CSRF](/docs/sec/06-vulnerability/csrf) \| [SSRF](/docs/sec/06-vulnerability/ssrf) |
| 6-2. 시스템/플랫폼 취약점 | [IoT](/docs/sec/06-vulnerability/iot) \| [스마트팩토리](/docs/sec/06-vulnerability/smart-factory) \| [스마트카](/docs/sec/06-vulnerability/smart-car) \| [블록체인](/docs/sec/06-vulnerability/blockchain) \| [딥러닝 AI](/docs/sec/06-vulnerability/ai) \| [MEC](/docs/sec/06-vulnerability/mec) \| [메타버스](/docs/sec/06-vulnerability/metaverse) \| [UAM](/docs/sec/06-vulnerability/uam) \| [클라우드 취약점](/docs/sec/06-vulnerability/cloud) |

---

## 7. 보안 운영 · 대응 (5개)

| 토픽 |
|:-----|
| [위협헌팅](/docs/sec/07-security-operations/threat-hunting) \| [침입탐지/차단 IDS/IPS](/docs/sec/07-security-operations/ids-ips) \| [XDR](/docs/sec/07-security-operations/xdr) \| [SOAR](/docs/sec/07-security-operations/soar) \| [FDS(금융 이상거래탐지)](/docs/sec/07-security-operations/fds) |

---

## 8. 디지털 포렌식 (6개)

| 토픽 |
|:-----|
| [디지털/컴퓨터 포렌식](/docs/sec/08-digital-forensics/digital-forensics) \| [파일카빙](/docs/sec/08-digital-forensics/file-carving) \| [파일슬랙](/docs/sec/08-digital-forensics/file-slack) \| [디스크이미징](/docs/sec/08-digital-forensics/disk-imaging) \| [안티포렌식](/docs/sec/08-digital-forensics/anti-forensics) \| [클라우드 포렌식](/docs/sec/08-digital-forensics/cloud-forensics) |

---

## 9. 개인정보 보호 (8개)

| 구분 | 토픽 |
|:-----|:-----|
| 9-1. 법·제도 | [데이터 3법](/docs/sec/09-privacy/data-3-laws) \| [개인정보 유출신고](/docs/sec/09-privacy/privacy-breach-report) \| [개인정보 영향평가(PIA)](/docs/sec/09-privacy/pia) |
| 9-2. 기술 (PET) | [개인정보 보호기술(PET)](/docs/sec/09-privacy/pet) \| [익명화](/docs/sec/09-privacy/anonymization) \| [비식별화 가이드라인](/docs/sec/09-privacy/de-identification) \| [프라이버시 보호모델](/docs/sec/09-privacy/privacy-model) \| [가명정보 결합](/docs/sec/09-privacy/pseudonymization) |

---

## 10. 보안 정책 · 표준 (7개)

| 토픽 |
|:-----|
| [ISO 27001](/docs/sec/10-policy-standard/iso-27001) \| [ISMS-P](/docs/sec/10-policy-standard/isms-p) \| [ISO/IEC 27017](/docs/sec/10-policy-standard/iso-27017) \| [ISO/IEC 27018](/docs/sec/10-policy-standard/iso-27018) \| [ISMS 예비심사](/docs/sec/10-policy-standard/isms-preliminary) \| [정보보호 제품 신속 확인 제도](/docs/sec/10-policy-standard/security-product-rapid) \| [자동차 사이버보안 표준](/docs/sec/10-policy-standard/automotive-cybersecurity) |

---

## 11. 개발 보안 / 운영 보안 (4개)

| 토픽 |
|:-----|
| [시큐어 코딩](/docs/sec/11-devsecops/secure-coding) \| [Attack Surface Management](/docs/sec/11-devsecops/attack-surface-management) \| [DevSecOps](/docs/sec/11-devsecops/devsecops) \| [콘텐츠 보안](/docs/sec/11-devsecops/content-security) |

---

## 12. 보안 신기술 / 트렌드 (6개)

| 토픽 |
|:-----|
| [Zero Trust](/docs/sec/12-security-trends/zero-trust) \| [SASE](/docs/sec/12-security-trends/sase) \| [AI 기반 위협 탐지](/docs/sec/12-security-trends/ai-threat-detection) \| [블록체인 신기술](/docs/sec/12-security-trends/blockchain-new-tech) \| [양자내성 기술](/docs/sec/12-security-trends/quantum-resistant) \| [RPA/자동화 기반 보안 운영](/docs/sec/12-security-trends/rpa-security) |

---

## 학습 가이드

### 핵심 영역

1. **암호화 기초**: 대칭키/비대칭키, 해시 함수, 전자서명, 양자암호
2. **인증/인가**: PKI, FIDO, SSO, 접근통제 모델
3. **클라우드 보안**: CASB, SASE, Zero Trust
4. **보안솔루션**: XDR, SOAR, IDS/IPS
5. **개인정보보호**: 데이터 3법, PET, 비식별화

### 최신 트렌드

- 제로 트러스트 아키텍처
- 양자내성암호화(PQC)
- DevSecOps
- AI 기반 위협 탐지

---

## 참고자료

- 정보관리기술사 보안 학습자료
- KISA 정보보호 가이드
- NIST Cybersecurity Framework
