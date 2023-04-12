
import streamlit as st
from datetime import datetime, timedelta, date

# 보고서 제목
st.title('공모회사채 발행시장 현황')

# 날짜 선택
start_date = st.date_input('시작일', value=date.today()- timedelta(days=1), max_value = date.today()- timedelta(days=1))
max_date = min(start_date+timedelta(days=3), date.today()- timedelta(days=1))
end_date = st.date_input('종료일', value=start_date, min_value = start_date, max_value = max_date)
#st.write(datetime.strftime(aa,'%Y%m%d'))
