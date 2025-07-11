import calculator
import number_guess
import todo
import password_generator
import unit_converter
import dice
import clock
import sys
from time import sleep

def display_banner():
    """Display the program banner"""
    print("\n" + "=" * 50)
    print("💻  Mega Python Utility Toolkit - Week 1".center(50))
    print("=" * 50)

def display_menu():
    """Display the menu options"""
    menu_items = [
        ("1️⃣", "Calculator", "🔢"),
        ("2️⃣", "Number Guessing Game", "🎯"),
        ("3️⃣", "To-Do List", "📝"),
        ("4️⃣", "Password Generator", "🔐"),
        ("5️⃣", "Unit Converter", "🧮"),
        ("6️⃣", "Dice Roller", "🎲"),
        ("7️⃣", "Digital Clock", "🕒"),
        ("8️⃣", "Exit", "❌")
    ]
    
    for emoji, item, icon in menu_items:
        print(f"{emoji}  {item.ljust(25)} {icon}")

def clear_screen():
    """Clear the console screen"""
    # For Windows
    if sys.platform == 'win32':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def main():
    while True:
        clear_screen()
        display_banner()
        display_menu()

        choice = input("\n👉 Choose an option (1-8): ").strip()

        apps = {
            '1': calculator.main,
            '2': number_guess.main,
            '3': todo.main,
            '4': password_generator.main,
            '5': unit_converter.main,
            '6': dice.main,
            '7': clock.main
        }

        if choice in apps:
            clear_screen()
            apps[choice]()
            input("\nPress Enter to return to main menu...")
        elif choice == '8':
            print("\n👋 Thanks for using the Toolkit. Goodbye!")
            sleep(1)
            clear_screen()
            break
        else:
            print("\n❌ Invalid option! Please choose between 1 and 8.")
            sleep(1)

if __name__ == "__main__":
    import os  # Import moved here to avoid circular import issues
    main()
