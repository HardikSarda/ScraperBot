#This is the main file to be executed in orde for the scraper to funtion

from process.process import Process

with Process(teardown = False) as bot:
    # bot.land_first_page()
    bot.signin_button()
    # bot.search_box()
    # bot.apply_filtration()
