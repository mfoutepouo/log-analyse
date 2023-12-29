import streamlit as st
import os
import sys
from st_aggrid import GridOptionsBuilder, AgGrid
import pandas as pd

# path of actual script
actual = os.path.dirname(os.path.abspath(__file__))
# path to config
config_path = os.path.join(actual)
sys.path.append(config_path)
# # import config
from cfg import config as cfg
import functions as fn




st.set_page_config(
    page_title="Log Analyze",
    page_icon=":file:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        # 'Get Help': 'https://www.linkedin.com/in/ars%C3%A8ne-bakandakan/',
        # 'About': "# cool app! Made with 💖"
    }
)

# logo

c1,c2,c3 = st.columns([1,1,1])
with c1:
    pass
with c2:
    st.image("assets/img/logo.jpeg",width=300)
    st.title("Log Analyzer")   
with c3:
    pass

 

# step 1
n , hea = st.columns([0.05,0.95])
n = n.warning("1")
hea = hea.header("Load the log file")

log_type = st.empty()
log_type = log_type.selectbox(
            "Log Type",
            options=["Web","Network","System"], 
            index=None,
            placeholder="Select the log type...",
            help="Type of Log you want to process"
        )

st.divider()


if log_type == "Web":
    data = cfg.web_csv_content
    fn.log_analyzer(data,log_type)
elif log_type == "Network":
    data = cfg.netw_csv_content
    fn.log_analyzer(data,log_type)
elif log_type == "System":
    data = cfg.sys_csv_content
    fn.log_analyzer(data,log_type)  
            
    st.divider()   







