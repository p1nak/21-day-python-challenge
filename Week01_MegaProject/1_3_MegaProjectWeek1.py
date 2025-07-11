import calculator
import number_guess
import todo
import password_generator
import unit_converter
import dice
import clock
import sys
import os
from time import sleep, time
from datetime import datetime

# Constants
LOG_FILE = "toolkit_log.txt"
VERSION = "2.0"

def display_banner():
    """Display the program banner with version info"""
    print("\n" + "=" * 50)
    print(f"💻  Mega Python Utility Toolkit v{VERSION}".center(50))
    print("=" * 50)

def display_menu():
    """Display the menu options with emojis"""
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
    """Clear the console screen cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')

def log_activity(tool_name, duration=None):
    """Log user activity to a file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        if duration is not None:
            f.write(f"{timestamp} - Used {tool_name} for {duration:.1f} seconds\n")
        else:
            f.write(f"{timestamp} - Launched toolkit\n")

def format_time(seconds):
    """Convert seconds to human-readable format"""
    if seconds < 60:
        return f"{seconds:.1f} sec"
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{int(minutes)} min {int(seconds)} sec"

def show_stats():
    """Display usage statistics if log file exists"""
    if not os.path.exists(LOG_FILE):
        return
    
    print("\n📊 Usage Statistics:")
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            print(f"Total sessions: {len([l for l in lines if 'Launched toolkit' in l])}")
            
            # Calculate total time per tool
            tool_times = {}
            for line in lines:
                if "for" in line:
                    tool = line.split("Used ")[1].split(" for")[0]
                    time = float(line.split("for ")[1].split(" ")[0])
                    tool_times[tool] = tool_times.get(tool, 0) + time
            
            if tool_times:
                print("\n⏱️ Time spent per tool:")
                for tool, total_time in tool_times.items():
                    print(f"  {tool}: {format_time(total_time)}")
    except Exception as e:
        print(f"Couldn't read stats: {e}")

def main():
    # Log toolkit launch
    log_activity("Toolkit")
    
    while True:
        clear_screen()
        display_banner()
        show_stats()
        display_menu()

        choice = input("\n👉 Choose an option (1-8): ").strip()

        apps = {
            '1': ("Calculator", calculator.main),
            '2': ("Number Guessing Game", number_guess.main),
            '3': ("To-Do List", todo.main),
            '4': ("Password Generator", password_generator.main),
            '5': ("Unit Converter", unit_converter.main),
            '6': ("Dice Roller", dice.main),
            '7': ("Digital Clock", clock.main)
        }

        if choice in apps:
            tool_name, app_func = apps[choice]
            clear_screen()
            start_time = time()
            app_func()
            duration = time() - start_time
            log_activity(tool_name, duration)
            input(f"\n⏱️ Used {tool_name} for {duration:.1f} seconds. Press Enter to continue...")
        elif choice == '8':
            print("\n👋 Thanks for using the Toolkit. Goodbye!")
            sleep(1)
            clear_screen()
            break
        else:
            print("\n❌ Invalid option! Please choose between 1 and 8.")
            sleep(1)

if __name__ == "__main__":
    main()
