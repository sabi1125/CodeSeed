def pick_recent_resource(recent):
    print("SELECT A RESOURCE:")
    for i, name in enumerate(recent, start=1):
        print("  " + str(i) + ") " + name)

    choice = input("Enter number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(recent)):
        print('INVALID SELECTION')
        return None

    return recent[int(choice) - 1]
