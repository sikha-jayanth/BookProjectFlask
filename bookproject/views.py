
from flask import Flask
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request,Blueprint
from .extensions import mongo
bp=Blueprint('bp',__name__)


#to add a new book to collection
@bp.route('/bookcreate',methods=['POST'])
def add_book():
    _json=request.json
    book_name=_json['book_name']
    author_name=_json['author_name']
    price=_json['price']
    summary=_json['summary']
    if book_name and author_name and price and summary and request.method=='POST':
        id=mongo.db.book.insert({'book_name':book_name,'author_name':author_name,'price':price,'summary':summary})
        resp=jsonify("Book added succesfully")
        resp.status_code=200
        return resp
    else:
        return not_found()

@bp.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message':'Not Found'+request.url
    }
    resp=jsonify(message)
    resp.status_code=404
    return resp

#to view all books and search using 'book' or 'author'
@bp.route('/booklist')
def list_books():
    if request.args:
        book=request.args.get('book')
        author=request.args.get('author')
        output = []
        for q in mongo.db.book.find({"$or":[{'book_name':book},{'author_name':author}]}):
            output.append({'book_name' : q['book_name'], 'author_name' : q['author_name'],'price':q['price'],'summary':q['summary']})
        if output:
            return jsonify({'result' : output})
        else:
            return not_found()
    else:
        books=mongo.db.book.find()
        resp=dumps(books)
        return resp

#to view details of a particular book
@bp.route('/bookdetail/<id>')
def book_detail(id):
    book=mongo.db.book.find({'_id':ObjectId(id)})
    resp=dumps(book)
    return resp

#to view delete a particular book
@bp.route('/bookdelete/<id>',methods=['DELETE'])
def delete_book(id):
    mongo.db.book.delete_one({'_id':ObjectId(id)})
    resp=jsonify("book deleted successully")
    resp.status_code=200
    return resp

#to update details of a particular book
@bp.route('/bookupdate/<id>',methods=["PUT","PATCH"])
def update_book(id):
    _id=id
    data = request.json
    if not data:
        abort(400, 'No data received')

    try:
        mongo.db.book.update_one({'_id': ObjectId(_id)}, {'$set': data})
    except Exception as e:
        print (e)

    return {'Message' : 'The book is updated'}

