from colorama import Fore, Style

yourName = str(input("What is your name?\n"))
print(Fore.GREEN + f"{yourName} written in green")
print(Style.RESET_ALL)
print("Written in white")