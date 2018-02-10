def year(year):
    #year = int(input("Enter year "))
    if year %4==0 and year%100!=0:
        print("YES")
        return True
    elif year%400==0:
        print("YES")
        return True
    else:
        print("NO")
        return False

y = year(2012)