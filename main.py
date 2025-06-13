import streamlit as st
import math

st.set_page_config(page_title="예상 대피 시간 계산기", layout="centered")
st.title("🚪 건물 대피 시간 예측 도구")

st.markdown("인원 수, 출입구 수, 복도 길이 등을 입력하면 예상 대피 시간을 계산해드립니다.")

# 입력 받기
num_people = st.number_input("인원 수", min_value=1, max_value=10000, value=100)
num_exits = st.number_input("출입구 수", min_value=1, max_value=20, value=2)
corridor_length = st.number_input("복도 길이 (m)", min_value=1.0, max_value=500.0, value=30.0)
corridor_width = st.number_input("복도 폭 (m)", min_value=0.5, max_value=10.0, value=2.0)

# 기준 값
walking_speed = 1.2  # 평균 보행 속도 (m/s)
exit_flow_rate = 1.3  # 출입구 1개당 통과 인원 수 (명/초)

# 계산
corridor_time = corridor_length / walking_speed  # 복도 통과 시간 (초)
exit_time = num_people / (num_exits * exit_flow_rate)  # 출입구 통과 시간 (초)

total_time_sec = corridor_time + exit_time
total_time_min = total_time_sec / 60

# 출력
st.subheader("⏱ 예상 대피 시간:")
st.markdown(f"**{total_time_sec:.1f} 초**  (~ {total_time_min:.1f} 분)")

# 위험 레벨 표시
if total_time_min < 2:
    st.success("대피 시간 양호 ✅")
elif total_time_min < 5:
    st.warning("주의: 대피 시간이 다소 깁니다 ⚠️")
else:
    st.error("위험: 대피 시간이 너무 깁니다 ❗")

# 참고 정보
with st.expander("📘 참고 기준 보기"):
    st.markdown("""
    - 평균 보행 속도: **1.2 m/s**
    - 출입구 1개당 통과 속도: **1.3명/초**
    - 실제 대피 시간은 혼잡도, 시야 확보, 장애물 여부에 따라 달라질 수 있습니다.
    """)



