from flask import Flask, jsonify, request
from models import db, Books, Member
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/books', methods=['GET'])
def get_books()->jsonify:
    books = Books.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published': book.published
        }
        output.append(book_data)
    return jsonify({'books': output})

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id:int)->jsonify:
    book = Books.query.get(id)
    if not book:
        return jsonify({'message': 'No book found'})
    return jsonify({
        'title': book.title,
        'author': book.author,
        'published': book.published
    })

@app.route('/books', methods=['POST'])
def create_book()->jsonify:
    data = request.get_json()
    if data['title'] in [book.title for book in Books.query.all()]:
        return jsonify({'message': 'Book already exists'})
    try:
        published_date = datetime.strptime(data['published'], '%Y-%m-%d')
    except ValueError:
        return jsonify({'message': 'Invalid date format. Use YYYY-MM-DD'})
    new_book = Books(
        title=data['title'],
        author=data['author'],
        published=published_date
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'New Book Added'})

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id:int)->jsonify:
    book = Books.query.get(id)
    if not book:
        return jsonify({'message': 'No book found'})
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    try:
        published_date = datetime.strptime(data['published'], '%Y-%m-%d')
    except ValueError:
        return jsonify({'message': 'Invalid date format. Use YYYY-MM-DD'})
    book.published = published_date
    db.session.commit()
    return jsonify({'message': "Book Updated"})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id:int)->jsonify:
    book = Books.query.get(id)
    if not book:
        return jsonify({'message': 'No book found'})
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book Deleted Successfully'})

@app.route('/members', methods=['GET'])
def get_members()->jsonify:
    members = Member.query.all()
    output = []
    for member in members:
        member_data = {
            'id': member.id,
            'name': member.name,
            'email': member.email
        }
        output.append(member_data)
    return jsonify({'members': output})

@app.route('/members', methods=['POST'])
def create_member()->jsonify:
    data = request.get_json()
    if data['email'] in [member.email for member in Member.query.all()]:
        return jsonify({'message': 'Email already exists'})
    new_member = Member(name=data['name'],email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'New Member Added'})

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id:int)->jsonify:
    member = Member.query.get(id)
    if not member:
        return jsonify({'message': 'Member not found'})
    data = request.get_json()
    member.name = data['name']
    member.email = data['email']
    db.session.commit()
    return jsonify({'message': 'Member Updated'})

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id:int)->jsonify:
    member = Member.query.get(id)
    if not member:
        return jsonify({'message': 'Member not found'})
    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member Deleted'})

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id:int)->jsonify:
    member = Member.query.get(id)
    if not member:
        return jsonify({'message': 'Member not found'})
    return jsonify({'name': member.name,'email': member.email})

if __name__ == '__main__':
    app.run(debug=True)
