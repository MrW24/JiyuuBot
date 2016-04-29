from . import send, functions

@functions.command
def bots():
    """.bots - report info about bot"""
    send("Reporting in! [Python3]")
    
    from . import send, functions

@functions.command
def source():
    """.source - shows a link to the bot's source"""
    send("Jiyuubot's source can be found here: https://github.com/Bob131/JiyuuBot")
