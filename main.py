from flask import Flask, request, redirect, render_template, session
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'K>~EEAnH_x,Z{q.43;NmyQiNz1^Yr7'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect the table choice from the form. Store it in a session cookie.
        session['table'] = request.form['table']

        # Based on the table choice, assign the column names to the session.
        # These will be displayed on each of the other the web forms.
        if session['table'] == 'movies':
            session['columns'] = ['movie_id', 'title', 'year_released', 'director']
        else:
            session['columns'] = ['director_id', 'last_name', 'first_name']

        # Request the chosen SQL option from the form, and use it to build the query_type string.
        query_type = '/' + request.form['query_type'].lower()

        # Use the query_type string to redirect control to the proper function.
        return redirect(query_type)
    else:
        # The query_types list is used to create the labels for the form on the home page.
        query_types = ['INSERT', 'SELECT', 'UPDATE', 'DELETE']
        
        # Remove old data from the session cookie.
        session.clear()

    return render_template("index.html", tab_title = "Movie SQL Project", query_types = query_types, home = True)

@app.route('/insert', methods=['GET', 'POST'])
def insert_query():
    return render_template("insert.html", tab_title = "INSERT query", home = False)

@app.route('/select', methods=['GET', 'POST'])
def select_query():
    return render_template("select.html", tab_title = "SELECT query", home = False)

@app.route('/update', methods=['GET', 'POST'])
def update_query():
    return render_template("update.html", tab_title = "UPDATE query", home = False)

@app.route('/delete', methods=['GET', 'POST'])
def delete_query():
    return render_template("delete.html", tab_title = "DELETE query", home = False)

if __name__ == '__main__':
    app.run()