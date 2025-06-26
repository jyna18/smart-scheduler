# scheduler.py

# Exam schedule list
exam_schedule = []

def add_exam():
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter assigned room: ")
    exam_schedules.append({
        "name": name,
        "date": date,
        "time": time,
        "room": room
    })
    print("✅ Exam added successfully!\n")

def view_exams():
    if not exam_schedules:
        print("❌ No exams scheduled yet.\n")
        return
    print("\n📅 Scheduled Exams:")
    for idx, exam in enumerate(exam_schedules, start=1):
        print(f"{idx}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")
    print()

def edit_exam():
    view_exams()
    if not exam_schedules:
        return
    try:
        index = int(input("Enter exam number to edit: ")) - 1
        if 0 <= index < len(exam_schedules):
            print("Leave field blank to keep current value.")
            name = input("New exam name: ") or exam_schedules[index]['name']
            date = input("New date (YYYY-MM-DD): ") or exam_schedules[index]['date']
            time = input("New time (HH:MM): ") or exam_schedules[index]['time']
            room = input("New room: ") or exam_schedules[index]['room']

            exam_schedules[index].update({
                "name": name,
                "date": date,
                "time": time,
                "room": room
            })
            print("✅ Exam updated successfully!\n")
        else:
            print("❌ Invalid exam number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def delete_exam():
    view_exams()
    if not exam_schedules:
        return
    try:
        index = int(input("Enter exam number to delete: ")) - 1
        if 0 <= index < len(exam_schedules):
            removed = exam_schedules.pop(index)
            print(f"🗑️ Removed '{removed['name']}' from the schedule.\n")
        else:
            print("❌ Invalid exam number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def main_menu():
    while True:
        print("==== SMART EXAM SCHEDULER ====")
        print("1. Add Exam")
        print("2. View Exams")
        print("3. Edit Exam")
        print("4. Delete Exam")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_exam()
        elif choice == "2":
            view_exams()
        elif choice == "3":
            edit_exam()
        elif choice == "4":
            delete_exam()
        elif choice == "5":
            print("👋 Exiting Smart Scheduler. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-5.\n")

if __name__ == "__main__":
    main_menu()

