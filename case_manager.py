from analysis import get_priority

def add_case(cases):
    cid = input("Case ID: ")
    crime = input("Crime: ")
    location = input("Location: ")
    suspect = input("Suspect: ")
    evidence = int(input("Evidence count: "))

    priority = get_priority(evidence)
    cases.append([cid, crime, location, suspect,
                  evidence, priority, "Open"])
    print("Case added!")

def view_cases(cases):
    if not cases:
        print("No cases found!")
        return

    for c in cases:
        print("\nID:", c[0], "| Crime:", c[1])
        print("Location:", c[2], "| Suspect:", c[3])
        print("Evidence:", c[4], "| Priority:", c[5])
        print("Status:", c[6])

def search_case(cases):
    cid = input("Enter Case ID: ")

    for c in cases:
        if c[0] == cid:
            print("Case Found:", c)
            return

    print("Case not found!")

def update_status(cases):
    cid = input("Enter Case ID: ")

    for c in cases:
        if c[0] == cid:
            status = input(
                "New status (Open/Under Investigation/Solved): "
            )

            if status not in ["Open", "Under Investigation", "Solved"]:
                print("Invalid status!")
                return

            c[6] = status

            if status == "Solved":
                print("The case has been solved!")
            else:
                print("Status updated!")

            return

    print("Case not found!")

def delete_case(cases):
    cid = input("Enter Case ID: ")

    for c in cases:
        if c[0] == cid:
            cases.remove(c)
            print("Case deleted!")
            return

    print("Case not found!")