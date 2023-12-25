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
    st.image("assets/img/logo.png",width=300)
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
    st.info("Upload a csv or txt file 👇")
    with st.expander("Check a sample of the kind of csv file you should upload"):
    # st.write("Here's a sample of the csv file you should upload")
        st.download_button("Download sample",data=cfg.csv_content,file_name="sample.csv",mime="text/csv")

        uploaded_file = st.file_uploader("Choose a local file", type=["csv" , "txt"])
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
            # st.dataframe(
            #     dataframe,
            # #     column_config={
            # #         "Adresse IP": "Adresse IP",
            # #         "Vide":"Vide",
            # #         "Qui":"Qui",
            # #         "Quand":"Quand",
            # #         "Quoi":"Quoi",
            # #         "Ok":"Ok",
            # #         "Combien ?":"Combien ?",
            # #         "D’où ?":"D’où ?",
            # #         "Comment ?":"Comment ?"
            # # },
            # use_container_width=True
            # ,)
            n , hea = st.columns([0.05,0.95])
            n = n.warning("2")

            hea = hea.header("Check")
            st.info("Check information of the log file")
            new_df = fn.check_log(dataframe)

            n , hea = st.columns([0.05,0.95])
            n = n.warning("3")

            hea = hea.header("Export")
            st.info("Export the information to csv file")
            if st.button("Export"): 
                data_as_csv= new_df.to_csv(index=False).encode("utf-8")
                st.download_button("Download the export",data=data_as_csv,file_name="export.csv",mime="text/csv")



    st.divider()   

# with st.expander("Enter a card number, a month and a year and the number of results you want to extrapolate"):

#     number , result , month , year = st.columns([1,1,1,1])
#     number = number.text_input("Enter a card number",help="Enter a card number")
#     month = month.selectbox(
#             "Month",
#             options=range(1, 13), 
#             help="Month"
#         )
#     year = year.selectbox(
#             "Year",
#             options=range(23, 63), 
#             help="Year"
#         )
#     result = result.selectbox(label="number of results",options = [5,10,15,20],help="number of results")


#     if st.button("Extrapolate"):
#         # convert list to dataframe
#         dataframe = pd.DataFrame(data=fn.dk_extrapolator(number, result), columns=["numero"])

#         # adding month and year
#         dataframe["mois"] = month
#         dataframe["annee"] = year
#         st.table(dataframe)







