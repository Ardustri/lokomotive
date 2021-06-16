from colorama import Fore, Style, init

init(autoreset=True)

def out(message):
    """
    standard out
    """
    print(message)

def info(message):
    """
    out info message in blue
    """
    out(f"{Style.BRIGHT}{Fore.BLUE}{message}")

def warning(message):
    """
    out warning message in blue
    """
    out(f"{Style.BRIGHT}{Fore.YELLOW}{message}")

def error(message):
    """
    out error message in blue
    """
    out(f"{Style.BRIGHT}{Fore.RED}{message}")

def succeed(message):
    """
    out success message in blue
    """
    out(f"{Style.BRIGHT}{Fore.GREEN}{message}")
