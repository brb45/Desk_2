from datetime import date


def get_today():
    print(type(date.today()))
    return date.today()


def myfunc_using_date():
    print("\nCalling func get_today()")
    day = get_today()
    print("Done calling get_today()")
    return day