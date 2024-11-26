import pandas as pd
from shiny.express import input, ui
from shiny import render
df = pd.read_csv("careers.csv")

ui.page_opts()
@render.data_frame  
def careers_df():
    return render.DataGrid(df) 