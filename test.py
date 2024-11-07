
# w=input().split()
# print(len(w))
# w=input().split()
# print(";".join(w))
# a=sorted(input().split())
# b= " ".join(a)
# print(f"{b}")
# a,b=map(int,input().split())
# print(f"{min(a,b)} {max(a,b)} ")
# print(f"г. {input()}, ул. {input()}, д. {input()}, кв. {input()}")
# usd=float(input())
# rub=int(input())
# s=int(rub/usd)
# print(f"Вы можете получить {s}$ за {rub} рублей по курсу {usd}")
# l=list(input().split())
# lst=f"[{', '.join(l)}]"
# print(lst)
# lst=list(map(int,input().split()))
# print(lst)
# cities = input().split()
# print("Москва" in cities)
# cities = input().split()
# print(cities[-1])

# marks = list(map(int, input().split()))
# print(round(sum(marks)/len(marks),1))

# name=input()
# author=input()
# number=input()
# price=float(input())*2
# book=[name,author,number,price]
# book[book.index(author)]='Пушкин'
# del book [book.index(number)]
# print(book)

# lst= list(map(int, input().split()))
# print(max(lst),min(lst),sum(lst))

# lst= list(map(int,input().split()))
# lst= sorted(lst, reverse=True)
# lst=" ".join(map(str,lst))
# print(lst)

# lst= list(map(int,input().split()))
# lst= sorted(lst, reverse=True)
# print(*lst)

# cities =["Москва", "Тверь", "Вологда"]
# lst=list(input().split())+cities
# print(*lst)
# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[:3])
# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[2:])
# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[::2])
# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[1::2])
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# slised_m = m[2:7]
# m=slised_m[::-1]
# print(m)
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[6:1:-1])
# # m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# # print(m[::-2])
# lst=list(map(int,input().split()))
# lst.append(lst[0]!=lst[-1])
# print(*lst)
# cities = ["Москва", "Казань", "Ярославль"]
# cities.insert(1,"Ульяновск")
# print(*cities)
# lst=list(input())
# lst.remove("+")
# lst.remove("7")
# lst.insert(0,"8")
# lst.remove("-")
# lst.remove("-")
# print("".join(lst))
# lst=input().split()
# lst.remuve(1)
# print(lst)
# lst = [5.4, 6.7, 10.4]
# digs =list(map(int,input().split()))
# lst.append(digs)
# print(lst)
# a,b,c=input().split(),input().split(),input().split()
# lst=[a,b,c]
# print(lst)
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# c=list(map(int,input().split()))
# n=[a,b,c]
# num=n[0][-1],n[1][-1],n[2][-1]
# print(*num)
# a = [True, [1, 0, ["True", ["Истина", "Ложь"], "False"]], False]
# print(a[1][2][1][0])
# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#      ["Я", "Python", "выучил", "с", "каналом"],
#      ["Балакирев", "что", "раздавал?"]]
# a = " ".join(t)
# print(input() in a)
# word = input().strip().lower()
# if word == word[::-1]:
#     print("ДА")
# else:
#     print("НЕТ")
# m,n=map(int,input().split())
#
# if m % n==0:
#     print(int(m/n))
# else:
#    if m / n != 0:
#     print(f" {m} на {n} нацело не делится")

# a,b,c=map(int,input().split())
# a = pow(a,2)
# b = pow(b,2)
# c = pow(c,2)
# if a + b == c:
#     print("ДА")
# else:
#     print("НЕТ")
# a=input()
# b=  f"[{' '.join(a)}]"
# if a[-1] == '7':
#     print("ДА")
# else:
#     print("НЕТ")

# a = input()  # Наприклад, введення: 23456
# print('[', ' '.join(a), ']')
# t = float(input())
# if t % 5 < 3:
#     print("green")
# else:
#     print("red")
# a = int(input())
# if a == 1:
#     print("понедельник")
# if a == 2:
#     print("вторник")
# days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# day_namber = int(input())
# if 1 <= day_namber <= 7:
#     print(days [day_namber -1])
# else:
#     print("Неправильний номер дня недели")

# number_of_days = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31","30","31"]
# month_number = int(input())
# if month_number in [1,3,5,7,8,10,12]:
#     print(31)
# elif month_number == 2:
#     print(28)
# elif month_number in [4,6,9,11]:
#     print(30)
# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# m, n = map(int, input().split())
# if n > 1 :
#     prev_day = n - 1
#     prev_month = m
# else:
#     if m > 1 :
#         prev_month = m -1
#     else:
#         prev_month = 12
#     prev_day = days_in_month [prev_month-1]
# if n < days_in_month [m - 1] :
#     next_day = n + 1
#     next_month = m
# else:
#     if m < 12:
#         next_month = m + 1
#     else:
#         next_month = 1
#     next_day = 1
# prev_date = f"{prev_month:02}.{prev_day:02}"
# next_date = f"{next_month:02}.{next_day:02}"
# print(" ".join([prev_date, next_date]))

# day_week = ['понедельник','вторник','среда','четверг','пятница','суббота','воскресенье']
# k = int(input())
# r = (k - 1) % 7
# print(day_week[r])

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())
a -= 1
b -= 1
c -= 1
note_a = f"#{m[a]}" if a == 0 or a == 3 else m[a]
note_b = f"#{m[b]}" if b == 0 or b == 3 else m[b]
note_c = f"#{m[c]}" if c == 0 or c == 3 else m[c]
result = " ".join([note_a, note_b, note_c ])
print(result)

/opt/homebrew/bin/git
/opt/homebrew/opt/git


















