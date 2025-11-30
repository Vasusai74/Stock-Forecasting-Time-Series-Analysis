import streamlit as st

from streamlit_option_menu import option_menu

import Trading_App
import CAPM_return
import CAPM_Beta
import Stock_Analysis
import Stock_Prediction


st.set_page_config(page_title='CAPM',
                   page_icon='chart_with_upwards_trend',
                   layout='wide')


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='CAPM',
                options=['Trading App', 'CAPM Return', 'CAPM Beta',
                         'Stock Analysis', 'Stock Prediction'],
                menu_icon='chart-text-fill',
                default_index=0,
                # styles=
            )

        if app == 'Trading App':
            Trading_App.app()
        if app == 'CAPM Return':
            CAPM_return.app()
        if app == 'CAPM Beta':
            CAPM_Beta.app()
        if app == 'Stock Analysis':
            Stock_Analysis.app()
        if app == 'Stock Prediction':
            Stock_Prediction.app()


if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
