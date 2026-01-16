import streamlit as st
from datetime import datetime, timedelta
import time

# 1. 페이지 설정
st.set_page_config(page_title="오늘의 점심 & 오후 루틴", page_icon="🍴")

# --- [중요] 한국 시간(KST) 설정 ---
# 서버(Streamlit Cloud)는 보통 UTC 기준이므로 9시간을 더해줍니다.
now_utc = datetime.utcnow()
now_kst = now_utc + timedelta(hours=9)
today_date = now_kst.strftime('%Y-%m-%d')
current_hour = now_kst.hour

# 2. 목표 시간 정의 (KST 기준)
lunch_start = now_kst.replace(hour=13, minute=0, second=0, microsecond=0)
afternoon_start = now_kst.replace(hour=14, minute=0, second=0, microsecond=0)

# 3. 깜빡이는 효과를 위한 CSS 추가
st.markdown("""
    <style>
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0.3; }
        100% { opacity: 1; }
    }
    .blink-text {
        animation: blink 1s linear infinite;
        color: #FF4B4B;
        font-weight: bold;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. 제목 및 날짜
st.title("🍴 오늘의 점심 & 오후 가이드")
st.subheader(f"오늘의 메뉴는 무엇인가요? ({today_date})")
st.write(f"현재 시간(KST): {now_kst.strftime('%H:%M:%S')}")
st.write("---")

# 5. 시간대별 동적 메시지
message_placeholder = st.empty()

if now_kst < lunch_start:
    # [1단계] 오후 1시 전: 실시간 카운트다운 + 깜빡이 효과
    remaining = lunch_start - now_kst
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # HTML을 사용해 깜빡이는 효과 적용
    message_placeholder.markdown(
        f"""
        <div style="text-align: center;">
            <p>⏰ 점심시간(13:00)까지 남은 시간</p>
            <p class="blink-text">{hours:02d}:{minutes:02d}:{seconds:02d}</p>
        </div>
        """, unsafe_allow_html=True)

elif lunch_start <= now_kst < afternoon_start:
    # [2단계] 오후 1시 ~ 2시 사이: 점심 식사 문구
    message_placeholder.success("🎉 즐거운 점심시간입니다! 맛있게 드세요!")

else:
    # [3단계] 오후 2시 이후: 오후 화이팅 문구
    message_placeholder.info("☕️ 나른한 오후네요! 커피 한 잔과 함께 남은 시간도 화이팅입니다! 💪")

# 6. 식당 정보
st.write("---")
st.markdown("### 📍 오늘 선정한 식당 정보")
naver_map_url = "https://naver.me/GKUJawFB"
st.link_button("👉 네이버 지도로 보기", naver_map_url, use_container_width=True)

# 7. 실시간 업데이트 (1초마다 새로고침)
time.sleep(1)
st.rerun()
