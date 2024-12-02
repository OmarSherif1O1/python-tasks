def count_books_by_genre(books):
    genre_dict = {}
    for book in books:
        index = book.find('(')
        genre = book[index+1:-1]
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1 
    return genre_dict  

def get_longest_title(books):
    longest_title = ""
    for book in books:
        current_book_title_index = book.find(' by')
        if len(book) > len(longest_title):
            longest_title = book[0:current_book_title_index]
    return longest_title

def list_unique_authors(books):
    authors_dict = {}
    for book in books:
        start_of_author = book.find('by ')
        end_of_author = book.find('(')
        authors = book[start_of_author+3 : end_of_author-1]
        if authors in authors_dict:
            authors_dict[authors] += 1
        else:
            authors_dict[authors] = 1 
    return authors_dict

        



      