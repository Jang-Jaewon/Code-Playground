import sys
n = int(sys.stdin.readline())

books = {}
for i in range(n):
    book = sys.stdin.readline().strip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values())

l = []
for book,number in books.items():
    if number == target:
        l.append(book)
print(sorted(l)[0])