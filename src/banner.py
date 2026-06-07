import os

def show_banner():
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    GRAY = "\033[90m"
    RESET = "\033[0m"

    banner_text = CYAN + r"""
 _   _    _    ____  _   _   ___ ____  _____ _   _ _____ ___ _____ ___ _____ ____
| | | |  / \  / ___|| | | | |_ _|  _ \| ____| \ | |_   _|_ _|  ___|_ _| ____|  _ \
| |_| | / _ \ \___ \| |_| |  | || | | |  _| |  \| | | |  | || |_   | ||  _| | |_) |
|  _  |/ ___ \ ___) |  _  |  | || |_| | |___| |\  | | |  | ||  _|  | || |___|  _ <
|_| |_/_/   \_\____/|_| |_| |___|____/|_____|_| \_| |_| |___|_|   |___|_____|_| \_\
""" + RESET + f"""
     {GRAY}===================================================================={RESET}
     {GREEN}[+] Version: 2.0.0             [+] Project: Hash Identifier{RESET}
     {GREEN}[+] Scope  : Cyber Security    [+] Type   : Hash Classifier{RESET}
     {GRAY}===================================================================={RESET}
    """

    print(banner_text)

def clear_screen():
    """Clears the terminal screen safely across platforms."""
    os.system("cls" if os.name == "nt" else "clear")
