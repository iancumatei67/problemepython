import datetime

user_input = input("Enter your goal with a deadline separated by a colon ")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, '%d.%m.%Y')
today_date = datetime.datetime.today()
difference = deadline_date - today_date

print(f"Dear user, the time remaining for your goal: {goal} is {difference.total_seconds() / 60 / 60 } hours ")