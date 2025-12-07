import module1_academic_tracker as m1
import module2_password_assistant as m2

def main():
    MENU = """
Smart Student Assistant
-----------------------
1) Academic Tracker — GPA & Scholarship
2) Password Assistant — Generator & Checker
3) Exit
Choice: """
    while True:
        choice = input(MENU).strip()
        if choice == "1":
            print("\nLaunching Academic Tracker...\n")
            m1.main()     # run Module 1’s internal menu
        elif choice == "2":
            print("\nLaunching Password Assistant...\n")
            m2.main()     # run Module 2’s internal menu
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1–3.")

if __name__ == "__main__":
    main()