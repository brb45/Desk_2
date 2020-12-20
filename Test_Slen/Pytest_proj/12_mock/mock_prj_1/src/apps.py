from datetime import date


def get_today():
    return date.today()


def myfunc_using_date():
    print("do something")
    day = get_today()
    print("do something else")
    return day