from process.process import Process

with Process(teardown = False) as bot:
    bot.land_first_page()
    bot.signin_button()
