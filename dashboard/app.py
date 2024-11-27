import pandas as pd
from shiny.express import input, ui
from shiny import render, reactive


df = pd.read_csv("premier-player-23-24.csv")
stats_df = df[["Player", "Pos", "Age", "MP", "Gls", "Ast", "Team"]]
goal_range = [float(df["Gls"].min()),float(df["Gls"].max())]


ui.page_opts(title="Premier League Player Stats 2023-24", fillable=True)
with ui.sidebar(position="left", open="open", bg="f8f8f8"):
    ui.h2("Sidebar", style="text-align: center;", bg="#0a0a0a")
    ui.input_select(  
    "select_team",  
    "Select a Team:",  
    choices=['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton',
       'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham',
       'Liverpool', 'Luton Town', 'Manchester City', 'Manchester United', 'Newcastle United',
       "Nottingham Forest", 'Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton'],
       selected="Chelsea",
       multiple=True,
        selectize=True
)
    
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Player Table", style="text-align: center;")

        @render.data_frame  
        def stats_table():
            return render.DataGrid(filtered_data()) 


@reactive.calc
def filtered_data():
    isTeamMatch= stats_df["Team"].isin(input.select_team())
    return stats_df[isTeamMatch]
