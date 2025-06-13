import streamlit as st
import matplotlib.pyplot as plt

st.title("건물 화재 위험도 예측")

# 사용자 입력
floors = st.number_input("층수 입력 (층)", min_value=1, max_value=100, value=5)
material = st.selectbox("건물 재질 선택", ["목재", "철근 콘크리트", "강철", "복합재"])
area = st.number_input("건물 면적 입력 (제곱미터)", min_value=10, max_value=10000, value=500)

# 화재 위험도 계산 (예시)
# 층수가 많고, 면적이 크고, 재질이 가연성일수록 위험도가 높다고 가정

material_risk_map = {
    "목재": 0.9,
    "철근 콘크리트": 0.3,
    "강철": 0.5,
    "복합재": 0.7
}

base_risk = 0.1
risk = base_risk + (floors * 0.05) + (area / 10000) + material_risk_map[material]
risk = min(risk, 1.0)  # 위험도는 최대 1.0으로 제한

# 위험도 출력
st.write(f"예상 화재 위험도: {risk*100:.1f}%")

# 시각화: 위험도 원형 그래프
labels = ['화재 위험도', '안전도']
sizes = [risk, 1-risk]
colors = ['red', 'green']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')

st.pyplot(fig)
