from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from main import app, db
from main.models import User, Book, JournalArticle, Webpage
from datetime import date

@app.route("/", methods=['GET','POST'])
@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('user_id') != None:
            userid = session['user_id']
            books =  Book.query.filter_by(userId= userid ).all()
            journalArticles = JournalArticle.query.filter_by(userId= userid ).all()
            webpages = Webpage.query.filter_by(userId= userid ).all()
            return render_template('dashboard.html', books = books, journalArticles = journalArticles, webpages = webpages)
    return render_template('login.html') 

@app.route("/register", methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route("/userRegistered", methods=['POST'])
def userRegistered():
    if request.method == 'POST':
        username= request.form.get('username')
        email= request.form.get('email')
        password= request.form.get('password')
        user = User.query.filter_by(username=username).first()
        newEmail = User.query.filter_by(email=email).first()
        
        if user or newEmail:
            error = "username or email already exist"
            return render_template('register.html', error = error)
            
        newUser = User(username = username, email = email, password = password)
        db.session.add(newUser)
        db.session.commit()
        print(newUser)

    return render_template('login.html')

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    print(session.get('user_id'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        print(user)
        if user:
            session['user_id'] = user.id
            userid = session['user_id']
            books =  Book.query.filter_by(userId= userid ).all()
            journalArticles = JournalArticle.query.filter_by(userId= userid ).all()
            webpages = Webpage.query.filter_by(userId= userid ).all()
            return render_template('dashboard.html', books = books, journalArticles = journalArticles, webpages = webpages)
        else:
            return render_template('login.html', error="Invalid username or password")
    elif session.get('user_id')!= None:
        userid = session['user_id']
        books =  Book.query.filter_by(userId= userid ).all()
        journalArticles = JournalArticle.query.filter_by(userId= userid ).all()
        webpages = Webpage.query.filter_by(userId= userid ).all()
        return render_template('dashboard.html', books = books, journalArticles = journalArticles, webpages = webpages)
    else:
        return render_template('login.html', error="Invalid username or password")

@app.route("/logout")
def logout():
    session.clear()
    return render_template('login.html')
    
@app.route("/books", methods=['GET','POST'])
def books():
    if session.get('user_id') != None :
        print("session :",session['user_id'])
        userid = session['user_id']
        books =  Book.query.filter_by(userId= userid ).all()
        print("Books:", books)
        return render_template('books.html')
    return render_template('login.html')

@app.route("/bookadded", methods=['GET','POST'])
def bookadded():
    print('check 1')
    if session['user_id'] == None:
        return render_template("login.html")

    if request.method == 'POST':
        userid = session['user_id']
        title = request.form.get('title')
        author1fname = request.form.get('author1fname')
        author1lname = request.form.get('author1lname')
        author2fname = request.form.get('author2fname')
        author2lname = request.form.get('author2lname')
        author3fname = request.form.get('author3fname')
        author3lname = request.form.get('author3lname')
        author4fname = request.form.get('author4fname')
        author4lname = request.form.get('author4lname')
        edition = request.form.get('edition')
        volume = request.form.get('volume')
        dd= request.form.get('dd')
        mm= request.form.get('mm')
        yyyy= request.form.get('yyyy')
        publisher = request.form.get('publisher')
        countryOfPublication = request.form.get('countryOfPublication')
        stateOfPublication = request.form.get('stateOfPublication')
        cityOfPublication = request.form.get('cityOfPublication')
        doi = request.form.get('doi')
        url = request.form.get('url')
        isbn = request.form.get('isbn')
        issn = request.form.get('issn')

        newBook = Book(userId = userid, title = title, author1fname = author1fname, author1lname = author1lname, author2fname = author2fname, author2lname = author2lname, author3fname = author3fname, author3lname = author3lname, author4fname = author4fname, author4lname = author4lname, edition = edition, volume = volume, dop = date(int(yyyy),int(mm),int(dd)), publisher = publisher, countryOfPublication = countryOfPublication, stateOfPublication = stateOfPublication, cityOfPublication = cityOfPublication, doi = doi, url = url, isbn = isbn, issn = issn)
        print("BOOK:",newBook)
        db.session.add(newBook)
        db.session.commit()

        return render_template("books.html")
    
    print('check 2')
    return render_template("books.html")

@app.route("/journalArticle", methods=['GET','POST'])
def journalArticle():
    if session.get('user_id') != None :
        print("session :",session['user_id'])
        # userid = session['user_id']
        # books =  Book.query.filter_by(userId= userid ).all()
        # print("Books:", books)
        return render_template('journalArticle.html')
    return render_template('login.html')

@app.route("/journaladded", methods=['GET','POST'])
def journaladded():
    print('check 1')
    if session['user_id'] == None:
        return render_template("login.html")

    if request.method == 'POST':
        userid = session['user_id']
        title = request.form.get('title')
        name = request.form.get('name')
        author1fname = request.form.get('author1fname')
        author1lname = request.form.get('author1lname')
        author2fname = request.form.get('author2fname')
        author2lname = request.form.get('author2lname')
        author3fname = request.form.get('author3fname')
        author3lname = request.form.get('author3lname')
        author4fname = request.form.get('author4fname')
        author4lname = request.form.get('author4lname')
        volume = request.form.get('volume')
        pubStatus =  request.form.get('pubStatus')
        if pubStatus == 'Published':
            pubStatus = True
        else:
            pubStatus= False
        dd= request.form.get('dd')
        mm= request.form.get('mm')
        yyyy= request.form.get('yyyy')
        libDatabase = request.form.get('libDatabase')
        pageRange = request.form.get('pageRange')
        doi = request.form.get('doi')
        url = request.form.get('url')
        articleNo = request.form.get('articleNo')

        newJournalArticle = JournalArticle(userId = userid, title = title,name = name, author1fname = author1fname, author1lname = author1lname, author2fname = author2fname, author2lname = author2lname, author3fname = author3fname, author3lname = author3lname, author4fname = author4fname, author4lname = author4lname, pubStatus = pubStatus, volume = volume, dop = date(int(yyyy),int(mm),int(dd)), libDatabase = libDatabase, pageRange = pageRange, doi = doi, url = url, articleNo = articleNo)
        print("Journal Article:",newJournalArticle)
        db.session.add(newJournalArticle)
        db.session.commit()

        return render_template("journalArticle.html")
    
    print('check 2')
    return render_template("journalArticle.html")

@app.route("/webpage", methods=['GET','POST'])
def webpage():
    if session.get('user_id') != None :
        print("session :",session['user_id'])
        # userid = session['user_id']
        # books =  Book.query.filter_by(userId= userid ).all()
        # print("Books:", books)
        return render_template('webpage.html')
    return render_template('login.html')

@app.route("/deleteBook/<int:id>")
def deleteBook(id):
    book = Book.query.filter_by(id = id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/dashboard")

@app.route("/deleteWebpage/<int:id>")
def deleteWebpage(id):
    webpage = Webpage.query.filter_by(id = id).first()
    db.session.delete(webpage)
    db.session.commit()
    return redirect("/dashboard")

@app.route("/deleteJournalArticle/<int:id>")
def deleteJournalArticle(id):
    journalArticle = JournalArticle.query.filter_by(id = id).first()
    db.session.delete(journalArticle)
    db.session.commit()
    return redirect("/dashboard")

@app.route("/webpageadded", methods=['GET','POST'])
def webpageadded():
    print('check 1')
    if session['user_id'] == None:
        return render_template("login.html")

    if request.method == 'POST':
        userid = session['user_id']
        name = request.form.get('name')
        title = request.form.get('title')
        desc = request.form.get('desc')
        author1fname = request.form.get('author1fname')
        author1lname = request.form.get('author1lname')
        author2fname = request.form.get('author2fname')
        author2lname = request.form.get('author2lname')
        author3fname = request.form.get('author3fname')
        author3lname = request.form.get('author3lname')
        author4fname = request.form.get('author4fname')
        author4lname = request.form.get('author4lname')
        ddp= request.form.get('ddp')
        mmp= request.form.get('mmp')
        yyyyp= request.form.get('yyyyp')
        dda= request.form.get('dda')
        mma= request.form.get('mma')
        yyyya= request.form.get('yyyya')
        url = request.form.get('url')

        newWebpage = Webpage(userId = userid, name = name,title = title, desc = desc, author1fname = author1fname, author1lname = author1lname, author2fname = author2fname, author2lname = author2lname, author3fname = author3fname, author3lname = author3lname, author4fname = author4fname, author4lname = author4lname, dop = date(int(yyyyp),int(mmp),int(ddp)),doa = date(int(yyyya),int(mma),int(dda)), url = url )
        print("Journal Article:",newWebpage)
        db.session.add(newWebpage)
        db.session.commit()

        return render_template("webpage.html")
    
    print('check 2')
    return render_template("webpage.html")
