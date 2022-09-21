from flask import Flask,jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import create_engine,Column,Integer,String

# callling the flask application
app= Flask(__name__)

# MySQL users:
engine = create_engine('sqlite:///orms.db')
# [DB_TYPE]+[DB_
# cdCONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]

connection =engine.connect()

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# create a base clase which is declarative
Base = declarative_base()

app = Flask(__name__)
# api 
@app.route('/api/')
def index():
    return "Flask API-Application Programming Interface"

#users database
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key = True)
    name = Column(String(60))
    burrowed_book_id = Column(Integer)
    def __repr__(self) -> str:
        return super().__repr__()

#BOOK
class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer,primary_key=True)
    book_name = Column(String(60), nullable =False)
    book_author_name = Column(String(60),nullable = False)
    book_category = Column(String(60),nullable =False)
    book_description = Column(String(255),nullable = False)

    def __repr__(self) -> str:
         return super().__repr__()

#create table
@app.route('/create_table/',methods=['GET'])
def create_table():
        Base.metadata.create_all(engine)
        return jsonify({
            'status':200,
            'message':'Tables Successfully created.',
            'tables':engine.table_names()
       })

#insert users
@app.route('/insert_user/',methods = ['GET'])
def insert_user():
    try:
        query = session.query(User).filter_by(name='Joey Tribiani')
        count = query.count()
        user = User(id=8,name='Joey Tribiani',burrowed_book_id=80)
        if count<=2:
            session.add(user)
            session.commit()
            return jsonify({
                'status':200,
                "message":"User added successfully"
                })
        else:
            return({
                'status':404,
                'message':'User have already accessed 3 books'
                })    
    except:
        return({
            'status':404,
            'message':'Error'
            }) 


#insert book
@app.route('/insert_book/<int:book_id>',methods=['GET'])
def insert_book(book_id):
    try:
        books = Book(book_id,book_category='Drama',book_description='Descp of the book.',book_name='Hello World',booK_author_name='Olie Watkins')
        session.add(books)
        session.commit()
        return jsonify({
            'message':'New Book added to library',
            'book_id':books.book_id,
            'book_name':books.book_name,
            'author':books.book_author_name,
            'description':books.book_description,
    })
    except:
        return jsonify({
            'status':404,
            'message':'Book is already in the list'
            })


#RETURNED BOOK
@app.route('/return/<int:book_id>',methods=['GET'])
def return_book(book_id):
    try:
        sql = '''
        DELETE  FROM userdetails
        WHERE burrowed_book_id = {0};
        '''.format(book_id)
        with engine.connect() as conn:
            query = conn.execute(sql)    
            session.commit()     
            df = pd.DataFrame(query.fetchall())
    
        return jsonify({
            'status':200,
            'message':'Book returned'
            })
   
    except:
        return jsonify({
            'status':404,
            'message':'Error'
            })
        
   
#book_list
@app.route('/book_list',methods = ['GET'])
def book_list():
    try:
        sql = '''
            SELECT book_name, count(book_name) AS  Number_of_books
            FROM book
            GROUP BY  book_name;
            '''
        with engine.connect() as conn:
            query = conn.execute(sql)         
            df = pd.DataFrame(query.fetchall())
            session.commit()
        
        return jsonify({
                'status':200,
                'message':'Book returned'
                })
    except:
        return jsonify({
            'status':404,
            'message':'Error'
            })
        

#Show Books According to Catgories   
@app.route('/category',methods = ['GET'])
def catagory():
    try:
        sql = '''
        SELECT u.user_name, count(burrowed_book_id) AS Burrowed_books
        FROM userdetails u
        LEFT JOIN book b
        ON u.burrowed_book_id = b.book_id AND b.category IN ('Fantasy and Adventure','Drama')
        GROUP BY user_name
        '''
        with engine.connect() as conn:
            query = conn.execute(sql)         
            df = pd.DataFrame(query.fetchall())
            session.commit()
            print(df)
        return jsonify({
            'status':200,
            'message':"book list"
            })
    except:
        return jsonify({
            'status':404,
            'message':'Error'
            })


#Books which is famous among users[top 5] 
@app.route('/top_five',methods = ['GET'])
def top_five():
    try:
        sql = '''
            SELECT u.user_name, count(burrowed_book_id) AS Burrowed_books, b.category
            FROM userdetails u
            LEFT JOIN book b
            ON u.burrowed_book_id = b.book_id
            GROUP BY user_name
            ORDER BY Burrowed_books DESC ;
            '''
        with engine.connect() as conn:
            query = conn.execute(sql)         
            df = pd.DataFrame(query.fetchall())
            session.commit()
            print(df)
        
        return jsonify({
                'status':200,
                'message':"book list"
                })
    except:
        return jsonify({
            'status':404,
            'message':'Error'
            })

#update Book 
@app.route('/update/',methods = ['GET'])
def update(): 
    try:
        sql = '''UPDATE book
                set  book_name ='Jon Doe'
                WHERE book_id NOT IN (SELECT burrowed_book_id FROM userdetails)'''
        sql1 = '''SELECT * FROM book'''        
        with engine.connect() as con:
            query = con.execute(sql)
            query = con. execute(sql1)
            session.commit()
            df = pd.DataFrame(query.fetchall())
            print(df)    
        
        return jsonify({
            'status':200,
            'message':'Book Name Updated Successfully'
            })
    except:
        return jsonify({
            'status':404,
            'message':'Error'
            })
     

if __name__ == '__main__':
    app.run(debug=True)