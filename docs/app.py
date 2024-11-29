import pandas as pd
from shiny.express import input, ui
from shiny import render, reactive, req
from shinywidgets import render_widget  
import plotly.express as px
from shinyswatch import theme
from faicons import icon_svg

df = pd.read_csv("premier-player-23-24.csv")
stats_df = df[["Player", "Pos", "Age", "MP", "Gls", "Ast", "Team"]]
goal_range = [float(df["Gls"].min()),float(df["Gls"].max())]
players = stats_df["Player"].tolist()

ui.page_opts(title="⚽ Premier League Player Stats 2023-24",window_title="Jeremy's Interactive App", fillable=True, theme=theme.darkly)
with ui.sidebar(position="left", open="open", bg="f8f8f8"):
    ui.h2("Compare Players", style="text-align: center;", bg="#0a0a0a")
    
    ui.input_select(  
    "select_player",  
    "Select a Player:",  
    choices=players,
    multiple=True,
    selectize=True
    )


    ui.input_radio_buttons(
        "select_stat",
        "Select Stat",
        choices={"Gls": "Goals","Ast": "Assists", "MP": "Matches Played"},
        selected=None
    )


    ui.input_action_button("reset_button", "Reset")  

with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Player Table", style="text-align: center;")

        @render.data_frame  
        def stats_table():
            return render.DataGrid(filtered_data()) 

with ui.card(full_screen=True):
        ui.card_header("Player Comparison", style="text-align: center;")

        @render_widget
        def plotly_bar():
            stat=input.select_stat()
            compare_df= filtered_data()
            chart = px.bar(
                compare_df, x=stat, y="Player", orientation='h', hover_data=input.select_stat()
            ).update_layout(
                xaxis_title=f"{stat}",
                yaxis_title="Player",
            )
            chart.update_traces(hovertemplate='</b> %{y}<br></b> %{x}<br><b>')


            return chart


@reactive.calc
def filtered_data():
    req(input.select_player())
    isPlayerMatch = stats_df["Player"].isin(input.select_player())
    selectStat = stats_df[input.select_stat()]
    return stats_df[isPlayerMatch & selectStat]

@reactive.effect
@reactive.event(input.reset_button)
def reset():
    ui.update_select("select_player", selected=[])