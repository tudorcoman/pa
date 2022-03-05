
def sterge_carte(books, code):
    try:
        key = "book" + str(code)
        return books["author" + str(books[key]['author'])]
    except:
        return None
        print("Cartea nu exista")

with open("autori.in", "r") as inp:
    lines = inp.readlines()
    M, N = lines[0].split(" ")
    M = int(M)
    N = int(N)

    books = {}

    for i in range(1, M + 1):
        code, nume, prenume = lines[i].split(" ")
        nume_complet = nume + " " + prenume[:-1]
        books["author" + code] = nume_complet

    for i in range(1, N + 1):
        tokens = lines[M + i].split(" ")
        author = int(tokens[0])
        code = tokens[1]
        year = int(tokens[2])
        pages = int(tokens[3])
        book_name = " ".join([tokens[i] for i in range(4, len(tokens))])[:-1]
        books["book" + code] = {'author': author, 'year': year, 'pages': pages, 'name': book_name}

    #code = int(input())
    #sterge_carte(books, code)
    '''
print("Cartea a fost scrisa de %s" % books["author" + str(books[key]['author'])])
        books.pop("book" + str(code))
        print(books)
    '''
