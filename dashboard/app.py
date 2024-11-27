import pandas as pd
from shiny.express import input, ui
from shiny import render
df = pd.read_csv("Premier League Player Stats.csv")

ui.page_opts()
@render.data_frame  
def stats_df():
    return render.DataGrid(df) 
