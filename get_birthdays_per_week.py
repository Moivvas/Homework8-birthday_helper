from datetime import datetime, timedelta
from collections import defaultdict

users = [{'name': 'Jill Valentine', 'birthday': '2000-6-27'},
         {'name': 'Bill Overbeck', 'birthday': '1970-6-27'},
         {'name': 'Feng Min', 'birthday': '2000-06-24'}
         ]

def next_monday_f():
    today = datetime.now().date()
    days_ahead = (0 - today.weekday()) % 7
    next_monday = today + timedelta(days=days_ahead)
    print(next_monday)
    return next_monday

def get_birthdays_per_week(lst):
    party = defaultdict(list)
    current_datetime = datetime.now().date()
    next_monday = next_monday_f()
    for user in users:
        user_birthday = datetime.strptime(user['birthday'], "%Y-%m-%d")
        actual_user_birthday = datetime(year=current_datetime.year, month=user_birthday.month, day=user_birthday.day).date()
        if (next_monday - timedelta(days=2)) <= actual_user_birthday < (next_monday + timedelta(days=5)):
            if actual_user_birthday.weekday() in (5, 6):
                party[next_monday].append(f'{user["name"]} - {actual_user_birthday}')
            else:
                party[actual_user_birthday].append(f'{user["name"]} - {actual_user_birthday}')
        else:
            continue
    sorted_party = dict(sorted(party.items(), key=lambda x: x[0].weekday()))
    return sorted_party

if __name__ == '__main__':
    for key, value in get_birthdays_per_week(users).items():
        print(f"{key.strftime('%A')}: {value}")
