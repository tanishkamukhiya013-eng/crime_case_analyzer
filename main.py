from case_manager import add_case, view_cases
from case_manager import search_case, update_status, delete_case
from data_manager import save_cases, load_cases

cases = load_cases()

while True:
    print("\n===== CRIME CASE ANALYZER =====")
    print("1. Add Case")
    print("2. View Cases")
    print("3. Search Case")
    print("4. Update Status")
    print("5. Delete Case")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_case(cases)
        save_cases(cases)

    elif choice == "2":
        view_cases(cases)

    elif choice == "3":
        search_case(cases)

    elif choice == "4":
        update_status(cases)
        save_cases(cases)

    elif choice == "5":
        delete_case(cases)
        save_cases(cases)

    elif choice == "6":
        print("Investigation closed!")
        break

    else:
        print("Invalid choice!")