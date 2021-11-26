def get_num_from_user():
    num = int(input("Enter a number : "))
    return num


def legal_day(day):
    if(day in range(1, 32)):
        return True
    else:
        return False


def legal_month(month):
    if(month in range(1, 13)):
        return True
    else:
        return False


def legal_year(year):
    if(year > 0):
        return True
    else:
        return False


def get_month_english(month):
    month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']
    print(month_name[month-1])
    return month_name[month-1]


def get_day_english(day):
    day_as_string = str(day)
    print(day_as_string + "th")
    return day_as_string + "th"


def print_english_date(day_in_english, month_in_english, year):
    print(month_in_english + " " + day_in_english + ", " + str(year))


def main():
    day = get_num_from_user()
    month = get_num_from_user()
    year = get_num_from_user()

    if(legal_day(day) and legal_month(month) and legal_year(year)):
        month_in_english = get_month_english(month)
        day_in_english = get_day_english(day)
        print_english_date(day_in_english, month_in_english, year)

    else:
        print("Error! invalid Date!  Goodbye :) ")


if __name__ == "__main__":
    main()
