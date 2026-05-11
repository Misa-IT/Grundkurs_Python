# ==================================================================================
#  COOLT EXEMPEL — "Johans Café"
# ==================================================================================
#  Det här exemplet visar vad man kan bygga med Python när man har lärt sig mer.
#  Du behöver INTE förstå koden nu! Syftet är bara att visa vad som är möjligt.
#
#  DISCLAIMER: Jag (Johan) är jättedålig på de visuella bitarna och har därmed
#  använt AI för att göra färger och ASCII-konsten korrekt.
#
#  Koncepten som används här kommer vi att gå igenom steg för steg under kursen:
#    - Variabler och datatyper      (Lektion 02)
#    - if/elif/else                 (Lektion 03)
#    - Loopar (while, for)          (Lektion 04)
#    - Funktioner                   (Lektion 06)
#    - Dictionaries                 (Lektion 08)
#    - Klasser                      (Lektion 08)
#
#  Kör programmet och testa att beställa kaffe! ☕
# ==================================================================================

import time
import random
import os


# --- Färger för terminalen (ANSI-koder) ---

class Color:
    """Färgkoder som gör texten snyggare i terminalen."""
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


# --- Meny med drycker och priser ---

MENU = {
    "1": {"namn": "Kaffe", "pris": 30, "emoji": "☕"},
    "2": {"namn": "Latte", "pris": 45, "emoji": "🥛"},
    "3": {"namn": "Cappuccino", "pris": 45, "emoji": "☕"},
    "4": {"namn": "Te", "pris": 25, "emoji": "🍵"},
    "5": {"namn": "Varm choklad", "pris": 40, "emoji": "🍫"},
}

# --- "Roliga" citat som visas slumpmässigt ---

QUOTES = [
    "Kaffe är en kram i en mugg.",
    "Livet är för kort för dåligt kaffe.",
    "Men först... kaffe.",
    "Programmering = kaffe → kod → repeat.",
    "En dag utan kaffe är... skämt, jag vet inte.",
]


# --- Funktioner ---

def clear_screen():
    """Rensar terminalskärmen."""
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.03):
    """Skriver ut text tecken för tecken, som en skrivmaskin."""
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def print_cafe_logo():
    """Skriver ut kaféts logotyp med ASCII-konst och färger."""
    logo = f"""
{Color.YELLOW}{Color.BOLD}
        ) ) )
       ( ( (
        ) ) )
     .-------.
     |       |]
     \\       /
      `-----'{Color.RESET}

{Color.CYAN}{Color.BOLD}  ╔════════════════════════════════╗
  ║      ☕  JOHANS CAFÉ   ☕      ║
  ╚════════════════════════════════╝{Color.RESET}
"""
    print(logo)


def show_menu():
    """Visar menyn med alla drycker och priser."""
    print(f"\n{Color.BOLD}  ┌────────────────────────────────┐{Color.RESET}")
    print(f"{Color.BOLD}  │              MENY              │{Color.RESET}")
    print(f"{Color.BOLD}  ├────────────────────────────────┤{Color.RESET}")

    for number, item in MENU.items():
        name = item["namn"]
        price = item["pris"]
        emoji = item["emoji"]
        print(f"  │  {Color.GREEN}{number}.{Color.RESET} {emoji} {name:<15} {Color.YELLOW}{price:>2} kr{Color.RESET}   │")

    print(f"{Color.BOLD}  ├────────────────────────────────┤{Color.RESET}")
    print(f"  │  {Color.RED}0.{Color.RESET} 🚪 Betala och gå           │")
    print(f"{Color.BOLD}  └────────────────────────────────┘{Color.RESET}")


def print_receipt(order_list, customer_name):
    """Skriver ut ett snyggt kvitto."""
    total_price = sum(MENU[item]["pris"] for item in order_list)

    print(f"\n{Color.CYAN}{Color.BOLD}")
    print("  ╔════════════════════════════════╗")
    print("  ║             KVITTO             ║")
    print("  ╠════════════════════════════════╣")
    print(f"  ║  Kund: {customer_name:<22}  ║")
    print("  ╠════════════════════════════════╣")

    for item in order_list:
        name = MENU[item]["namn"]
        price = MENU[item]["pris"]
        emoji = MENU[item]["emoji"]
        print(f"  ║  {emoji} {name:<16} {price:>5} kr  ║")

    print("  ╠════════════════════════════════╣")
    print(f"  ║     {'TOTALT:':<16} {total_price:>5} kr  ║")
    print("  ╚════════════════════════════════╝")
    print(f"{Color.RESET}")


def animation_loading():
    """En liten laddningsanimation."""
    print(f"\n  {Color.DIM}", end="")
    for _ in range(3):
        for frame in ["☕    ", " ☕   ", "  ☕  ", "   ☕ ", "    ☕"]:
            print(f"\r  {Color.YELLOW}  Brygger... {frame}{Color.RESET}", end="", flush=True)
            time.sleep(0.1)
    print(f"\r  {Color.GREEN}  ✓ Klart!              {Color.RESET}")


def countdown_and_exit():
    """Visar en nedräkning innan programmet avslutas."""
    print(f"\n  {Color.DIM}Detta fönster stängs om: ", end="", flush=True)
    for i in range(5, 0, -1):
        print(f"{i}...", end="", flush=True)
        time.sleep(1)
    print(f"{Color.RESET}\n")


def main():
    """Huvudprogrammet — här körs allt."""
    clear_screen()
    print_cafe_logo()

    random_quote = random.choice(QUOTES)
    slow_print(f'  {Color.DIM}"{random_quote}"{Color.RESET}', delay=0.04)

    print(f"\n{Color.BOLD}  Välkommen till Johans Café!{Color.RESET}")
    customer_name = input(f"\n  {Color.CYAN}Vad heter du? {Color.RESET}")

    slow_print(f"\n  {Color.GREEN}Hej, {customer_name}! Vad vill du beställa?{Color.RESET}")

    order_list = []

    while True:
        show_menu()
        choice = input(f"\n  {Color.CYAN}Välj (0-5): {Color.RESET}")

        if choice == "0":
            if not order_list:
                print(f"\n  {Color.RED}Du har inte beställt något ännu!{Color.RESET}")
                continue
            break
        elif choice in MENU:
            item_name = MENU[choice]["namn"]
            order_list.append(choice)
            animation_loading()
            print(f"  {Color.GREEN}✓ {item_name} tillagd i din beställning!{Color.RESET}")
            print(f"  {Color.DIM}({len(order_list)} artik{'lar' if len(order_list) > 1 else 'el'} "
                  f"i beställningen){Color.RESET}")
        else:
            print(f"\n  {Color.RED}Ogiltigt val! Försök igen.{Color.RESET}")

    print_receipt(order_list, customer_name)

    slow_print(f"  {Color.MAGENTA}Tack för besöket, {customer_name}! Välkommen åter! 👋{Color.RESET}")
    print()

    countdown_and_exit()


# --- Kör programmet ---

if __name__ == "__main__":
    main()
