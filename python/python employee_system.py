import csv
import os

FILE_NAME = "employees.csv"

# ------------------- Functions -------------------
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:  # لو الملف لسه جديد نكتب الهيدر
            writer.writerow(["ID", "Name", "Department", "Salary"])
        writer.writerow([emp_id, name, dept, salary])

    print("✅ Employee added successfully!")


def view_employees():
    if not os.path.exists(FILE_NAME):
        print("❌ No employees found.")
        return

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        print("\n--- Employee List ---")
        for row in reader:
            print(row)


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False

    if not os.path.exists(FILE_NAME):
        print("❌ No employees found.")
        return

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == emp_id:  # row[0] = ID
                print(f"✅ Found -> {row}")
                found = True
                break

    if not found:
        print("❌ Employee not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    if not os.path.exists(FILE_NAME):
        print("❌ No employees found.")
        return

    employees = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] != emp_id:
                employees.append(row)
            else:
                found = True

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(employees)

    if found:
        print("✅ Employee deleted successfully.")
    else:
        print("❌ Employee not found.")


# ------------------- Main Menu -------------------
def main():
    while True:
        print("\n=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
