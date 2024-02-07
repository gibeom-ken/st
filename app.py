import streamlit as st 
import streamlit.components.v1 as stc 
import pandas as pd 
import pygwalker as pyg 
import seaborn as sns
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Partner Data Solution팀 솔루션 매출 ",
    page_icon=":bar_chart:",
    layout="wide",
)
st.subheader("엑셀")


# Load Data Fxn
def load_data(data):
    return pd.read_excel(data)

def main():
    st.title("Partner Data Solution팀 솔루션 매출 현황판")
    st.subheader("Nimo에서 다운받은 파일을 업로드해주세요.")
    # Form
    with st.form("upload_form"):
        data_file = st.file_uploader("엑셀 파일만 업로드해주세요!") #,type=["xlsx","txt"]
        submitted = st.form_submit_button("Submit")

    if submitted:
        df = load_data(data_file)
        df = df[df['솔루션명'].isin(['상품명마스터','상품진단 솔루션', 'API데이터솔루션(통계)', '거래 Quick 모니터링', '유입 Quick 모니터링', '트렌드 Quick 모니터링'])].sort_values('기준일')
        KPI_df = pd.DataFrame({'솔루션명':['상품명마스터', '상품진단 솔루션', 'API데이터솔루션(통계)', '거래 Quick 모니터링', '유입 Quick 모니터링', '트렌드 Quick 모니터링'],'KPI':[30000000, 20000000, 10000000, 30000000, 20000000, 10000000]})
        df_merge = pd.merge(left=df, right=KPI_df, how = "inner", on = "솔루션명")
        df_merge['누적 매출'] = round(df_merge.groupby('솔루션명')['발생 매출'].cumsum())
        df_merge['달성률'] = round((df_merge['누적 매출'] / df_merge['KPI'])*100,1)
        df_merge = df_merge[['솔루션명', '기준일', '발생 매출', '기간 매출', '완료 매출', '누적 매출', '달성률']]


        
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["전체", "상품명마스터", "상품진단 솔루션", 'API데이터솔루션(통계)', '거래 Quick 모니터링', '유입 Quick 모니터링', '트렌드 Quick 모니터링'])

        with tab1:
            st.markdown("일별 매출")
            st.bar_chart(data=df_merge, x='기준일', y='발생 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("누적 매출")
            st.bar_chart(data=df_merge, x='기준일', y='누적 매출', color=None, width=0, height=0, use_container_width=True)

            st.dataframe(data=df_merge, width=None, height=None, use_container_width=True, hide_index=True, column_order=None, column_config=None)

        with tab2:
            st.markdown("일별 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '상품명마스터'], x='기준일', y='발생 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("누적 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '상품명마스터'], x='기준일', y='누적 매출', color=None, width=0, height=0, use_container_width=True)
        
            st.markdown("KPI 달성률")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '상품명마스터'], x='기준일', y='달성률', color=None, width=0, height=0, use_container_width=True)

            st.dataframe(data=df_merge[df_merge['솔루션명'] == '상품명마스터'], width=None, height=None, use_container_width=True, hide_index=True, column_order=None, column_config=None)
        
        with tab3:
            st.markdown("일별 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '상품진단 솔루션'], x='기준일', y='발생 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("누적 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '상품진단 솔루션'], x='기준일', y='누적 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("KPI 달성률")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '상품진단 솔루션'], x='기준일', y='달성률', color=None, width=0, height=0, use_container_width=True)

            st.dataframe(data=df_merge[df_merge['솔루션명'] == '상품진단 솔루션'], width=None, height=None, use_container_width=True, hide_index=True, column_order=None, column_config=None)

        with tab4:
            st.markdown("일별 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == 'API데이터솔루션(통계)'], x='기준일', y='발생 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("누적 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == 'API데이터솔루션(통계)'], x='기준일', y='누적 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("KPI 달성률")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == 'API데이터솔루션(통계)'], x='기준일', y='달성률', color=None, width=0, height=0, use_container_width=True)

            st.dataframe(data=df_merge[df_merge['솔루션명'] == 'API데이터솔루션(통계)'], width=None, height=None, use_container_width=True, hide_index=True, column_order=None, column_config=None)    

        with tab5:
            st.markdown("일별 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '거래 Quick 모니터링'], x='기준일', y='발생 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("누적 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '거래 Quick 모니터링'], x='기준일', y='누적 매출', color=None, width=0, height=0, use_container_width=True)
        
            st.markdown("KPI 달성률")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '거래 Quick 모니터링'], x='기준일', y='달성률', color=None, width=0, height=0, use_container_width=True)

            st.dataframe(data=df_merge[df_merge['솔루션명'] == '거래 Quick 모니터링'], width=None, height=None, use_container_width=True, hide_index=True, column_order=None, column_config=None)
        
        with tab6:
            st.markdown("일별 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '유입 Quick 모니터링'], x='기준일', y='발생 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("누적 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '유입 Quick 모니터링'], x='기준일', y='누적 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("KPI 달성률")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '유입 Quick 모니터링'], x='기준일', y='달성률', color=None, width=0, height=0, use_container_width=True)

            st.dataframe(data=df_merge[df_merge['솔루션명'] == '유입 Quick 모니터링'], width=None, height=None, use_container_width=True, hide_index=True, column_order=None, column_config=None)

        with tab7:
            st.markdown("일별 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '트렌드 Quick 모니터링'], x='기준일', y='발생 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("누적 매출")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '트렌드 Quick 모니터링'], x='기준일', y='누적 매출', color=None, width=0, height=0, use_container_width=True)

            st.markdown("KPI 달성률")
            st.bar_chart(data=df_merge[df_merge['솔루션명'] == '트렌드 Quick 모니터링'], x='기준일', y='달성률', color=None, width=0, height=0, use_container_width=True)

            st.dataframe(data=df_merge[df_merge['솔루션명'] == '트렌드 Quick 모니터링'], width=None, height=None, use_container_width=True, hide_index=True, column_order=None, column_config=None)    
        

        


        # Visualize
        #pyg_html = pyg.walk(df_merge,return_html=True)
        # Render with components
        #stc.html(pyg_html,scrolling=True,height=1000)

    
        
    
if __name__ == "__main__":
    main()

