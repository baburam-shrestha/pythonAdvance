# SET 3 (TEAM 3)  Library Management System.
# Users should be able to add books and their categories such as non-fiction, autobiography, and so on. 
# A book can belong to more than one category. Add users, each user should have a unique username. 
# A user can borrow up to 3 books at a time. A user can return any book he has borrowed at any time.  
# A book’s description, category, name, and author’s name can be updated only  if the book has not been borrowed. 
# Show total list of books(including count), show total users, 
# show books on the basis of category given[multiple categories can be provided], 
# show which book is famous among users[top 5], show which category of book users like most[show top 5].  
# On the basis of username, find the category of the book he/she prefers.
import imp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask import Flask,jsonify
from sqlalchemy import text
import pandas as pd
#import MySQLdb # pip install mysqlclient

# callling the flask application
app= Flask(__name__)

# MySQL users:

engine = create_engine('sqlite:///ormss.db')
# [DB_TYPE]+[DB_
# cdCONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]

connection =engine.connect()

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# create a base clase which is declarative
Base = declarative_base()

@app.route('/api/')
def index():
    return "Flask API-Application Programming Interface"

class User(Base): # to create the daabase from command line $ from orms import  User
    __tablename__ = 'users' 

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    burrowed_book_id = Column(Integer)

    def __repr__(self) -> str:
        return super().__repr__()

class Book(Base): # to create the daabase from command line $ from orms import  Book
    __tablename__ = 'books'

    book_id = Column(Integer,primary_key=True)
    book_name = Column(String(60), nullable =False)
    book_author_name = Column(String(60),nullable = False)
    book_category = Column(String(60),nullable =False)
    book_description = Column(String(255),nullable = False)
    
    def __repr__(self) -> str:
         return super().__repr__()

@app.route('/create_table/',methods=['GET'])
def create_table():
       Base.metadata.create_all(engine)
       print(engine.table_names())
       return jsonify({
        'status':200,
        'message':'Table Created Successfully!',
        'table':engine.table_names()
       })

# show users
@app.route('/show_user/',methods = ['GET'])
def show_user():
    query  = session.query(User).filter_by(name='Hari Tribiani')
    return jsonify({
        'status':200,
        'message':'User Found Successully!',
        })

# show books
@app.route('/show_book/',methods = ['GET'])
def show_book():
    query  = session.query(Book).filter_by(book_name='Hari Tribiani')
    return jsonify({
            'status':200,
            'message':'Book Found Successully!',
            })


# add insert user 
@app.route('/insert_user/',methods = ['GET','POST'])
def insert_user():
    query = session.query(User).filter_by(name='Hari Tribiani')
    count = query.count()
    user = User(id=count+1,name='Hari Tribiani',phone=9877732,email='adafa@fa.com',burrowed_book_id=40)
    if count <=2:
        session.add(user)
        session.commit()
        return jsonify({
            'status':200,
            'message':'User Added Successully!',
            })
    else:
        return jsonify({
            'status':404,
            'message':'Invalid User!',
            })

#add book to library
@app.route('/add_book/',methods=['GET'])
def add_book():
    insert_query = session.query(Book).filter_by(book_category='Drama and Love')
    count = insert_query.count()
    if count !=1:
        book = Book(book_id=32,book_category='Drama and Love',book_description='Descp of the book.',book_name='Hello World',book_author_name='Olie Watkins')
        session.add(book)
        session.commit()
        return jsonify({
            'status':200,
            'message':'New Book added to library',
            })
    else:
        return jsonify({
            'status':400,
            'message':'Already in a list'
            })

@app.route('/insert_book/',methods = ['GET','POST'])
def insert_book():
    insert_query = session.query(User).filter_by(name='Ramhari Shrestha')
    count = insert_query.count()     
    book = User(name='Ramhari Shrestha',phone=9875533, email='em@asfaf' , burrowed_book_id=80)
    if count < 3 :
        session.add(book)
        session.commit()
        return jsonify({
            'status':200,
            'message':'Book Insetted Successully!',

            })
    else:
        return jsonify({
            'status':400,
            'message':'Borrowing More Than 3 Book Isnot Allowed!'
            })

#return books
@app.route('/return_book/',methods=['GET'])
def return_book():
    try:
        book_id=32
        sql = '''
            DELETE  FROM users
            WHERE burrowed_book_id = {0};
            '''.format(book_id)
        with engine.connect() as conn:
            query = conn.execute(sql)    
            session.commit()     
            df = pd.DataFrame(query.fetchall())
        return jsonify({
            'status':200,
            'message':'Book Returned',
            'data':df,
            })
   
    except:
        return jsonify({
            'status':404,
            'message':'Error'
            })
        

#book list
@app.route('/book_list/',methods = ['GET'])
def book_list():
        sql = '''
            SELECT book_name, count(book_name) AS  Number_of_books
            FROM books
            GROUP BY  book_name;
            '''
        with engine.connect() as conn:
            query = conn.execute(sql)         
            df = pd.DataFrame(query.fetchall())
            session.commit()
        return jsonify({
            'status':200,
            'message':'Book list found',
            })

#Show Books According to Catgories   
@app.route('/book_category/',methods = ['GET'])
def book_cat():
        sql = '''
            SELECT u.name, count(burrowed_book_id) AS Burrowed_book
            FROM users u
            LEFT JOIN books b
            ON u.burrowed_book_id = b.book_id AND b.category IN ('Fantasy and Adventure','Drama')
            GROUP BY name
            '''
        with engine.connect() as conn:
            query = conn.execute(sql)         
            df = pd.DataFrame(query.fetchall())
            session.commit()
            print(df)
    
        return jsonify({
            'status':200,
            'mesasge':'Success',
            'data':df,
            })



#Books which is famous among users[top 5] 
@app.route('/top_5/',methods = ['GET'])
def top_5_famous():
        sql = '''
            SELECT u.user_name, count(burrowed_book_id) AS Burrowed_books, b.category
            FROM users u
            LEFT JOIN books b
            ON u.burrowed_book_id = b.book_id
            GROUP BY user_name
            ORDER BY Burrowed_books DESC ;
            '''
        with engine.connect() as conn:
            query = conn.execute(sql)         
            df = pd.DataFrame(query.fetchall())
            session.commit()
        return jsonify({
            'status':200,
            'mesasge':'Success',
            'data':df,
            })

#update books
@app.route('/update/',methods = ['PUT'])
def update_booklist():
    update_query = session.query(Book).filter_by(book_id=1).update(dict(book_name="Nepali"))
    session.commit()
    

    return jsonify({
        'msg':'success'})



#delete users
@app.route('/delete_user/',methods = ['DELETE'])
def delete_user():
    delete_query = session.query(User).filter_by(name='Hari Tribiani').delete()
    session.commit()
    return jsonify({
        'Deleted':delete_query
    })

#delete books
@app.route('/delete_book/',methods = ['DELETE'])
def delete_book():
    delete_query = session.query(User).filter_by(book_category='Drama and Love').delete()
    session.commit()
    return jsonify({
        'Deleted':delete_query
    })


if __name__ == '__main__':
    app.run(debug=True)
