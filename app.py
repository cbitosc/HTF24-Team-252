import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# In-memory storage for registered users (for demonstration purposes)
users = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        
        # Simple validation
        if not name or not age or not phone or not email or not password:
            flash('All fields are required!')
            return redirect(url_for('register'))

        # Store user data (in a real app, you would store this in a database)
        users.append({'name': name, 'age': age, 'phone': phone, 'email': email, 'password': password})
        
        flash('Registration successful! You can now log in.')
        return redirect(url_for('home'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)