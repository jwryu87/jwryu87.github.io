#!/usr/bin/env python3
"""
DS 카테고리 빈 포스트 자동 생성 스크립트
"""

import os
from datetime import datetime

# DS 항목 데이터
DS_TOPICS = {
    "01-cloud": {
        "name": "클라우드",
        "items": [
            # 1.1 클라우드 개념
            ("클라우드 컴퓨팅", "cloud-computing"),
            ("클라우드 컴퓨팅 서비스 품질·성능 기준", "cloud-service-quality"),
            ("클라우드운영별 분류", "cloud-types"),
            ("멀티 클라우드", "multi-cloud"),
            ("분산 클라우드", "distributed-cloud"),
            ("클라우드 네이티브", "cloud-native"),
            ("클라우드 네이티브 15 Factor", "cloud-native-15-factor"),
            ("서버리스 컴퓨팅", "serverless-computing"),
            ("XaaS", "xaas"),
            # 1.2 클라우드 아키텍처 / 전환
            ("오토스케일링", "auto-scaling"),
            ("클라우드 마이그레이션", "cloud-migration"),
            ("랜딩존", "landing-zone"),
            ("클라우드 전환", "cloud-transformation"),
            ("민간 클라우드 이용 절차", "cloud-adoption-process"),
            # 1.3 클라우드 보안
            ("CSAP", "csap"),
            ("CASB", "casb"),
            ("클라우드 보안 인증 제도", "cloud-security-certification"),
            ("클라우드 컴퓨팅 보안", "cloud-computing-security"),
            # 1.4 클라우드 운영
            ("MSP", "msp"),
            ("클라우드 운용성", "cloud-operability"),
            # 1.5 OpenStack
            ("오픈 스택 프로젝트", "openstack"),
        ]
    },
    "02-xr-metaverse": {
        "name": "가상융합_XR_메타버스",
        "items": [
            ("메타버스", "metaverse"),
            ("메타버스 윤리 원칙", "metaverse-ethics"),
            ("실감형 콘텐츠", "immersive-content"),
            ("XR", "xr"),
            ("Smart City", "smart-city"),
            ("스마트시티 통합 플랫폼", "smart-city-platform"),
        ]
    },
    "03-blockchain": {
        "name": "블록체인",
        "items": [
            ("블록체인", "blockchain"),
            ("퍼블릭_프라이빗_하이브리드 블록체인", "blockchain-types"),
            ("블록체인 분산 저장 기술", "blockchain-distributed-storage"),
            ("블록체인 경량화 기술", "blockchain-lightweight"),
            ("블록체인 암호기술 가이드라인", "blockchain-crypto-guideline"),
            ("머클트리", "merkle-tree"),
            ("영지식 증명", "zero-knowledge-proof"),
            ("합의 알고리즘", "consensus-algorithm"),
            ("블록체인 트릴레마", "blockchain-trilemma"),
            ("스마트 컨트랙트", "smart-contract"),
            ("스마트 계약의 오라클", "smart-contract-oracle"),
            ("디지털 ID", "digital-id"),
            ("DID", "did"),
            ("디지털 신분증", "digital-identity-card"),
            ("암호화폐 지갑", "crypto-wallet"),
            ("CBDC", "cbdc"),
            ("NFT", "nft"),
            ("STO", "sto"),
            ("스테이블코인", "stablecoin"),
            ("하이퍼레저", "hyperledger"),
            ("라이트닝 네트워크", "lightning-network"),
            ("DAO", "dao"),
            ("Travel Rule", "travel-rule"),
        ]
    },
    "04-autonomous-vehicle": {
        "name": "스마트카_자율주행",
        "items": [
            ("자율주행 자동차", "autonomous-vehicle"),
            ("자율주행 단계", "autonomous-levels"),
            ("HD맵", "hd-map"),
            ("자율주행 윤리 가이드라인", "autonomous-ethics"),
            ("RADAR", "radar"),
            ("LiDAR", "lidar"),
            ("ISO 26262", "iso-26262"),
            ("ISO_SAE 21434", "iso-sae-21434"),
            ("ISO_PAS 21448", "iso-pas-21448"),
            ("ASIL", "asil"),
            ("스마트카", "smart-car"),
            ("MaaS", "maas"),
            ("SDV", "sdv"),
            ("모빌리티 혁신 로드맵", "mobility-roadmap"),
        ]
    },
    "05-smart-factory": {
        "name": "스마트공장",
        "items": [
            ("스마트 공장", "smart-factory"),
            ("디지털 트윈", "digital-twin"),
        ]
    },
    "06-smart-grid": {
        "name": "스마트그리드_에너지",
        "items": [
            ("스마트그리드", "smart-grid"),
            ("AMI", "ami"),
            ("에너지 수확", "energy-harvesting"),
            ("인터미턴트 컴퓨팅", "intermittent-computing"),
            ("분산 에너지 시스템", "distributed-energy-system"),
        ]
    },
    "07-virtualization": {
        "name": "가상화_컨테이너",
        "items": [
            ("가상화 종류", "virtualization-types"),
            ("애플리케이션 가상화", "application-virtualization"),
            ("Hypervisor", "hypervisor"),
            ("HCI", "hci"),
            ("Docker", "docker"),
            ("Container", "container"),
            ("CRI", "cri"),
            ("Kubernetes", "kubernetes"),
            ("Container Orchestration", "container-orchestration"),
        ]
    },
    "08-iot": {
        "name": "IoT",
        "items": [
            ("IoT", "iot"),
            ("NB-IoT", "nb-iot"),
        ]
    },
    "09-drone-uam": {
        "name": "드론_UAM",
        "items": [
            ("드론", "drone"),
            ("안티드론", "anti-drone"),
            ("UAM", "uam"),
        ]
    },
    "10-digital-healthcare": {
        "name": "디지털_헬스케어",
        "items": [
            ("u-Health", "u-health"),
            ("디지털 헬스케어", "digital-healthcare"),
            ("디지털 치료제", "digital-therapeutics"),
        ]
    },
    "11-distributed-computing": {
        "name": "분산_컴퓨팅",
        "items": [
            ("엣지 컴퓨팅", "edge-computing"),
            ("모바일 엣지 컴퓨팅", "mobile-edge-computing"),
            ("포그 컴퓨팅", "fog-computing"),
            ("서버리스 컴퓨팅", "serverless-computing-dist"),
        ]
    },
    "12-ui-ux": {
        "name": "UI_UX",
        "items": [
            ("전자정부 웹사이트 UI_UX", "e-gov-ui-ux"),
            ("웹 접근성", "web-accessibility"),
            ("전자정부 웹사이트 품질관리 지침", "e-gov-quality-guideline"),
            ("전자정부 UI_UX 설계기준", "e-gov-ui-ux-standard"),
            ("UX_UI", "ux-ui"),
            ("토탈 경험", "total-experience"),
        ]
    },
    "13-api": {
        "name": "API",
        "items": [
            ("오픈 API", "open-api"),
            ("API Gateway", "api-gateway"),
            ("API Management", "api-management"),
            ("서비스 메시", "service-mesh"),
        ]
    },
    "14-spatial-info": {
        "name": "공간정보",
        "items": [
            ("공간 DB", "spatial-db"),
            ("측위 기술", "positioning-technology"),
        ]
    },
    "15-design-thinking": {
        "name": "문제해결_디자인씽킹",
        "items": [
            ("디자인씽킹", "design-thinking"),
        ]
    },
    "16-e-government": {
        "name": "전자정부",
        "items": [
            ("전자정부 평가", "e-government-evaluation"),
        ]
    },
    "17-gartner": {
        "name": "가트너_전략",
        "items": [
            ("가트너 전략기술 2024", "gartner-2024"),
            ("슈퍼앱", "super-app"),
        ]
    },
    "18-etc": {
        "name": "DS_기타",
        "items": [
            ("OLAP", "olap"),
            ("디지털 플랫폼 정부", "digital-platform-government"),
            ("리빙랩", "living-lab"),
            ("로우코드_노코드", "low-code-no-code"),
            ("데이터 메시", "data-mesh"),
            ("Scale-up_Scale-out", "scale-up-out"),
        ]
    },
    "19-robot-automation": {
        "name": "로봇_자동화",
        "items": [
            ("로봇", "robot"),
            ("RPA", "rpa"),
            ("IPA", "ipa"),
            ("Hyperautomation", "hyperautomation"),
            ("멀티 에이전트 협업", "multi-agent-collaboration"),
        ]
    },
    "20-recommendation": {
        "name": "추천_시스템",
        "items": [
            ("추천 시스템", "recommendation-system"),
            ("협업 필터링", "collaborative-filtering"),
        ]
    },
    "21-computer-vision": {
        "name": "영상처리_영상보안",
        "items": [
            ("Computer Vision", "computer-vision"),
            ("지능형 영상 분석", "intelligent-video-analytics"),
            ("지능형 CCTV", "intelligent-cctv"),
            ("원격근무", "remote-work"),
        ]
    },
    "22-digital-wallet": {
        "name": "디지털_지갑_FinOps",
        "items": [
            ("디지털 지갑", "digital-wallet"),
            ("FinOps", "finops"),
        ]
    },
    "23-infrastructure": {
        "name": "인프라스트럭처",
        "items": [
            ("IaC", "iac"),
        ]
    },
    "24-web-tech": {
        "name": "웹_기술_검색엔진",
        "items": [
            ("Semantic Web", "semantic-web"),
            ("TF-IDF", "tf-idf"),
            ("온톨로지", "ontology"),
            ("RDF", "rdf"),
            ("Web 3.0", "web-3-0"),
            ("HTML5", "html5"),
            ("OAuth 2.0", "oauth-2-0"),
        ]
    },
}

def slugify(text):
    """한글 제목을 URL-safe한 slug로 변환"""
    return text.lower().replace(" ", "-").replace("/", "-").replace("·", "-")

def create_post(category, item_name, slug, base_path):
    """빈 포스트 생성"""
    date = "2025-01-02"
    time = "10:00:00"
    
    filename = f"{date}-{slug}.md"
    filepath = os.path.join(base_path, "_posts", "ds", category, filename)
    
    # 이미 파일이 있으면 스킵
    if os.path.exists(filepath):
        return False
    
    content = f"""---
layout: post
title: (DS) {item_name}
date: {date} {time} +09:00
categories: ds
tags: [ds, {DS_TOPICS[category]['name']}]
comments: true
---

# {item_name}

## 개념

<!-- 여기에 내용을 작성하세요 -->

<!-- more -->

## 상세 내용

## 관련 개념

---

**학습 체크리스트:**
- [ ] 개념 이해
- [ ] 실무 적용 사례 파악
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    base_path = "/Users/jaewoo.ryu/woowa/dev/pe-study"
    
    total = 0
    created = 0
    
    for category, data in DS_TOPICS.items():
        print(f"\n📁 {category} ({data['name']})")
        for item_name, slug in data['items']:
            total += 1
            if create_post(category, item_name, slug, base_path):
                created += 1
                print(f"  ✅ {item_name}")
            else:
                print(f"  ⏭️  {item_name} (이미 존재)")
    
    print(f"\n\n🎉 완료!")
    print(f"총 {total}개 항목 중 {created}개 포스트 생성")

if __name__ == "__main__":
    main()

