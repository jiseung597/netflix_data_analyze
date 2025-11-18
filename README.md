<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" width="320">
</p>

<h1 align="center" style="font-size:42px; margin-bottom:0;">
  🎬 Netflix 콘텐츠 분석 대시보드
</h1>

<p align="center" style="font-size:18px;">
  Streamlit · Python · Plotly · Pandas 기반 인터랙티브 데이터 분석 프로젝트
</p>

---

<br>

## <span style="font-size:28px;">📌 프로젝트 개요 (Project Overview)</span>

Netflix는 전 세계적으로 가장 많은 이용자를 보유한 스트리밍 플랫폼 중 하나이며  
매년 수많은 영화와 TV 시리즈가 추가되는 **방대한 콘텐츠 라이브러리**를 운영하고 있습니다.  

이처럼 규모가 큰 서비스의 콘텐츠 구조를 이해하기 위해서는  
단순한 표 형태가 아닌 **시각화 기반의 체계적인 분석 도구**가 필요합니다.

본 프로젝트는 넷플릭스 콘텐츠 데이터를 활용해  
작품 유형, 장르, 국가, 시청등급, 제작 연도 등의 패턴을 한눈에 확인할 수 있는  
**사용자 친화적 인터랙티브 대시보드**로 구현되었습니다.

<br>

---

## <span style="font-size:28px;">🧠 왜 이 대시보드를 만들었는가? (Why This Project?)</span>

### ✔ 1. 방대한 넷플릭스 콘텐츠를 “정확하고 빠르게” 이해하기 위해  
넷플릭스 데이터는 단순 CSV로 보면 흐름을 파악하기 어렵습니다.  
어느 국가의 콘텐츠가 많은지, 영화/시리즈 비율은 어떠한지,  
어떤 장르가 압도적으로 많은지는 시각화 없이는 알기 힘듭니다.  
이 프로젝트는 이러한 구조를 **직관적으로 파악**할 수 있도록 돕습니다.

### ✔ 2. 필터링 + 시각화 + 자동 업데이트 기능이 필요했기 때문에  
사용자가 원하는 조건(장르 / 국가 / 연도 등)으로 즉시 분석 결과를 바꿔볼 수 있도록  
**인터랙티브 분석 환경**을 Streamlit으로 구축했습니다.

### ✔ 3. 실제 서비스 형태로 데이터 분석을 구현해보기 위한 목적  
Pandas로 전처리하고, Plotly로 시각화하고, Streamlit으로 웹 대시보드를 구성함으로써  
데이터 분석 실습을 넘어 **실제 서비스 가능한 분석 툴을 만드는 경험**을 목표로 했습니다.

### ✔ 4. 과제 및 포트폴리오로 충분히 가치 있는 프로젝트  
데이터 분석, 웹 애플리케이션 구성, 사용자 UI/UX, 로직 설계까지 모두 포함되므로  
과제/포트폴리오에서 높은 평가를 받을 수 있는 형태로 제작되었습니다.

<br>

---

## <span style="font-size:28px;">🔥 주요 기능 (Features)</span>

### ✔ 고급 필터링 기능  
- 제목 검색  
- Movie / TV Show 필터  
- 개봉연도 범위 선택  
- 시청등급 필터  
- 장르 다중 선택  
- 국가 부분 검색 (쉼표로 여러 입력 가능)

### ✔ 실시간 시각화  
- 연도별 콘텐츠 수 변화  
- Movie vs TV Show 비율  
- 인기 장르 Top 15

### ✔ KPI 제공  
- 필터링된 콘텐츠 수  
- 선택된 제작 연도 범위  
- 유형 수  
- 가장 많이 등장한 장르  

### ✔ CSV 다운로드 기능  
필터링된 데이터를 **netflix_filtered.csv**로 다운로드 가능

<br>

---

## <span style="font-size:28px;">🗂 데이터셋 (Dataset)</span>

데이터 파일: **netflix_titles.csv**

| Column | Description |
|--------|-------------|
| type | Movie 또는 TV Show |
| title | 작품 제목 |
| director | 감독 |
| cast | 출연 배우 |
| country | 제작 국가 |
| date_added | 넷플릭스 등록일 |
| release_year | 제작 연도 |
| rating | 시청등급 |
| duration | 러닝타임/에피소드 수 |
| listed_in | 장르 |
| description | 설명 |

<br>

---

## <span style="font-size:28px;">🛠 기술 스택 (Tech Stack)</span>

- **Python 3.x**
- **Streamlit**
- **Pandas**
- **Plotly Express**
- **Pathlib**
- **Collections.Counter**

<br>

---

## <span style="font-size:28px;">📊 주요 화면 (Dashboard Preview)</span>

- 연도별 콘텐츠 Bar Chart  
- Movie/TV Show 비율 Pie·Bar Chart  
- 장르 Top 15  
- 필터 결과 데이터 테이블  
- 필터된 결과 자동 다운로드  

<br>

---

# <span style="font-size:32px;">👥 팀 정보 (Team)</span>

## 🎭 팀명: **덤앤더머 (Dumb & Dumber)**

본 프로젝트는 2인 팀으로 구성되었으며,  
각자 맡은 역할을 명확히 분리하여 효율적으로 개발을 진행했습니다.

---

# <span style="font-size:28px;">🙋‍♂️ 팀원 소개 (Members)</span>

### **1️⃣ 송지승 (Team Leader / Developer)**  
- **역할**
  - Streamlit 기반 전체 대시보드 UI 제작  
  - 필터링 로직 설계 및 구현  
  - Plotly 그래프 생성  
  - README 작성 및 프로젝트 정리  
  - Frontend(데이터 표시 UI) 구성  
- **기여도**
  - 프로젝트 기획 주도  
  - 대시보드 전체 인터랙션 & 사용자 경험 중심 설계  
  - 데이터 시각화 방식 결정 및 그래프 구조 디자인  

---

### **2️⃣ 신준수 (Data Engineer / Backend Developer)**  
- **역할**
  - CSV 데이터 전처리 구조 설계  
  - genre_list, rating, release_year 처리 로직 구현  
  - 데이터 품질 검사 및 필터링 알고리즘 보완  
  - 성능 개선(Pandas 처리 최적화)  
  - 파일 구조 및 테스트  
- **기여도**
  - 데이터 분석 환경 구축  
  - 전처리 자동화 및 오류 처리 안정화  
  - 프로젝트 안정성과 구조적 완성도를 크게 향상  

---

# <span style="font-size:28px;">📝 팀 회고 (Team Retrospective)</span>

## **💬 송지승 – 느낀 점**
- 이번 프로젝트를 통해 데이터 분석과 웹 대시보드를 직접 연결해보는 경험을 얻었다.  
- 단순히 표를 보는 것보다 시각화와 필터링이 얼마나 중요한지 체감했으며,  
  실제 서비스처럼 사용자 인터랙션을 제공하는 것이 큰 의미가 있다고 느꼈다.  
- Streamlit 기반 구조를 처음 접했지만 빠르게 배울 수 있었고,  
  **실제 포트폴리오로 사용 가능한 완성도 높은 프로젝트**를 만들었다고 생각한다.

## **💬 신준수 – 느낀 점**
- 팀 프로젝트를 진행하며 데이터 전처리의 중요성을 크게 실감했다.  
- CSV 구조가 단순해 보여도, 실제로는 결측치·공백·문자열 처리 등 신경 쓸 부분이 많았고,  
  안정적인 필터링을 위해 많은 테스트가 필요했다.  
- 이번 경험을 통해 **실무적인 데이터 클렌징 감각**을 익힐 수 있었으며  
  팀원과 협업하며 역할을 분담하는 법도 배울 수 있었다.  

---

# <span style="font-size:28px;">🎯 총평 (Summary)</span>

**덤앤더머(Dumb & Dumber)** 팀은  
서로의 강점을 기반으로 역할을 분담하여 효율적으로 개발을 진행했습니다.

- 지승 → 사용자 경험 중심 UI·대시보드 설계  
- 준수 → 데이터 안정성과 로직 기반 탄탄한 분석 환경 구축  

이 조합은 “데이터 + 인터랙션”이라는 강력한 결합을 만들어냈고,  
결과적으로 **사용성과 완성도가 높은 Netflix 분석 프로젝트**를 완성했습니다.

팀원 모두에게 의미 있는 경험이었고,  
향후 웹 기반 데이터 분석 프로젝트를 진행하는 데 중요한 기반이 되는 프로젝트가 되었습니다.



<br>
<span style="font-size:28px;">🙌 Author</span>
지승 송 (jiseung597)
프로젝트 관련 문의는 Issues로 남겨주세요.
