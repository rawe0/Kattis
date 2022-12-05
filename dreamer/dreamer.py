from functools import cmp_to_key
import sys, itertools

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def compare(item1, item2):
    if(item1[2] > item2[2]):
        return 1
    elif(item1[2] < item2[2]):
        return -1
    else:
        if(item1[1] > item2[1]):
            return 1
        elif(item1[1] < item2[1]):
            return -1
        else:
            if(item1[0] > item2[0]):
                return 1
            elif(item1[0] < item2[0]):
                return -1
            else:
                return 0


def check_for_leap(year):
    if(year % 4 != 0):
        return False
    if(year % 100 != 0):
        return True
    if (year % 400 == 0):
        return True
    return False


def get_date(date):
    month = ""
    day = ""
    year = date[2]
    if (date[1] < 10 ):
        month = f"0{date[1]}"
    else:
        month = date[1]
    if (date[0] < 10 ):
        day = f"0{date[0]}"
    else:
        day = date[0]
    return f"{day} {month} {year}"


def valid_date(day, month, year):
    
    if year < 2000:
        return -1
    if month > 12 or month == 0:
        return -1

    if(month == 2 and check_for_leap(year)):
         if day > 29 or day == 0:
            return -1
    else:
        if day > days_in_month[month-1] or day == 0:
            return -1
    return 0

def main():
    first = True
    for arg in sys.stdin:
        parameters = arg.split()
        if(first):
            n = int(parameters[0])
            first=False
        else:
            y = parameters[2]
            m = parameters[1]
            d = parameters[0]
            permutations = list(itertools.permutations(y + m + d, 8))
            dates = set()
            for permutation in permutations:
                day =  int(permutation[0] + permutation[1])
                month = int(permutation[2] + permutation[3])
                year = int(permutation[4] + permutation[5] + permutation[6] + permutation[7])
                if(valid_date(day, month, year) != -1):
                    dates.add((day, month, year))
            
            all_dates = list(dates)
            min_date = min(all_dates, key=compare)
            nr_dates = len(all_dates)
            if(nr_dates == 0):
                print("0")
            else:
                print(f"{nr_dates} {get_date(min_date)}")

            
if __name__ == "__main__":
    main()


            