def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None

    gunler = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return gunler[month - 1]


def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12:
        return None

    ay_gunu = days_in_month(year, month)

    if day < 1 or day > ay_gunu:
        return None

    toplam_gun = day

    for ay in range(1, month):
        toplam_gun += days_in_month(year, ay)

    return toplam_gun


print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 1, 1))
print(day_of_year(2000, 2, 29))
