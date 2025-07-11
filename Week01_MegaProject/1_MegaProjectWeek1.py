import calculator
import number_guess
import todo
import password_generator
import unit_converter
import dice
import clock

def main():
    while True:
        print("\n" + "=" * 45)
        print("💻  Mega Python Utility Toolkit - Week 1".center(45))
        print("=" * 45)

        print("1️⃣  Calculator           🔢")
        print("2️⃣  Number Guessing Game 🎯")
        print("3️⃣  To-Do List           📝")
        print("4️⃣  Password Generator   🔐")
        print("5️⃣  Unit Converter       🧮")
        print("6️⃣  Dice Roller          🎲")
        print("7️⃣  Digital Clock        🕒")
        print("8️⃣  Exit                 ❌")

        choice = input("\n👉 Choose an option (1-8): ").strip()

        if choice == "1":
            calculator.main()
        elif choice == "2":
            number_guess.main()
        elif choice == "3":
            todo.main()
        elif choice == "4":
            password_generator.main()
        elif choice == "5":
            unit_converter.main()
        elif choice == "6":
            dice.main()
        elif choice == "7":
            clock.main()
        elif choice == "8":
            print("\n👋 Thanks for using the Toolkit. Goodbye!")
            break
        else:
            print("❌ Invalid option! Please choose between 1 and 8.")

if __name__ == "__main__":
    main()
