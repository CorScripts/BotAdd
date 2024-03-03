import webbrowser
import os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("BotAdd")

os.system(f"mode 58,11")

while True:
    os.system("cls")
    print("""
    ███████╗  ██████╗ ████████╗ █████╗ ██████╗ ██████╗ 
    ██╔══██╗ ██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
    ███████╔╝██║   ██║   ██║   ███████║██║  ██║██║  ██║
    ██╔══██╗ ██║   ██║   ██║   ██╔══██║██║  ██║██║  ██║
    ███████╔╝╚██████╔╝   ██║   ██║  ██║██████╔╝██████╔╝
    ╚══════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ 
                    Type 'exit' to exit
       VN COMMUNITY ON TOP - discord.gg/ErFRq9Tcfy""")
    bot_id = input("Enter the Discord bot's ID: ")
    if bot_id == 'exit':
        break

    url = f"https://discordapp.com/oauth2/authorize?scope=bot&client_id={bot_id}"
    webbrowser.open(url)
