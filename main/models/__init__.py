from main import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique= True)
    password = db.Column(db.String(300))
    webpages = db.relationship('Webpage', backref='user', lazy=True)
    journal_articles = db.relationship('JournalArticle', backref='user', lazy=True)
    books = db.relationship('Book', backref='user', lazy=True)

    def __repr__(self) -> str:
        return f"{self.id}-{self.username}"
    
class Webpage(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(200))
    desc = db.Column(db.String(1000))
    dop = db.Column(db.DateTime)
    url = db.Column(db.String(300))
    author1fname = db.Column(db.String(100))
    author1lname = db.Column(db.String(100))
    author2fname = db.Column(db.String(100))
    author2lname = db.Column(db.String(100))
    author3fname = db.Column(db.String(100))
    author3lname = db.Column(db.String(100))
    author4fname = db.Column(db.String(100))
    author4lname = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.id}-{self.name}"

class JournalArticle(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200))
    name = db.Column(db.String(200))
    author1fname = db.Column(db.String(100))
    author1lname = db.Column(db.String(100))
    author2fname = db.Column(db.String(100))
    author2lname = db.Column(db.String(100))
    author3fname = db.Column(db.String(100))
    author3lname = db.Column(db.String(100))
    author4fname = db.Column(db.String(100))
    author4lname = db.Column(db.String(100))
    publicatinStatus = db.Column(db.Boolean, default=False)
    dop = db.Column(db.DateTime)    #date of publishing
    libDatabase = db.Column(db.String(50))
    pageRange = db.Column(db.String(20))
    doi = db.Column(db.String(15))  #database object identifier
    url = db.Column(db.String(300))
    articleNo = db.Column(db.String(15))
    
    def __repr__(self) -> str:
        return f"{self.id}-{self.name}"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200))
    author1fname = db.Column(db.String(100))
    author1lname = db.Column(db.String(100))
    author2fname = db.Column(db.String(100), nullable = True)
    author2lname = db.Column(db.String(100), nullable = True)
    author3fname = db.Column(db.String(100), nullable = True)
    author3lname = db.Column(db.String(100), nullable = True)
    author4fname = db.Column(db.String(100), nullable = True)
    author4lname = db.Column(db.String(100), nullable = True)
    edition = db.Column(db.Integer)
    volume = db.Column(db.String(10))
    dop = db.Column(db.Date)    #date of publishing
    publisher = db.Column(db.String(100))
    countryOfPublication = db.Column(db.String(50))
    stateOfPublication = db.Column(db.String(50))
    cityOfPublication = db.Column(db.String(50))
    doi = db.Column(db.String(15))  #database object identifier
    url = db.Column(db.String(300))
    isbn = db.Column(db.Integer)
    issn = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"{self.id}-{self.title}"
    
with app.app_context():
    db.create_all()