import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="건물 화재 위험도 예측", layout="centered")
st.title("🏢 건물 화재 위험도 예측기")

st.markdown("건물의 기본 구조 정보를 입력하면, 예상 화재 위험도를 계산해 드립니다.")

# 사용자 입력
floors = st.number_input("층수", min_value=1, max_value=100, value=5)
material = st.selectbox("건물 재질", ["목재", "철근 콘크리트", "강철", "복합재"])
area = st.number_input("건물 면적 (㎡)", min_value=10.0, max_value=10000.0, value=500.0)

# 화재 위험도 계산 로직 (간단한 가중치 기반 예측)
material_risk = {
    "목재": 0.6,
    "복합재": 0.4,
    "강철": 0.3,
    "철근 콘크리트": 0.2
}

risk_score = (
    (floors * 0.02) +          # 층수당 2% 위험도 증가
    (area / 10000) +           # 면적에 따른 증가 (10000㎡ 이상 시 +1.0)
    material_risk[material]    # 재질별 위험 가중치
)

# 0~100%로 환산
risk_percent = min(round(risk_score * 100, 1), 100.0)

st.subheader("🔥 예상 화재 위험도:")
st.markdown(f"**{risk_percent}%**")

# 시각화 (게이지 차트)
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=risk_percent,
    title={'text': "화재 위험도 (%)"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "red"},
        'steps': [
            {'range': [0, 30], 'color': "lightgreen"},
            {'range': [30, 70], 'color': "yellow"},
            {'range': [70, 100], 'color': "orangered"}
        ]
    }
))
st.plotly_chart(fig)

# 추가 설명
if risk_percent >= 70:
    st.warning("⚠️ 매우 높은 화재 위험! 안전 점검이 필요합니다.")
elif risk_percent >= 40:
    st.info("주의: 중간 이상의 화재 위험이 있습니다.")
else:
    st.success("안전 수준이 양호합니다.")
