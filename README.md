# BookProjectFlask
Framework:Flask Restplus
Database:MongoDB

To run the project use command: flask run

APIs - Requests and Responses

Request Method : GET (Search Fields - Author Name,Book Name)

Url - http://127.0.0.1:5000/booklist/  (Complete List of Books)
Search key:book,author
Response - status 200 ok
Url - http://127.0.0.1:5000/bookdetail/<objectId>(Particular Book)
Response - status 200 ok

Request Method : POST

Url - http://127.0.0.1:5000/bookcreate/
Body - 
	 {
        "book_name": "Anna Karenina",
        "author_name": “Leo Tolstoy”,
        "price": 500,
        "summary": "The story centers on an extramarital affair between Anna and dashing cavalry officer Count Alexei Kirillovich Vronsky that scandalizes the social circles of Saint Petersburg and forces the young lovers to flee to Italy in a search for happiness, but after they return to Russia, their lives further unravel."
    }

Response - status 201 created


Request Method : PUT

Url - http://127.0.0.1:5000/bookupdate/<objectId>
Body - 
	 {
        "book_name": "Anna- Karenina",
        "author_name": “Leo Tolstoy”,
        "price": 600,
        "summary": "The story centers on an extramarital affair between Anna and dashing cavalry officer Count Alexei Kirillovich Vronsky that scandalizes the social circles of Saint Petersburg and forces the young lovers to flee to Italy."
    }


Response - status 200 ok


Request Method : PATCH

Url - http://127.0.0.1:5000/bookupdate/<objectId>
Body - {
 "price": 650
 
}

Response - status 200 ok




Request Method : DELETE

Url - http://127.0.0.1:5000/bookdelete/<objectId>
Response - status 204 no content

Additional features: Search book list by author name and book name,
Search key:book,author
