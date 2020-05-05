from datetime import date
print(" you will enter your date of birth and i will tell you what your sign is\n")

year = int(input("please enter the Year of your birth"))
month = int(input("please enter the Month of your birth"))
day = int(input("please enter the Day of your birth"))
print("your Date of Birth is : ", day, "/", month, "/", year)
age = date.today().year - year
print(" you are ", age, "years old")

if month == 12 and day >= 22 or month == 1 and day <= 19:
    sign = "Capicorn"
elif month == 1 and day >= 20 or month == 2 and day <=18:
   sign = "Aquarius"
elif month == 2 and day >= 19 or month == 3 and day <= 20:
    sign = "Pisces"
elif month == 3 and day >= 21 or month == 4 and day <= 19:
    sign = "Aries"
elif month == 4 and day >= 20 or month == 5 and day <= 20:
    sign = "Taurus"
elif month == 5 and day >= 21 or month == 6 and day <= 20:
    sign = "Gemini"
elif month == 6 and day >= 21 or month == 7 and day <= 22:
    sign = "Cancer"
elif month == 7 and day >= 23 or month == 8 and day <= 22:
    sign = "Leo"
elif month == 8 and day >= 23 or month == 9 and day <= 22:
    sign = "Virgo"
elif month == 9 and day >= 23 or month == 10 and day <= 22:
    sign = "Libra"
elif month == 10 and day >= 23 or month == 11 and day <= 21:
    sign = "Scorpio"
elif month == 11 and day >= 22 or month == 12 and day <= 21:
    sign = "Sagittarius"

print("your sign is", sign)
