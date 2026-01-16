import streamlit as st
from datetime import datetime
import time

# 1. 페이지 설정
st.set_page_config(page_title="오늘의 점심 & 오후 루틴", page_icon="🍴")

# 2. 시간 설정
now = datetime.now()
today_date = now.strftime('%Y-%m-%d')
current_hour = now.hour

# 3. 목표 시간 정의
lunch_start = now.replace(hour=13, minute=0, second=0, microsecond=0)
afternoon_start = now.replace(hour=14, minute=0, second=0, microsecond=0)

# 4. 제목 및 날짜
st.title("🍴 오늘의 점심 & 오후 가이드")
st.subheader(f"오늘의 메뉴는 무엇인가요? ({today_date})")
st.write("---")

# 5. 시간대별 동적 메시지 (요청 반영)
message_placeholder = st.empty()

if now < lunch_start:
    # [1단계] 오후 1시 전: 카운트다운 표시
    remaining = lunch_start - now
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    message_placeholder.metric(
        label="⏰ 점심시간(13:00)까지 남은 시간", 
        value=f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    )

elif lunch_start <= now < afternoon_start:
    # [2단계] 오후 1시 ~ 2시 사이: 점심 식사 문구 표시
    message_placeholder.success("🎉 즐거운 점심시간입니다! 맛있게 드세요!")

else:
    # [3단계] 오후 2시 이후: 오후 화이팅 문구 표시 (점심 문구는 자동 제거됨)
    message_placeholder.info("☕️ 나른한 오후네요! 커피 한 잔과 함께 남은 시간도 화이팅입니다! 💪")

# 6. 식당 정보 (고정 섹션)
st.write("---")
st.markdown("### 📍 오늘 선정한 식당 정보")
naver_map_url = "https://naver.me/GKUJawFB"
st.link_button("👉 네이버 지도로 보기", naver_map_url, use_container_width=True)

st.caption("이 페이지는 매일 00시에 날짜가 자동 업데이트됩니다.")
