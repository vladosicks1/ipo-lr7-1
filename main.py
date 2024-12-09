
books = {
    1: {"title": "Война и мир", "author": "Лев Толстой", "year": 1869},
    2: {"title": "Дом, в котором", "author": "Мариам Петросян", "year": 2010},
    3: {"title": "1984", "author": "Джордж Оруэлл", "year": 1949},
    4: {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
    5: {"title": "Метро 2035', ", "author": "Дмитрий Глуховский", "year": 2015}
}

count = 1

for key,book in books.items():
    print("-"*25,"Книга",count,"-"*25)
    print("Название:",book['title'],end=", ")
    print("Автор:",book['author'])
    print("-"*25,book['year'],"-"*25)
    count+=1
