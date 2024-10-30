def get_user_info():
    user_info = {}

    user_info['name'] = input("Enter your name: ").strip()
    while not user_info['name']:
        print("This field is required. Please enter your name.")
        user_info['name'] = input("Enter your name: ").strip()

    user_info['surname'] = input("Enter your surname: ").strip()
    while not user_info['surname']:
        print("This field is required. Please enter your surname.")
        user_info['surname'] = input("Enter your surname: ").strip()

    user_info['grade'] = input("Enter your grade: ").strip()
    while not user_info['grade']:
        print("This field is required. Please enter your grade.")
        user_info['grade'] = input("Enter your grade: ").strip()

    user_info['gender'] = input("Enter your gender: ").strip()
    while not user_info['gender']:
        print("This field is required. Please enter your gender.")
        user_info['gender'] = input("Enter your gender: ").strip()

    user_info['address'] = input("Enter your address: ").strip()
    while not user_info['address']:
        print("This field is required. Please enter your address.")
        user_info['address'] = input("Enter your address: ").strip()

    user_info['province'] = input("Enter your province: ").strip()
    while not user_info['province']:
        print("This field is required. Please enter your province.")
        user_info['province'] = input("Enter your province: ").strip()

    user_info['id_number'] = input("Enter your ID number: ").strip()
    while not user_info['id_number']:
        print("This field is required. Please enter your ID number.")
        user_info['id_number'] = input("Enter your ID number: ").strip()

    return user_info


def display_school_categories():
    categories = {
        1: "Maths",
        2: "Economics",
        3: "History",
        4: "Agriculture"
    }

    print("\nSchool Categories:")
    for number, category in categories.items():
        print(f"{number}. {category}")

    while True:
        try:
            choice = int(input("Select a category by number: "))
            if choice in categories:
                return categories[choice]
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a number.")


def display_subjects():
    subjects = {
        1: "Maths",
        2: "English",
        3: "Language",
        4: "Physical Science",
        5: "Life Sciences",
        6: "Geography",
        7: "Economics",
        8: "Accounting",
        9: "Business Management",
        10: "History",
        11: "Agriculture"
    }

    print("\nAvailable Subjects:")
    for number, subject in subjects.items():
        print(f"{number}. {subject}")

    return subjects


def get_subject_marks(subjects):
    marks = {}
    selected_subjects = []

    while len(selected_subjects) < 6:
        try:
            choice = int(input("Select a subject by number (or 0 to finish): "))
            if choice == 0:
                break
            if choice in subjects and choice not in selected_subjects:
                mark = input(f"Enter marks for {subjects[choice]}: ").strip()
                while not mark or not mark.replace('.', '', 1).isdigit():
                    print("Please enter a valid mark (numeric value).")
                    mark = input(f"Enter marks for {subjects[choice]}: ").strip()
                marks[subjects[choice]] = float(mark)
                selected_subjects.append(choice)
            else:
                print("Invalid selection or subject already selected. Please choose a valid subject.")
        except ValueError:
            print("Please enter a valid number.")

    return marks


def calculate_aps_score(selected_category, marks):
    if marks:
        aps_score = sum(marks.values())
    else:
        return "Rejected", None

    if selected_category == "Maths":
        if aps_score >= 35:
            return f"You are accepted to the Maths category with an APS score of {aps_score:.2f}.", None
        else:
            return "Rejected", aps_score

    elif selected_category == "Economics":
        if aps_score >= 28:
            return f"You are accepted to the Economics category with an APS score of {aps_score:.2f}.", None
        else:
            return "Rejected", aps_score

    elif selected_category == "History":
        if aps_score >= 14:
            return f"You are accepted to the History category with an APS score of {aps_score:.2f}.", None
        else:
            return "Rejected", aps_score

    return "Rejected", None


def suggest_categories(aps_score):
    suggestions = []
    if aps_score >= 35:
        suggestions.append("Maths")
    if aps_score >= 28:
        suggestions.append("Economics")
    if aps_score >= 14:
        suggestions.append("History")

    return suggestions


def main():
    while True:
        user_info = get_user_info()
        selected_category = display_school_categories()

        subjects = display_subjects()
        marks = get_subject_marks(subjects)

        print("\nUser Information:")
        for key, value in user_info.items():
            print(f"{key.capitalize()}: {value}")

        print(f"Selected Category: {selected_category}")

        aps_result, aps_score = calculate_aps_score(selected_category, marks)
        print(f"APS Score: {aps_result}")

        if aps_result.startswith("Rejected") and aps_score is not None:
            suggestions = suggest_categories(aps_score)
            if suggestions:
                print("You qualify for the following categories based on your APS score:")
                for category in suggestions:
                    print(f"- {category}")
            else:
                print("You do not qualify for any categories based on your APS score.")

        # Ask if the user wants to start over or quit
        restart = input(
            "\nWould you like to start over or quit? (Enter 'start' to restart or 'quit' to exit): ").strip().lower()
        if restart == 'quit':
            print("Thank you for using the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
