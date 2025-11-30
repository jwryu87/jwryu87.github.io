#!/usr/bin/env python3
"""
Just the Docs 형식으로 DS 페이지 마이그레이션
"""

import os

BASE_PATH = "/Users/jaewoo.ryu/woowa/dev/jwryu87.github.io/docs/ds"

# DS 카테고리 데이터
CATEGORIES = [
    {
        "id": "01-cloud",
        "title": "1. 클라우드",
        "nav_order": 1,
        "sections": [
            {
                "name": "1.1 클라우드 개념",
                "items": [
                    "클라우드 컴퓨팅",
                    "클라우드 컴퓨팅 서비스 품질·성능 기준",
                    "클라우드운영별 분류 (Public/Private/Hybrid)",
                    "멀티 클라우드",
                    "분산 클라우드",
                    "클라우드 네이티브",
                    "클라우드 네이티브 15 Factor",
                    "서버리스 컴퓨팅",
                    "XaaS (IaaS/PaaS/SaaS/DaaS/SecaaS)",
                ]
            },
            {
                "name": "1.2 클라우드 아키텍처/전환",
                "items": [
                    "오토스케일링",
                    "클라우드 마이그레이션",
                    "랜딩존",
                    "클라우드 전환",
                    "민간 클라우드 이용 절차",
                ]
            },
            {
                "name": "1.3 클라우드 보안",
                "items": [
                    "CSAP",
                    "CASB",
                    "클라우드 보안 인증 제도",
                    "클라우드 컴퓨팅 보안",
                ]
            },
            {
                "name": "1.4 클라우드 운영",
                "items": [
                    "MSP",
                    "클라우드 운용성",
                ]
            },
            {
                "name": "1.5 OpenStack",
                "items": [
                    "오픈 스택 프로젝트",
                ]
            },
        ]
    },
    {
        "id": "02-xr-metaverse",
        "title": "2. 가상융합/XR/메타버스",
        "nav_order": 2,
        "sections": [
            {
                "name": "2.1 메타버스",
                "items": ["메타버스", "메타버스 윤리 원칙", "실감형 콘텐츠"]
            },
            {
                "name": "2.2 XR",
                "items": ["XR(확장현실)"]
            },
            {
                "name": "2.3 스마트시티",
                "items": ["Smart City", "스마트시티 통합 플랫폼"]
            },
        ]
    },
    {
        "id": "03-blockchain",
        "title": "3. 블록체인",
        "nav_order": 3,
        "sections": [
            {
                "name": "3.1 블록체인 기본",
                "items": ["블록체인", "퍼블릭/프라이빗/하이브리드 블록체인", "블록체인 분산 저장 기술", "블록체인 경량화 기술"]
            },
            {
                "name": "3.2 블록체인 암호 기술",
                "items": ["블록체인 암호기술 가이드라인", "머클트리", "영지식 증명"]
            },
            {
                "name": "3.3 합의 알고리즘",
                "items": ["합의 알고리즘", "블록체인 트릴레마"]
            },
            {
                "name": "3.4 스마트 컨트랙트",
                "items": ["스마트 컨트랙트", "스마트 계약의 오라클"]
            },
            {
                "name": "3.5 ID/Wallet",
                "items": ["디지털 ID", "DID", "디지털 신분증", "암호화폐 지갑"]
            },
            {
                "name": "3.6 블록체인 경제",
                "items": ["CBDC", "NFT", "STO", "스테이블코인"]
            },
            {
                "name": "3.7 블록체인 생태계",
                "items": ["하이퍼레저", "라이트닝 네트워크", "DAO", "Travel Rule"]
            },
        ]
    },
    {
        "id": "04-autonomous",
        "title": "4. 스마트카/자율주행",
        "nav_order": 4,
        "sections": [
            {
                "name": "4.1 자율주행 기술",
                "items": ["자율주행 자동차", "자율주행 단계(SAE)", "HD맵/LDM", "자율주행 윤리 가이드라인"]
            },
            {
                "name": "4.2 차량 센서 기술",
                "items": ["RADAR", "LiDAR"]
            },
            {
                "name": "4.3 차량 표준 및 안전",
                "items": ["ISO 26262", "ISO/SAE 21434", "ISO/PAS 21448", "ASIL"]
            },
            {
                "name": "4.4 모빌리티",
                "items": ["스마트카", "MaaS", "SDV", "모빌리티 혁신 로드맵"]
            },
        ]
    },
    {
        "id": "05-smart-factory",
        "title": "5. 스마트공장",
        "nav_order": 5,
        "sections": [
            {
                "name": "5. 스마트공장",
                "items": ["스마트 공장", "디지털 트윈"]
            },
        ]
    },
    {
        "id": "06-smart-grid",
        "title": "6. 스마트그리드/에너지",
        "nav_order": 6,
        "sections": [
            {
                "name": "6.1 스마트 그리드",
                "items": ["스마트그리드", "AMI"]
            },
            {
                "name": "6.2 에너지 기술",
                "items": ["에너지 수확", "인터미턴트 컴퓨팅", "분산 에너지 시스템"]
            },
        ]
    },
    {
        "id": "07-virtualization",
        "title": "7. 가상화/컨테이너",
        "nav_order": 7,
        "sections": [
            {
                "name": "7.1 가상화 기본",
                "items": ["가상화 종류", "애플리케이션 가상화", "Hypervisor", "HCI"]
            },
            {
                "name": "7.2 컨테이너",
                "items": ["Docker", "Container", "CRI/CRI-O"]
            },
            {
                "name": "7.3 컨테이너 오케스트레이션",
                "items": ["Kubernetes", "Container Orchestration"]
            },
        ]
    },
    {
        "id": "08-iot",
        "title": "8. IoT",
        "nav_order": 8,
        "sections": [
            {
                "name": "8. IoT",
                "items": ["IoT", "NB-IoT"]
            },
        ]
    },
    {
        "id": "09-drone-uam",
        "title": "9. 드론/UAM",
        "nav_order": 9,
        "sections": [
            {
                "name": "9. 드론/UAM",
                "items": ["드론", "안티드론", "UAM"]
            },
        ]
    },
    {
        "id": "10-healthcare",
        "title": "10. 디지털 헬스케어",
        "nav_order": 10,
        "sections": [
            {
                "name": "10. 디지털 헬스케어",
                "items": ["u-Health", "디지털 헬스케어", "디지털 치료제"]
            },
        ]
    },
    {
        "id": "11-distributed",
        "title": "11. 분산 컴퓨팅",
        "nav_order": 11,
        "sections": [
            {
                "name": "11. 분산 컴퓨팅",
                "items": ["엣지 컴퓨팅", "모바일 엣지 컴퓨팅", "포그 컴퓨팅", "서버리스 컴퓨팅"]
            },
        ]
    },
    {
        "id": "12-ui-ux",
        "title": "12. UI/UX",
        "nav_order": 12,
        "sections": [
            {
                "name": "12. UI/UX",
                "items": ["전자정부 웹사이트 UI/UX", "웹 접근성", "전자정부 웹사이트 품질관리 지침", "전자정부 UI/UX 설계기준", "UX/UI", "토탈 경험"]
            },
        ]
    },
    {
        "id": "13-api",
        "title": "13. API",
        "nav_order": 13,
        "sections": [
            {
                "name": "13. API",
                "items": ["오픈 API", "API Gateway", "API Management", "서비스 메시"]
            },
        ]
    },
    {
        "id": "14-spatial",
        "title": "14. 공간정보",
        "nav_order": 14,
        "sections": [
            {
                "name": "14. 공간정보",
                "items": ["공간 DB", "측위 기술"]
            },
        ]
    },
    {
        "id": "15-design-thinking",
        "title": "15. 디자인씽킹",
        "nav_order": 15,
        "sections": [
            {
                "name": "15. 디자인씽킹",
                "items": ["디자인씽킹"]
            },
        ]
    },
    {
        "id": "16-e-gov",
        "title": "16. 전자정부",
        "nav_order": 16,
        "sections": [
            {
                "name": "16. 전자정부",
                "items": ["전자정부 평가"]
            },
        ]
    },
    {
        "id": "17-gartner",
        "title": "17. 가트너 전략",
        "nav_order": 17,
        "sections": [
            {
                "name": "17. 가트너 전략",
                "items": ["가트너 전략기술 2024", "슈퍼앱"]
            },
        ]
    },
    {
        "id": "18-etc",
        "title": "18. DS 기타",
        "nav_order": 18,
        "sections": [
            {
                "name": "18. DS 기타",
                "items": ["OLAP", "디지털 플랫폼 정부", "리빙랩", "로우코드/노코드", "데이터 메시", "Scale-up/Scale-out"]
            },
        ]
    },
    {
        "id": "19-robot",
        "title": "19. 로봇/자동화",
        "nav_order": 19,
        "sections": [
            {
                "name": "19. 로봇/자동화",
                "items": ["로봇", "RPA", "IPA", "Hyperautomation", "멀티 에이전트 협업"]
            },
        ]
    },
    {
        "id": "20-recommendation",
        "title": "20. 추천 시스템",
        "nav_order": 20,
        "sections": [
            {
                "name": "20. 추천 시스템",
                "items": ["추천 시스템", "협업 필터링"]
            },
        ]
    },
    {
        "id": "21-vision",
        "title": "21. 영상처리/영상보안",
        "nav_order": 21,
        "sections": [
            {
                "name": "21. 영상처리/영상보안",
                "items": ["Computer Vision", "지능형 영상 분석", "지능형 CCTV", "원격근무"]
            },
        ]
    },
    {
        "id": "22-finops",
        "title": "22. 디지털 지갑/FinOps",
        "nav_order": 22,
        "sections": [
            {
                "name": "22. 디지털 지갑/FinOps",
                "items": ["디지털 지갑", "FinOps"]
            },
        ]
    },
    {
        "id": "23-infra",
        "title": "23. 인프라스트럭처",
        "nav_order": 23,
        "sections": [
            {
                "name": "23. 인프라스트럭처",
                "items": ["IaC"]
            },
        ]
    },
    {
        "id": "24-web",
        "title": "24. 웹 기술/검색엔진",
        "nav_order": 24,
        "sections": [
            {
                "name": "24. 웹 기술/검색엔진",
                "items": ["Semantic Web", "TF-IDF", "온톨로지", "RDF", "Web 3.0", "HTML5", "OAuth 2.0"]
            },
        ]
    },
]


def slugify(text):
    """텍스트를 URL-safe 슬러그로 변환"""
    return text.lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "").replace("·", "-")


def create_category_index(category):
    """카테고리 인덱스 페이지 생성"""
    folder = os.path.join(BASE_PATH, category["id"])
    os.makedirs(folder, exist_ok=True)
    
    # 전체 항목 수 계산
    total_items = sum(len(s["items"]) for s in category["sections"])
    
    content = f"""---
layout: default
title: {category["title"]}
parent: DS (Digital Strategy)
nav_order: {category["nav_order"]}
has_children: true
permalink: /docs/ds/{category["id"]}
---

# {category["title"]}
{{: .fs-8 }}

총 {total_items}개 항목
{{: .fs-5 .fw-300 }}

---

"""
    # 섹션별 항목 추가
    for section in category["sections"]:
        content += f"## {section['name']}\n\n"
        for item in section["items"]:
            content += f"- [ ] {item}\n"
        content += "\n"
    
    with open(os.path.join(folder, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)
    
    return folder


def create_item_page(category, section_name, item, nav_order, folder):
    """개별 항목 페이지 생성"""
    slug = slugify(item)
    filename = f"{slug}.md"
    
    content = f"""---
layout: default
title: {item}
parent: {category["title"]}
grand_parent: DS (Digital Strategy)
nav_order: {nav_order}
---

# {item}
{{: .fs-8 }}

{section_name}
{{: .label .label-purple }}

---

## 개념

<!-- 여기에 개념을 작성하세요 -->

---

## 상세 내용

<!-- 여기에 상세 내용을 작성하세요 -->

---

## 특징/장단점

| 구분 | 내용 |
|:-----|:-----|
| 장점 |  |
| 단점 |  |

---

## 관련 개념

- 

---

## 학습 체크리스트

- [ ] 개념 이해
- [ ] 핵심 키워드 암기
- [ ] 실무 적용 사례 파악
- [ ] 관련 기술 연계

---

## 참고자료

- 
"""
    
    with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
        f.write(content)


def main():
    total_items = 0
    
    for category in CATEGORIES:
        print(f"\n📁 {category['title']}")
        folder = create_category_index(category)
        
        nav_order = 1
        for section in category["sections"]:
            for item in section["items"]:
                create_item_page(category, section["name"], item, nav_order, folder)
                print(f"  ✅ {item}")
                nav_order += 1
                total_items += 1
    
    print(f"\n\n🎉 완료! 총 {total_items}개 페이지 생성")


if __name__ == "__main__":
    main()

