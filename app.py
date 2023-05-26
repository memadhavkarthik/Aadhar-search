from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL configuration
mysql_config = {
  'host': 'aadharkarthik.cfiydt5tiqgp.eu-north-1.rds.amazonaws.com',
  'user': 'admin',
  'password': 'Bahubali',
  'database': 'aadharkarthik'
}


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
  if request.method == 'POST':
    # Get the form data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Connect to MySQL database
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # Insert the data into the users table
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/success')

  return render_template('registration.html')


@app.route('/success')
def success():
  return render_template('success.html')


@app.route('/login')
def login():
  return render_template('login.html')


@app.route('/upload')
def upload():
  return render_template('upload.html')


if __name__ == '__main__':
  app.run()
