
from AsiB import *
from functools import cmp_to_key

def carti_autor(books, authorCode):
    ans = []
    try:
        authorName = books["author" + str(authorCode)]
        for key in books.keys():
            if key[:4] == "book" and books[key]["author"] == authorCode:
               ans.append((books[key]["name"], books[key]["year"], books[key]["pages"])) 
        return authorName, ans
    except:
        return []

def cmp(a, b):
    if a[1] > b[1]:
        return 1
    elif a[1] == b[1]:
        if a[2] > b[2]:
            return -1
        elif a[2] < b[2]:
            return 1
        else:
            if a[0] > b[0]:
                return 1
            else:
                return -1
    else:
        return -1

nume, ans = carti_autor(books, int(input()))
if len(ans) == 0:
    print("cod incorect")
else:
    print(nume)
    cmp_items_py3 = cmp_to_key(cmp)
    ans.sort(key=cmp_items_py3)    

    for x in ans:
        print(*x)
