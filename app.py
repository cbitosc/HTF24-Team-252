from Flask import Flask, request, render_template, redirect, url_for 
import sqlite3

app = Flask(__name__)

# Function to initialize the database
def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']

    # Basic validation (you can add more as needed)
    if not name or not age or not phone or not email or not password:
        return "All fields are required!", 400

    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (name, age, phone, email, password) VALUES (?, ?, ?, ?, ?)',
                           (name, age, phone, email, password))
            conn.commit()
    except sqlite3.IntegrityError:
        return "Email already exists!", 400

    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)