from st_aggrid import GridOptionsBuilder, AgGrid

def check_log(df):    
    gb = GridOptionsBuilder.from_dataframe(df)

    # pagination doesnt work
    gb.configure_pagination(paginationPageSize=50)

    gb.configure_grid_options(domLayout='normal')

    # sidebar
    gb.configure_side_bar()

    # height
    # gb.configure_auto_height()

    gb.configure_default_column(floatingFilter=True, selectable=False)

    # Enable multi-row selection
    # gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children")

    gridOptions = gb.build()

    gridtable = AgGrid(
        df,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_on='cellValueChanged',
        fit_columns_on_grid_load=False,
        theme='balham', #theme color for the table
        enable_enterprise_modules=True,
        height=350,
        width='100%',
        reload_data=True
    )

    grid = gridtable['data']
    # selected = grid_response['selected_rows']
    # df = pd.DataFrame(selected)
    return grid