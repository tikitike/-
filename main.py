import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="화재 통계 분석", layout="wide")

st.title("🔥 전국/지역별 연도별 화재 통계 분석 대시보드")

# 1. 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("fire_data.csv")  # CSV 경로
    return df

df = load_data()

# 2. 필터링 옵션
years = sorted(df['연도'].unique())
regions = ['전국'] + sorted(df['지역'].unique())

col1, col2 = st.columns(2)
with col1:
    selected_years = st.multiselect("연도 선택", years, default=years)
with col2:
    selected_region = st.selectbox("지역 선택", regions)

# 3. 필터 적용
filtered_df = df[df['연도'].isin(selected_years)]
if selected_region != '전국':
    filtered_df = filtered_df[filtered_df['지역'] == selected_region]

# 4. 통계 요약
total_cases = filtered_df['발생건수'].sum()
total_deaths = filtered_df['사망자수'].sum()
total_injured = filtered_df['부상자수'].sum()
total_loss = filtered_df['재산피해액'].sum()

st.subheader("📊 통계 요약")
st.metric("총 화재 발생건수", f"{total_cases:,} 건")
st.metric("총 사망자 수", f"{total_deaths:,} 명")
st.metric("총 부상자 수", f"{total_injured:,} 명")
st.metric("총 재산 피해액", f"{total_loss:,} 원")

# 5. 연도별 발생 건수 시각화
st.subheader("📈 연도별 화재 발생 추이")
fig = px.line(filtered_df.groupby('연도')['발생건수'].sum().reset_index(),
              x='연도', y='발생건수', markers=True, title='연도별 화재 발생건수')
st.plotly_chart(fig, use_container_width=True)

# 6. 원인별 비율
st.subheader("🔥 주요 원인별 비율")
cause_fig = px.pie(filtered_df, names='주요원인', title='화재 주요 원인 비율')
st.plotly_chart(cause_fig, use_container_width=True)

# 7. 지역별 분포 (전국일 때만)
if selected_region == '전국':
    st.subheader("📍 지역별 화재 건수")
    region_fig = px.bar(df[df['연도'].isin(selected_years)].groupby('지역')['발생건수'].sum().reset_index(),
                        x='지역', y='발생건수', title='지역별 화재 발생 건수')
    st.plotly_chart(region_fig, use_container_width=True)

