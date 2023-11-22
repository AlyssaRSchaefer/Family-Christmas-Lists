from flask import Flask, send_file, render_template, request, redirect, session, send_from_directory
import mysql

app = Flask(__name__)
# Database configuration
db_config = {
    'host': '127.0.0.1',     
    'user': 'root',
    'password': 'password',
    'database': 'christmas',
}

# Create a connection to the database
conn = pymysql.connect(**db_config)

# Function to execute SQL queries
def execute_query(query, params=None):
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
    return result

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Example query
        query = "SELECT * FROM users WHERE name = %s AND password = %s;"
        params = (username, password)
        result = execute_query(query, params)

        # Process the result
        if result:
            print("Login successful!")
            currentUser = username #update currentUser on login
            return render_template('lists.html')
        else:
            print("Login failed!")

    return render_template('login.html')

@app.route('/Family-Christmas-Lists/templates/lists.html')
def lists():
    return render_template('lists.html')

@app.route('/listcontent')
def listcontent():
    return render_template('listcontent.html')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)
