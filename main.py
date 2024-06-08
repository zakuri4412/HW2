from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

#bai tap 1
@app.route('/get_file', methods=['GET'])
def get_file_content():
    file_path = 'file.txt'

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return jsonify({'content': file_content})
    except FileNotFoundError:
        return jsonify({'error': 'File not found'})


#bai tap 2
@app.route('/get_customers', methods=['GET'])
def get_customers():
    df = pd.read_csv('Telco-Customer-Churn.csv')
    sorted_customers = df.sort_values(by='MonthlyCharges', ascending=True).head(20)
    customers_json = sorted_customers.to_dict(orient='records')
    return jsonify(customers_json)


#bai tap 3
books = [
    {
    "id": 1, "title": 'a', "author": 'aa'
    },
{
    "id": 2, "title": 'b', "author": 'bb'
    },
{
    "id": 3, "title": 'c', "author": 'cc'
    },
]

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(book)
    return jsonify({'message': 'Book added successfully!'})

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book['id'] == book_id:
            book['title'] = data.get('title', book['title'])
            book['author'] = data.get('author', book['author'])
            return jsonify({'message': 'Book updated successfully!'})
    return jsonify({'error': 'Book not found'})


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message': 'Book deleted successfully!'})
    return jsonify({'error': 'Book not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)