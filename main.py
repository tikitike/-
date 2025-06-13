import streamlit as st
import matplotlib.pyplot as plt

st.title("건물 화재 위험도 예측")

# 사용자 입력
floors = st.number_input("층수 입력 (층)", min_value=1, max_value=100, value=5)
material = st.selectbox("건물 재질 선택", ["목재", "철근 콘크리트", "강철", "복합재"])
area = st.number_input("건물 면적 입력 (제곱미터)", min_value=10, max_value=10000, value=500)

# 화재 위험도 계산 (예시)
#
