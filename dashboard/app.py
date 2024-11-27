import pandas as pd
from shiny.express import input, ui
from shiny import render


df = pd.read_csv("Premier League Player Stats.csv")

ui.page_opts()
with ui.sidebar():
    ui.input_select(  
    "select_team",  
    "Select a Team:",  
    {"1A": "Choice 1A", "1B": "Choice 1B", "1C": "Choice 1C"},  
)
    ui.input_slider("goals", "Goals Scored", min=1, max=100, value=5)



@render.data_frame  
def stats_df():
    return render.DataGrid(df) 
