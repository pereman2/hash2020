# sasukecomebackpls
def get_input_line():
    file_input = []
    with open('b_read_on.txt', 'r') as f:
        file_input = f.readlines()
    return file_input

class Library(object):

    def __init__(self, id, books, time, nbooks_scanned):
        super(Library, self).__init__()
        self.id = id
        self.books = books
        self.time = time
        self.nbooks_scanned = nbooks_scanned
        self.score = self.get_score()

    def get_score(self):
        score = 0
        for i in self.books:
            score += i.score
        score = score * self.nbooks_scanned
        score = score/self.time
        return score


class Book(object):

    def __init__(self, id, score):
        super(Book, self).__init__()
        self.id = id
        self.score = score

def get_books(b, scores):
    books = []
    for i in b:
        punt = int(scores[int(i)])
        book = Book(int(i), punt)
        books.append(book)
    books.sort(key=lambda x: x.score, reverse=True)
    return books

def get_library(lib, books, id_lib):
    librarie = Library(id_lib, books, int(lib[1]), int(lib[2]))
    return librarie


def get_libraries(data, scores):
    libraries = []
    i = 0
    id_lib = 0
    while i < len(data):
        if i+1 >= len(data):
            break
        lib = data[i].strip('\n').split(' ')
        b = data[i+1].strip('\n').split(' ')
        books = get_books(b, scores)
        librarie = get_library(lib, books, id_lib)
        libraries.append(librarie)
        i = i + 2
        id_lib = id_lib + 1
    return libraries


def days(sortedLibraries, config):
    singupDays = 0
    singupLibraries = []
    score = 0
    booksScanned = []
    iteracions = int(config[2])
    for i in range(iteracions):
        #Agafa una llibreria
        if len(sortedLibraries) != 0 and singupDays == 0:
            for pos,sl in enumerate(sortedLibraries):
                if len(sortedLibraries) != 0 and singupDays == 0:
                    l = sortedLibraries.pop(0)
                    singupDays = l.time+1

        #Quan acaba de registrarse se afegix a singupDays
        singupDays -= 1
        if singupDays == 0:
            singupLibraries.append(l)

        for pos, li in enumerate(singupLibraries):
            num = li.nbooks_scanned
            for index_book in range(num):
                if len(li.books) == 0:
                    singupLibraries.pop(pos)
                    break
                book = li.books.pop(0)
                if book not in booksScanned:
                    booksScanned.append(book)
                    score = score + book.score
    return score

def output(librerias, a):
    if a == 1:
        with open('a_out.txt', 'a') as the_file:
            the_file.write(str(len(librerias)))
            the_file.write("\n")
            #(librerias)
            for i in librerias:
                the_file.write(str(i.id) + ' ' + str(len(i.books)))
                the_file.write("\n")
                for b in i.books:
                    the_file.write(str(b.id) + ' ')
                the_file.write("\n")
    elif a == 2:
        with open('b_out.txt', 'a') as the_file:
            the_file.write(str(len(librerias)))
            the_file.write("\n")
            #(librerias)
            for i in librerias:
                the_file.write(str(i.id) + ' ' + str(len(i.books)))
                the_file.write("\n")
                for b in i.books:
                    the_file.write(str(b.id) + ' ')
                the_file.write("\n")
    elif a == 3:
        with open('c_out.txt', 'a') as the_file:
            the_file.write(str(len(librerias)))
            the_file.write("\n")
            #(librerias)
            for i in librerias:
                the_file.write(str(i.id) + ' ' + str(len(i.books)))
                the_file.write("\n")
                for b in i.books:
                    the_file.write(str(b.id) + ' ')
                the_file.write("\n")
    elif f == 4:
        with open('d_out.txt', 'a') as the_file:
            the_file.write(str(len(librerias)))
            the_file.write("\n")
            #(librerias)
            for i in librerias:
                the_file.write(str(i.id) + ' ' + str(len(i.books)))
                the_file.write("\n")
                for b in i.books:
                    the_file.write(str(b.id) + ' ')
                the_file.write("\n")
    elif f == 5:
        with open('e_out.txt', 'a') as the_file:
            the_file.write(str(len(librerias)))
            the_file.write("\n")
            #(librerias)
            for i in librerias:
                the_file.write(str(i.id) + ' ' + str(len(i.books)))
                the_file.write("\n")
                for b in i.books:
                    the_file.write(str(b.id) + ' ')
                the_file.write("\n")
    elif f == 6:
        with open('f_out.txt', 'a') as the_file:
            the_file.write(str(len(librerias)))
            the_file.write("\n")
            #(librerias)
            for i in librerias:
                the_file.write(str(i.id) + ' ' + str(len(i.books)))
                the_file.write("\n")
                for b in i.books:
                    the_file.write(str(b.id) + ' ')
                the_file.write("\n")

def main():
    inp = get_input_line()
    config = inp[0].strip('\n').split(' ')
    scores = inp[1].strip('\n').split(' ')
    data = inp[2:]
    libraries = get_libraries(data, scores)
    libraries.sort(key=lambda x: x.score, reverse=True)
    copia = libraries.copy()
    score = days(libraries, config)
    output(copia, 2)

if __name__ == '__main__':
    main()
