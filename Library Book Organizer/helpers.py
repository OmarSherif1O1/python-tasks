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

      