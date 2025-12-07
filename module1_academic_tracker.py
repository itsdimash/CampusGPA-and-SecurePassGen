def grade(percent):
    if 95 <= percent <= 100:
        return ("A", 4.00)
    elif 90 <= percent < 95:
        return ("A-", 3.67)
    elif 85 <= percent < 90:
        return ("B+", 3.33)
    elif 80 <= percent < 85:
        return ("B", 3.00)
    elif 75 <= percent < 80:
        return ("B-", 2.67)
    elif 70 <= percent < 75:
        return ("C+", 2.33)
    elif 65 <= percent < 70:
        return ("C", 2.00)
    elif 60 <= percent < 65:
        return ("C-", 1.67)
    elif 55 <= percent < 60:
        return ("D+", 1.33)
    elif 50 <= percent < 55:
        return ("D", 1.00)
    elif 25 <= percent < 50:
        return ("FX", 0.00)
    else:
        return ("F", 0.00)


def calculate_gpa(subjects):
    if not subjects:
        return 0.0

    total_points = 0
    total_credits = 0
    for name, credits, percent in subjects:
        letter, gp = grade(percent)
        total_points += gp * credits
        total_credits += credits

    gpa = total_points / total_credits if total_credits > 0 else 0
    return round(gpa, 2)


def classify_scholarship(gpa):
    if gpa >= 3.8:
        return "Dean’s List + Merit Scholarship"
    elif gpa >= 3.5:
        return "Merit Scholarship"
    elif gpa >= 2.0:
        return "No Scholarship"
    else:
        return "Scholarship Lost"


def add_subject(subjects: list, name: str, credits: int, percent: int):
    if credits <= 0 or not (0 <= percent <= 100):
        print("Invalid input. Credits must be >0 and percent 0–100.")
        return

    i = 0
    while i < len(subjects):
        sub_name, old_credits, old_percent = subjects[i]
        if sub_name == name:
            subjects[i] = (name, credits, percent)
            print(f"Updated {name}.")
            return
        i += 1

    subjects.append((name, credits, percent))
    print(f"Added {name}.")


def delete_subject(subjects: list, name: str):
    i = 0
    while i < len(subjects):
        sub_name, credits, percent = subjects[i]
        if sub_name == name:
            del subjects[i]
            print(f"Deleted {name}.")
            return True
        i += 1
    print(f"{name} not found.")
    return False

def add_gpa_to_trend(trend_list, semester_name, gpa):
    if not semester_name.strip():
        print("→ Semester label cannot be empty.")
        return
    for i in range(len(trend_list)):
        if trend_list[i][0] == semester_name:
            trend_list[i] = (semester_name, gpa)
            print(f"→ Updated semester: {semester_name} → {gpa}")
            return

    trend_list.append((semester_name, gpa))
    print(f"→ Added semester: {semester_name} → {gpa}")


def view_gpa_trend(trend_list):
    if not trend_list:
        print("→ No semester GPAs recorded.")
        return

    print("\nSemester GPA Trend")
    print("------------------")
    for i in range(len(trend_list)):
        semester, gpa = trend_list[i]
        status = classify_scholarship(gpa)
        print(f"{semester:<15}: {gpa:.2f} ({status})")

def print_report(subjects: list[str, int, int], semester_name: str):
    if not subjects:
        print(f"\nNo subjects entered for {semester_name}.\n")
        return

    total_credits = 0
    total_points = 0

    print(f"\nGPA Report — {semester_name}")
    print("+------------------------------+---------+---------+--------+--------+")
    print("| Subject                      | Credits | Percent | Letter | Points |")
    print("+------------------------------+---------+---------+--------+--------+")
    for name, credits, percent in subjects:
        letter, gp = grade(percent)
        total_credits += credits
        total_points += gp * credits
        print(f"| {name:<28} | {credits:^7} | {percent:^7} | {letter:^6} | {gp:^6.2f} |")

    print("+------------------------------+---------+---------+--------+--------+")
    gpa = round(total_points / total_credits, 2)
    status = classify_scholarship(gpa)
    print(f"| Total Credits                | {total_credits:^7} |         |        |        |")
    print(f"| Weighted GPA                 |         |         |        | {gpa:^6.2f} |")
    print(f"| Scholarship Status           |         |         |        | {status} |")
    print("+------------------------------+---------+---------+--------+--------+\n")


def main():
    semesters = {}
    trend = []

    while True:
        print("\nAcademic Tracker Menu")
        print("1) Add/Update Subject")
        print("2) Delete Subject")
        print("3) Show GPA Report")
        print("4) Switch semester")
        print("5) GPA trend (add current GPA)")
        print("6) View GPA trend")
        print("7) Back to main menu")

        choice = input("Enter choice: ").strip()

        if "current_semester" not in locals() or choice == "4":
            current_semester = input("\nEnter semester name (For example: 1): ").strip()
            if current_semester not in semesters:
                semesters[current_semester] = []
            print(f"Semester set to: {current_semester}")
            continue

        if choice == "1":
            name = input("Subject name: ")
            credits = int(input("Credits: "))
            percent = int(input("Percent: "))
            add_subject(semesters[current_semester], name, credits, percent)

        elif choice == "2":
            name = input("Subject name to delete: ")
            delete_subject(semesters[current_semester], name)

        elif choice == "3":
            print_report(semesters[current_semester], current_semester)

        elif choice == "5":
            semester = input("Semester label (For example: 1): ").strip()
            if current_semester in semesters and semesters[current_semester]:
                gpa = calculate_gpa(semesters[current_semester])
                add_gpa_to_trend(trend, semester, gpa)
            else:
                print("→ No subjects to calculate GPA.")

        elif choice == "6":
            view_gpa_trend(trend)

        elif choice == "7":
            print("Returning to main menu...")
            break
        else:
            print("Please choose 1–5.")


if __name__ == "__main__":
    main()