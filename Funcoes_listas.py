# def list_sum(lst):
#     s = 0
 
#     for elem in lst:
#         s += elem
 
#     return s

# print(list_sum([5, 4, 3]))

# def strange_list_fun(n):
#  strange_list = []
 
#  for i in range(0, n):
#     strange_list.insert(0, i)
 
#  return strange_list

# print(strange_list_fun(5))

# def is_year_leap(year):
#  #
#     if year % 4 == 0:
#         return True
#     if year % 100 == 0 and year % 400 == 0:
#         return True
#     if year % 100 != 0 and year % 400 == 0:
#         return False
#     else: 
#         False
     
# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fracassado")


# def is_year_leap(year):
#  if year % 4 != 0:
#     return False
#  elif year % 100 != 0:
#     return True
#  elif year % 400 != 0:
#     return False
#  else:
#     return True

# def days_in_month(year,month):
#  if year < 1582 or month < 1 or month > 12:
#     return None
#  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#  res = days[month - 1]
#  if month == 2 and is_year_leap(year):
#     res = 29
#  return res

# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#  yr = test_years[i]
#  mo = test_months[i]
#  print(yr,mo,"-> ",end="")
#  result = days_in_month(yr, mo)
#  if result == test_results[i]:
#     print("OK")
#  else:
#     print("Fracassado")

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
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
        print(days)
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))