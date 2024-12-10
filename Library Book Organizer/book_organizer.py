from helpers import (
    count_books_by_genre,
    get_longest_title,
    list_unique_authors,
    search_by_keyword,
    books_by_author,
)


books = [
    "1984 by George Orwell (Dystopian)",
    "Pride and Prejudice by Jane Austen (Romance)",
    "To Kill a Mockingbird by Harper Lee (Classic)",
    "The Great Gatsby by F. Scott Fitzgerald (Classic)",
    "Moby Dick by Herman Melville (Adventure)",
    "Brave New World by Aldous Huxley (Dystopian)",
    "The Catcher in the Rye by J.D. Salinger (Classic)",
    "The Hobbit by J.R.R. Tolkien (Fantasy)",
    "The Shining by Stephen King (Horror)",
    "War and Peace by Leo Tolstoy (Historical Fiction)",
    "Crime and Punishment by Fyodor Dostoevsky (Psychological Fiction)",
    "The Odyssey by Homer (Epic)",
    "Frankenstein by Mary Shelley (Gothic)",
    "The Picture of Dorian Gray by Oscar Wilde (Philosophical Fiction)",
]
while True:
    user_input = int(input("what opreation u need to do \n 1:Catalog Analysis \n 2:Catalog Transformation \n 0:to exit \n"))
    if user_input == 1:
        while True:
            user_input = int(input("do u want \n 1:Count Books by Genre \n 2:Identify Longest Title \n 3:List Unique Authors \n 0:to exit this menu \n"))
            if user_input == 1:
                genre_dict = count_books_by_genre(books)
                for genre, count in genre_dict.items():
                    print (f"{genre} : {count}")
            elif user_input == 2:
                print('the longest title is : ',get_longest_title(books))
            elif user_input == 3:
                authors_dict = list_unique_authors(books)
                for authors, count in authors_dict.items():
                    print ("-",authors)
            elif user_input == 0:
                break
    elif user_input == 2:
        while True:
            user_input = int(input("do u want \n 1:Search by Keyword \n 2:Convert Titles to Uppercase \n 3:Reorganize by Author \n 0:to exit this menu \n"))
            if user_input == 1:
                print('Books matching: ',search_by_keyword(books))

            elif user_input == 2:
                uppercase_books = list(map(str.upper, books))
                for book in uppercase_books:
                    print(f"• {book}")
            elif user_input == 3:
                print('a list of authors and there books for u \n',books_by_author(books))
