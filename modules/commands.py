from . import send, functions

@functions.command
def bots():
    """.bots - report info about bot"""
    send("Reporting in! [Python3]")
    
@functions.command
def source():
    """.source - show's the bot's source"""
    send("You can find my source here: https://github.com/MrW24/JiyuuBot")
