<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" width="330">
</p>

<h1 align="center" style="font-size:36px;">
  Netflix 콘텐츠 데이터 분석 프로젝트
</h1>

---

## 📌 1. 데이터 분석 프로젝트 설명

본 프로젝트는 **Netflix의 공개 데이터셋(netflix_titles.csv)**을 활용하여  
콘텐츠의 **장르, 국가, 연도, 시청등급, 유형(Movie/TV Show)** 등을 분석하고  
사용자가 직접 필터링하며 데이터를 탐색할 수 있는  
**인터랙티브 대시보드**를 개발한 데이터 분석 프로젝트입니다.

Python의 Pandas/Plotly를 사용해 데이터를 시각화했고,  
Streamlit을 통해 웹 기반으로 분석 사이트를 제작했습니다.

---

## 📌 2. 주제

**“Netflix 콘텐츠의 전반적인 구조와 트렌드를 시각적으로 분석하는 대시보드 제작”**

---

## 📌 3. 주제 선택 이유

- Netflix는 전 세계적으로 가장 많은 사용자를 보유한 스트리밍 서비스이며  
  매년 수많은 영화 및 시리즈가 추가되는 **방대한 데이터 구조**를 가지고 있음.
- CSV 파일만으로는 전체적인 트렌드를 한눈에 파악하기 어려워  
  **시각화 기반 분석 도구**가 필요하다고 판단함.
- 데이터 분석(전처리 · 시각화)과 대시보드 구현(Streamlit)을  
  하나의 프로젝트에서 모두 경험해보고 싶었음.
- 사용자가 직접 필터링하며 데이터를 탐색할 수 있는  
  **실제 서비스형 인터랙티브 분석 사이트**를 만드는 데 의미가 있었기 때문.

---

## 📌 4. 데이터 분석 내용

### 🔍 (1) 데이터 전처리
- 결측치 처리 및 공백 제거
- 문자열 컬럼 정리(type, cast, director 등)
- release_year 숫자 변환
- listed_in(장르) → genre_list 리스트 변환

### 📊 (2) 시각화 분석
- **연도별 콘텐츠 수 변화**
- **Movie vs TV Show 비율**
- **상위 장르 Top 15 분석**
- **국가별 콘텐츠 분포**
- **시청등급(Rating) 분포**

### 🎛 (3) 필터 기능 구현
- 제목 검색(부분 일치)
- 유형 선택(Movie / TV Show)
- 국가 검색(쉼표로 여러 개 가능)
- 제작 연도 범위 슬라이더
- 장르 다중 선택
- 시청 등급 선택

### 📥 (4) 부가 기능
- 필터링된 결과를 **CSV로 다운로드**
- 실시간 대시보드 업데이트

---

## 📌 5. 시연 동영상 (YouTube)

👉 **시연 영상 링크:**  
`https://www.youtube.com/여기에_넣기`

(※ 영상 업로드 후 실제 링크로 교체하세요!)

---

## 📌 6. 팀원 소개 (덤앤더머 팀)

| 이름 | 역할 | 담당 업무 |
|------|------|-----------|
| **송지승** | 팀장 / 대시보드 개발 | Streamlit UI 제작, 필터 로직 구현, Plotly 시각화, README 작성 |
| **신준수** | 데이터 엔지니어 | CSV 데이터 전처리, genre/rating 처리 로직, Panda 최적화, 오류 처리 |

---

## 📌 팀원 개인 회고

### 🙋‍♂️ 송지승 – 느낀 점
- 처음으로 Streamlit을 이용해 실제 분석 대시보드를 만들어보며  
  데이터 분석이 단순한 그래프 그리기를 넘어서  
  **사용자가 상호작용할 수 있는 서비스형 분석 도구**로 확장된다는 점을 배웠다.
- 필터링 로직과 차트 연동 과정에서 많은 오류를 겪었지만  
  문제 해결 능력이 크게 향상됐다고 느꼈다.

### 🙋‍♂️ 신준수 – 느낀 점
- 데이터 전처리의 중요성을 다시 깨달았다.  
  눈에 안 띄는 공백, 결측치, 타입 오류 등이 필터링에 큰 문제를 일으킬 수 있다는 것을 경험했다.
- 팀 프로젝트를 통해 협업의 중요성과 역할 분배의 필요성을 배웠다.

---

## 📌 7. 외부 URL (Streamlit Cloud)

👉 **실행 사이트 링크:**  
https://netflixdataanalyze-kdq2dqf2yqkrcomf46pjrz.streamlit.app/

---

## <span style="font-size:26px;">📌 8. 코드 저장소 (GitHub) / 코드 Push</span>

이 프로젝트의 전체 코드는 GitHub Repository에 저장되어 있으며  
다음 명령어를 통해 push되었습니다:

<pre><code>
git add .
git commit -m "Initial commit: Netflix dashboard project"
git push origin main
</code></pre>

---

## <span style="font-size:26px;">📌 9. 전체 프로젝트 구조</span>

<pre><code>
📦 netflix_data_analyze
 ┣ 📄 app.py
 ┣ 📄 netflix_titles.csv
 ┣ 📄 README.md
 ┗ 📄 requirements.txt (optional)
</code></pre>

---

## <span style="font-size:26px;">📌 10. 사용 기술</span>

- Python 3.x  
- Streamlit  
- Pandas  
- Plotly Express  
- Collections.Counter  
- Pathlib

