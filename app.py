# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from collections import Counter

st.set_page_config(page_title="Netflix 분석", page_icon="🎬", layout="wide")

@st.cache_data
def load_data(csv_path: str):
    df = pd.read_csv(csv_path)              # UTF-8 CSV
    for c in ["type","title","director","cast","country","rating","listed_in","description"]:
        if c in df.columns:
            df[c] = df[c].fillna("").astype(str).str.strip()
    if "release_year" in df.columns:
        df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
    if "listed_in" in df.columns:
        df["genre_list"] = df["listed_in"].str.split(",").apply(
            lambda xs: [x.strip() for x in xs] if isinstance(xs, list) else [])
    else:
        df["genre_list"] = [[] for _ in range(len(df))]
    return df

DATA_FILE = "netflix_titles.csv"  # app.py와 같은 폴더
if not Path(DATA_FILE).exists():
    st.error(f"'{DATA_FILE}'를 현재 폴더에 두세요.")
    st.stop()

df = load_data(DATA_FILE)
st.title("🎬 Netflix 컨텐츠 분석 대시보드")
st.caption(f"Rows: {len(df):,} | Columns: {len(df.columns)}")

# 사이드바 필터
st.sidebar.header("필터")
q = st.sidebar.text_input("제목 검색(포함)", "")
types = sorted(df["type"].dropna().unique().tolist())
sel_type = st.sidebar.multiselect("작품 유형", options=types, default=types)

years = [int(df["release_year"].min()), int(df["release_year"].max())] if df["release_year"].notna().any() else [1900, 2030]
year_min, year_max = st.sidebar.slider("개봉년도 범위", min_value=years[0], max_value=years[1], value=(years[0], years[1]))

ratings = sorted([r for r in df["rating"].unique().tolist() if r])
sel_ratings = st.sidebar.multiselect("등급(선택)", options=ratings)

genre_counter = Counter([g for lst in df["genre_list"] for g in lst if g])
top_genres = [g for g,_ in genre_counter.most_common(40)]
sel_genres = st.sidebar.multiselect("장르(하나라도 포함)", options=top_genres)

country_q = st.sidebar.text_input("국가(부분일치, 쉼표로 여러개)", "")

# 필터 로직
mask = (
    df["type"].isin(sel_type)
    & df["release_year"].between(year_min, year_max, inclusive="both")
)
if q:
    mask &= df["title"].str.contains(q, case=False, na=False)
if sel_ratings:
    mask &= df["rating"].isin(sel_ratings)
if sel_genres:
    mask &= df["genre_list"].apply(lambda gl: any(g in gl for g in sel_genres))
if country_q:
    wants = [c.strip().lower() for c in country_q.split(",") if c.strip()]
    if wants:
        mask &= df["country"].str.lower().apply(lambda s: any(w in s for w in wants))

filtered = df[mask].copy()

# KPI
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("표시 컨텐츠 수", f"{len(filtered):,}")
with c2: st.metric("년도 범위", f"{year_min}–{year_max}")
with c3: st.metric("유형 수", f"{filtered['type'].nunique()}")
with c4:
    mg = Counter([g for lst in filtered["genre_list"] for g in lst if g]).most_common(1)
    st.metric("최다 장르", mg[0][0] if mg else "-")

st.divider()

# 차트 1: 연도별
if filtered["release_year"].notna().any():
    year_counts = (filtered.dropna(subset=["release_year"])
                            .groupby("release_year", as_index=False)
                            .size()
                            .rename(columns={"size":"count"}))
    st.plotly_chart(px.bar(year_counts, x="release_year", y="count", title="연도별 컨텐츠 수"),
                    use_container_width=True)

# 차트 2: 유형 분포
type_counts = filtered["type"].value_counts().reset_index()
type_counts.columns = ["type", "count"]
st.plotly_chart(px.bar(type_counts, x="type", y="count", title="작품 유형 분포"),
                use_container_width=True)

# 차트 3: 상위 장르
topg = pd.DataFrame(genre_counter.most_common(15), columns=["genre","count"])
if not topg.empty:
    st.plotly_chart(px.bar(topg, x="genre", y="count", title="상위 장르 Top 15"),
                    use_container_width=True)

st.subheader("필터 결과 데이터")
st.dataframe(filtered[["type","title","country","release_year","rating","listed_in","director","cast","description"]],
             use_container_width=True, height=420)

st.download_button("⬇️ 현재 결과 CSV로 다운로드",
                   filtered.to_csv(index=False).encode("utf-8"),
                   file_name="netflix_filtered.csv",
                   mime="text/csv")
