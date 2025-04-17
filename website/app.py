from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pandas as pd
import sys
import os

# Add the path of the 'data_collection' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_collection')))

# Now import load_data from collect_data
from collect_data import load_data

app = Flask(__name__)

# Load the data globally for easy access (CSV Data)
df = load_data()

# Home page with links
@app.route("/")
def index():
    return render_template('index.html')

# Search Data
import sqlite3
from flask import request, render_template


# Search Route
@app.route("/search", methods=["GET", "POST"])
def search_data():
    results = None
    if request.method == "POST":
        query = request.form['query'].lower()

        # Path to your SQLite database
        db_path = os.path.join("database", "elections.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Build a WHERE clause that searches across key text columns
        sql_query = """
            SELECT * FROM election_data
            WHERE 
                LOWER(Precinct) LIKE ? OR
                LOWER(Race) LIKE ? OR
                LOWER(LegislativeDistrict) LIKE ? OR
                LOWER(CountyCouncil) LIKE ? OR
                LOWER(CongressionalDistrict) LIKE ? OR
                LOWER(CounterGroup) LIKE ? OR
                LOWER(CounterType) LIKE ?
        """

        params = tuple(['%' + query + '%'] * 7)

        cursor.execute(sql_query, params)
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        conn.close()

    return render_template("search.html", results=results)

# View Data page (Fetch data from SQLite)
@app.route("/data")
def view_data():
    conn = sqlite3.connect("database/elections.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM election_data")
    data = cursor.fetchall()
    conn.close()

    # Convert data into a dictionary-like structure for rendering in the template
    columns = ['Precinct', 'Race', 'LegislativeDistrict', 'CountyCouncil', 
               'CongressionalDistrict', 'CounterGroup', 'CounterType', 'SumOfCount']
    data_dict = [dict(zip(columns, row)) for row in data]

    return render_template("view_data.html", data=data_dict)

# Insert Data page
@app.route("/insert_data", methods=["GET", "POST"])
def insert_data():
    if request.method == "POST":
        # Get the data from the form
        precinct = request.form["precinct"]
        race = request.form["race"]
        legislative_district = request.form["legislative_district"]
        county_council = request.form["county_council"]
        congressional_district = request.form["congressional_district"]
        counter_group = request.form["counter_group"]
        counter_type = request.form["counter_type"]
        
        # Ensure that sum_of_count is an integer
        try:
            sum_of_count = int(request.form["sum_of_count"])
        except ValueError:
            # Handle invalid sum_of_count (non-integer input)
            return "Invalid Sum of Count value. Please enter a valid number.", 400

        # Insert data into the SQLite database
        conn = sqlite3.connect("database/elections.db")
        cursor = conn.cursor()

        try:
            # SQL query to insert the data into the table
            cursor.execute('''INSERT INTO election_data (
                Precinct, Race, LegislativeDistrict, CountyCouncil,
                CongressionalDistrict, CounterGroup, CounterType, SumOfCount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
            (precinct, race, legislative_district, county_council,
             congressional_district, counter_group, counter_type, sum_of_count))

            # Commit and close the connection
            conn.commit()
        except sqlite3.Error as e:
            # Handle any errors that occur during the database operation
            conn.rollback()
            return f"Database error: {e}", 500
        finally:
            conn.close()

        return redirect(url_for('view_data'))  # Redirect to the view data page

    return render_template('insert_data.html')

@app.route("/about")
def about_data():
    return render_template("about_data.html")

if __name__ == "__main__":
    app.run(debug=True)
