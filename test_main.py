from main import BooksCollector 
import pytest

@pytest.mark.parametrize ("books_dict",
    [                         
        {
            "Fantasy":"Фантастика",
            "Fantasy1":"Фантастика",
            "Comedy":"Комедии",
            "Horror":"Ужасы",
            "Detectives":"Детективы",
        }
    ]
    )
    
class TestBooksCollectorPositive:
    
    def test_add_new_book_correct_name_genre_added(self,books_dict,filled_book):
        for name, genre in books_dict.items():    
            assert filled_book.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_genre_books(self,filled_book):
        result = filled_book.get_books_with_specific_genre("Фантастика")    
        assert len(result)==2 and "Fantasy" in result and "Fantasy1" in result

    def test_get_books_for_children_genre_books_age_rating(self,filled_book,books_dict):
        result = filled_book.get_books_for_children()    
        for name, genre in books_dict.items():
            if genre != 'Ужасы' and genre != 'Детективы':
                assert name in result

    def test_add_book_in_favorites_book_list(self,filled_book,books_dict):
        for name in books_dict.keys():
            filled_book.add_book_in_favorites(name)
            assert name in filled_book.get_list_of_favorites_books()

    def test_delete_book_in_favorites_book_empty_list(self,filled_book,books_dict):
        for name in books_dict.keys():
            filled_book.add_book_in_favorites(name)
            filled_book.delete_book_from_favorites(name)
            assert name not in filled_book.get_list_of_favorites_books()            


class TestBooksCollectorNegative:
    @pytest.mark.parametrize ("bad_name",
    [
        "",
        "bad_name_length_more_than_forty_one_symbols"
    ]
    )
    def test_add_new_book_bad_name_not_added(self,book,bad_name):
        book.add_new_book(bad_name)
        assert book.get_books_genre() == {}

    @pytest.mark.parametrize ("bad_name,bad_genre",
    [
        ["Bad_Fantasy","Фантастика"],
        ["Fantasy","Bad_Фантастика"]
    ]
    )
    def test_set_book_genre_bad_name_genre_not_added(self,book,bad_name,bad_genre):
        book.add_new_book("Fantasy")
        book.set_book_genre(bad_name,bad_genre)
        assert book.get_books_genre() == {"Fantasy":""}

    def test_get_books_with_specific_genre_bad_genre_empty_list(self,book):
        book.add_new_book("Fantasy")
        book.set_book_genre("Fantasy", "Фантастика") 
        result = book.get_books_with_specific_genre("123")    
        assert result == []

    @pytest.mark.parametrize ("books_dict",
    [                         
        {
            "Comedy":"Комедии",
            "Horror":"Ужасы",
            "Detectives":"Детективы",
        }
    ]
    )
    def test_get_books_for_children_genre_books_age_rating(self,filled_book,books_dict):
        result = filled_book.get_books_for_children()     
        for name, genre in books_dict.items():
            if genre == 'Ужасы' or genre == 'Детективы':
                assert name not in result        

    def test_add_book_in_favorites_wrong_book_empty_list(self,book):
        book.add_book_in_favorites("123")
        assert "123" not in book.get_list_of_favorites_books()

    def test_delete_book_in_favorites_wrong_book_book_not_deleted(self,book):
        book.add_new_book("Fantasy")
        book.add_book_in_favorites("Fantasy")
        book.delete_book_from_favorites("123")
        assert book.get_list_of_favorites_books() == ["Fantasy"] 