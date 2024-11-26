import pandas as pd
from shiny.express import input, ui
from shiny import render
from shared import app_dir, careers_df, from_start, gp_max, players_dict, stats, to_end
df = pd.read_csv("careers.csv")

ui.page_opts()
@render.data_frame  
def careers_df():
    return render.DataGrid(df) 
