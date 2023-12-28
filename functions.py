from st_aggrid import GridOptionsBuilder, AgGrid
import streamlit as st
import pandas as pd

# the part used to check the log file data
def check_log(df):    
    gb = GridOptionsBuilder.from_dataframe(df)

    # pagination doesnt work
    gb.configure_pagination(paginationPageSize=50)

    gb.configure_grid_options(domLayout='normal')

    # sidebar
    gb.configure_side_bar()

    # enable sorting, filtering, editable
    gb.configure_default_column(floatingFilter=True, selectable=False ,editable=True)

    gridOptions = gb.build()

    gridtable = AgGrid(
        df,
        gridOptions=gridOptions,
        fit_columns_on_grid_load=False,
        theme='balham', #theme color for the table
        height=350,
        width='100%',
           )

    grid = gridtable['data']
    return grid

# the part used to analyze the log file data
def log_analyzer(data,log_type):
    st.info("Upload a csv or txt file 👇")
    with st.expander("Check a sample of the kind of csv file you should upload"):
    # st.write("Here's a sample of the csv file you should upload")
        st.download_button("Download sample",data=data,file_name=f"{log_type}_sample.csv",mime="text/csv")

        fu,sep = st.columns([0.9,0.1])

        uploaded_file = fu.file_uploader("Choose a local file", type=["csv" , "txt"])
        sep = sep.selectbox(
            "Separator",
            options=[",",";"], 
        )
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file,delimiter=sep, skipinitialspace=True)
            st.write(dataframe)
            n , hea = st.columns([0.05,0.95])
            n = n.warning("2")

            hea = hea.header("Check")
            st.info("Check information of the log file")
            new_df = check_log(dataframe)

            n , hea = st.columns([0.05,0.95])
            n = n.warning("3")

            hea = hea.header("Export")
            st.info("Export the information to csv file")
            if st.button("Export"): 
                st.write(new_df)
                data_as_csv= new_df.to_csv(index=False).encode("utf-8")
                st.download_button("Download the export",data=data_as_csv,file_name="export.csv",mime="text/csv")