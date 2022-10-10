# Let’s take a look at the Python Code of this game.

answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("""
WELCOME! LET'S START THE ADVENTURE

Let's assume a scenario that there is placement activity in your college which is going to happen soon. & Faculties looking that who are eligible and who are not.
The minimum required CGPA to be a part of this activity is 7cgpa. Now faculties ask to you some questions.

is your CGPA >=7 ❔ (Yes / No)
""")

ans1 = input("Type your answer:")

if ans1 in answer_yes:
    print("\nOK so currently do you have any backlog . Will you say (Yes / No)\n")

    ans2 = input("Type your answer:")

    if ans2 in answer_no:
        print("\nCongratulations! You are eligible to be a part of placement activity.Best of luck!")

    elif ans2 in answer_yes:
        print("\nSorry you are not eligible. Better luck next time!")

    else:
        print("\nYou typed the wrong input. Please try again!")

elif ans1 in answer_no:
    print("\nOkay so currently do you have any backlog? (Yes / No)\n")

    ans3 = input("Type your answer:")

    if ans3 in answer_yes:
        print("\nSorry! You should try harder.It's so sad 😔")

    elif ans3 in answer_no:
        print("\nIt's good that you don'thave any backlog.pls maintain you CGPA.")

    else:
        print("\nYou typed the wrong input. Please try again!")

else:
    print("\nYou typed the wrong input. Please try again!")
