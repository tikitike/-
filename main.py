import streamlit as st

st.title("맞춤형 다이어트 추천")

# 이름 입력 받기
name = st.text_input("이름을 입력하세요:")

def recommend_diet(name):
    # 간단하게 이름에 따라 다이어트 방법 추천
    # 여기서는 이름 첫 글자에 따라 다르게 추천
    if not name:
        return "이름을 입력해주세요!"
    first_char = name[0].lower()
    if first_char in "abc":
        return f"{name}님, 저탄수화물 다이어트를 추천합니다!"
    elif first_char in "def":
        return f"{name}님, 간헐적 단식 다이어트를 추천합니다!"
    elif first_char in "ghi":
        return f"{name}님, 지중해식 다이어트를 추천합니다!"
    else:
        return f"{name}님, 꾸준한 유산소 운동과 균형 잡힌 식단을 추천합니다!"

if name:
    result = recommend_diet(name)
    st.write(result)
