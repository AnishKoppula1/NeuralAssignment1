str1 = input("Enter a sentence")
str2 = str1.split()
ans = ""
for st in str2:
    if(st == "python"):
        ans += "pythons"
    else:
        ans += st
    ans += " "
print(ans)
