from flask import Flask, render_template, flash, redirect, url_for, session, request, logging ,send_from_directory
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField
from passlib.hash import sha256_crypt
from functools import wraps
import os
#from additemform import additemForm
import pymysql


app = Flask(__name__)



# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '302final'
app.config['MYSQL_PASSWORD'] = '302final'
app.config['MYSQL_DB'] = '302final'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)





# Index
@app.route('/')
def index():
    return render_template('home.html')

# Ordersuccess
@app.route('/ordersuccess')
def ordersuccess():
    return render_template('ordersuccess.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')


	
# Register Form Class
class RegisterForm(Form):
    rootpassword = PasswordField('Root Password', [validators.DataRequired()])
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        rootpassword = form.rootpassword.data
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        if rootpassword == '302final':
            # Create cursor
            cur = mysql.connection.cursor()

            # Execute query
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

            # Commit to DB
            mysql.connection.commit()

            # Close connection
            cur.close()

            flash('You are now registered and can log in', 'success')
            return redirect(url_for('login'))
        else:
            flash('Root password wrong')
    return render_template('register.html', form=form)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html')


@app.route("/import")
def importcsvhtml():
    return render_template("import.html")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/import", methods=["POST"])

def importcsv():
    target = os.path.join(APP_ROOT, 'csv/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if (ext == ".csv"):
            print("File supported moving on...")
        else:
            render_template("login.html", message="Files uploaded are not supported...")
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        f = open(os.path.join(target ,filename), "r")
        # fString = f.read()
        #fileDir = os.path.dirname(os.path.realpath('__file__'))
        #f = open(os.path.join(fileDir, target+filename), "r")
        fString = f.read()

        fList = []
        for line in fString.split('\n'):
            fList.append(line.split(','))

        # shipping_id = fList[0][0]; item_id = fList[0][1]; quantity = fList[0][2]; weight_KG = fList[0][3]
        # shipper_name = fList[0][4]; shipper_email = fList[0][5]; receiver_name = fList[0][6]; receiver_address = fList[0][7]
        # receiver_contact = fList[0][8]

        del fList[0]

        rows = ''
        for i in range(len(fList) - 1):
            rows += "('{}','{}',{},{},'{}','{}','{}','{}','{}')".format(fList[i][0], fList[i][1],fList[i][2], fList[i][3], fList[i][4], fList[i][5],fList[i][6], fList[i][7], fList[i][8])
            if i != len(fList) - 2:
                rows += ','
        #print("insert into ship values" + rows)

        cur = mysql.connection.cursor()
        insertsql = "insert into ship(shipping_id, item_id, quantity, weight_KG, shipper_name, shipper_email, receiver_name, receiver_address, receiver_contact) VALUES"+ rows
        print (insertsql)
        cur.execute(insertsql)
        mysql.connection.commit()
        cur.close()
        #try:
            #cur.execute(insertsql)
            #mysql.connection.commit()
            #cur.close()
            #db.commit()
        #except:
            #mysql.connection.rollback()
        #mysql.connection.close()

        #return render_template("import.html")
    # return send_from_directory("csv", filename, as_attachment=True)
    return render_template("import.html")

class additemForm(Form):
    item1 = IntegerField('item1', [validators.NumberRange(min=0, max=99999999)], default=0)
    item2 = IntegerField('item2', [validators.NumberRange(min=0, max=99999999)], default=0)
    item3 = IntegerField('item3', [validators.NumberRange(min=0, max=99999999)], default=0)
    item4 = IntegerField('item4', [validators.NumberRange(min=0, max=99999999)], default=0)
@app.route('/stock',methods = ['POST', 'GET'])
def stock():
    form = additemForm(request.form)
    if request.method == 'POST' and form.validate():
        item1 = form.item1.data
        item2 = form.item2.data
        item3 = form.item3.data
        item4 = form.item4.data
        if item1 > 0:
            cursor = mysql.connection.cursor()
            sql11 = ('INSERT INTO additem(item_id, quantity) VALUES("item1", %s)' % (item1))
            print(sql11)
            cursor.execute(sql11)
            mysql.connection.commit()
            cursor.close()
        if item2 > 0:
            cursor = mysql.connection.cursor()
            sql22 = ('INSERT INTO additem(item_id, quantity) VALUES("item2", %s)' % (item2))
            print(sql22)
            cursor.execute(sql22)
            mysql.connection.commit()
            cursor.close()
        if item3 > 0:
            cursor = mysql.connection.cursor()
            sql33 = ('INSERT INTO additem(item_id, quantity) VALUES("item3", %s)' % (item3))
            print(sql33)
            cursor.execute(sql33)
            mysql.connection.commit()
            cursor.close()
        if item4 > 0:
            cursor = mysql.connection.cursor()
            sql44 = ('INSERT INTO additem(item_id, quantity) VALUES("item4", %s)' % (item4))
            print(sql44)
            cursor.execute(sql44)
            mysql.connection.commit()
            cursor.close()

        #cursor.execute("INSERT INTO stock(item_id, quantity) VALUES(item4, %s)", (item4))


        return redirect(url_for('stock'))

    cursor = mysql.connection.cursor()

    history = 'select * from ship'
    cursor.execute(history)
    rows = cursor.fetchall()   # data from database
    cursor.close()

    cursorh = mysql.connection.cursor()
    history2 = 'select * from additem'
    cursorh.execute(history2)
    rows2 = cursorh.fetchall()  # data from database
    cursorh.close()

    cursor1a = mysql.connection.cursor()
    item1add = 'select sum(quantity) from additem where item_id = "item1"'
    cursor1a.execute(item1add)
    item1addd = cursor1a.fetchall()
    cursor.close()

    cursor2a = mysql.connection.cursor()
    item2add = 'select sum(quantity) from additem where item_id = "item2"'
    cursor2a.execute(item2add)
    item2addd = cursor2a.fetchall()
    cursor.close()

    cursor3a = mysql.connection.cursor()
    item3add = 'select sum(quantity) from additem where item_id = "item3"'
    cursor3a.execute(item3add)
    item3addd = cursor3a.fetchall()
    cursor.close()

    cursor4a = mysql.connection.cursor()
    item4add = 'select sum(quantity) from additem where item_id = "item4"'
    cursor4a.execute(item4add)
    item4addd = cursor4a.fetchall()
    cursor.close()



    cursor1 = mysql.connection.cursor()
    item1ship = 'select sum(quantity) from ship where item_id = "item1"'
    cursor1.execute(item1ship)
    item1shipp = cursor1.fetchall()
    cursor.close()

    cursor2 = mysql.connection.cursor()
    item2ship = 'select sum(quantity) from ship where item_id = "item2"'
    cursor2.execute(item2ship)
    item2shipp = cursor2.fetchall()
    cursor.close()

    cursor3 = mysql.connection.cursor()
    item3ship = 'select sum(quantity) from ship where item_id = "item3"'
    cursor3.execute(item3ship)
    item3shipp = cursor3.fetchall()
    cursor.close()

    cursor4 = mysql.connection.cursor()
    item4ship = 'select sum(quantity) from ship where item_id = "item4"'
    cursor4.execute(item4ship)
    item4shipp = cursor4.fetchall()
    cursor.close()

    cursor111 = mysql.connection.cursor()
    item1stock = 'select additem-ship as stock from (select sum(quantity) as additem from additem where item_id = "item1") as additem,' \
                 ' (select sum(quantity) as ship from ship where item_id = "item1") as ship;'
    cursor111.execute(item1stock)
    item1stockk = cursor111.fetchall()
    cursor.close()

    cursor222 = mysql.connection.cursor()
    item2stock = 'select additem-ship as stock from (select sum(quantity) as additem from additem where item_id = "item2") as additem,' \
                 ' (select sum(quantity) as ship from ship where item_id = "item2") as ship;'
    cursor222.execute(item2stock)
    item2stockk = cursor222.fetchall()
    cursor.close()

    cursor333 = mysql.connection.cursor()
    item3stock = 'select additem-ship as stock from (select sum(quantity) as additem from additem where item_id = "item3") as additem,' \
                 ' (select sum(quantity) as ship from ship where item_id = "item3") as ship;'
    cursor333.execute(item3stock)
    item3stockk = cursor333.fetchall()
    cursor.close()

    cursor444 = mysql.connection.cursor()
    item4stock = 'select additem-ship as stock from (select sum(quantity) as additem from additem where item_id = "item4") as additem,' \
                 ' (select sum(quantity) as ship from ship where item_id = "item4") as ship;'
    cursor444.execute(item4stock)
    item4stockk = cursor444.fetchall()
    cursor.close()


    #item1stock = item1addd-item1shipp
    #print(item1stock)
    return render_template("stock.html", rows=rows, rows2=rows2, form=form, item1shipp=item1shipp,
                           item2shipp=item2shipp, item3shipp=item3shipp, item4shipp=item4shipp,
                           item1addd=item1addd, item2addd=item2addd, item3addd=item3addd, item4addd=item4addd,
                           item1stockk=item1stockk, item2stockk=item2stockk, item3stockk=item3stockk, item4stockk=item4stockk)
def csvtosql():
    # f = open(os.path.join('cvs' ,'order2.cvs'), "r")
    # fString = f.read()
    filename = upload.filename
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    f = open(os.path.join(fileDir, filename), "r")
    fString = f.read()

    fList = []
    for line in fString.split('\n'):
        fList.append(line.split(','))

    # shipping_id = fList[0][0]; item_id = fList[0][1]; quantity = fList[0][2]; weight_KG = fList[0][3]
    # shipper_name = fList[0][4]; shipper_email = fList[0][5]; receiver_name = fList[0][6]; receiver_address = fList[0][7]
    # receiver_contact = fList[0][8]

    del fList[0]

    rows = ''
    for i in range(len(fList) - 1):
        rows += "('{}','{}',{},{},'{}','{}','{}','{}','{}')".format(fList[i][0], fList[i][1],
                                                                    fList[i][2], fList[i][3], fList[i][4], fList[i][5],
                                                                    fList[i][6], fList[i][7], fList[i][8])
        if i != len(fList) - 2:
            rows += ','
    print("insert into ship values" + rows)

# stock
#@app.route('/stock')
#def check():
    #return render_template('stock.php')



if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
