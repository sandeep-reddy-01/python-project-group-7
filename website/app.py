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

#Helper function to get the correct path to the database
def get_db_connection():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_collection', 'elections.db'))
    return sqlite3.connect(db_path)

# Home page with links
@app.route("/")
def index():
    return render_template('index.html')

# Search Route
@app.route("/search", methods=["GET", "POST"])
def search_data():
    results = None
    if request.method == "POST":
        query = request.form['query'].lower()

        conn = get_db_connection()
        cursor = conn.cursor()

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
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM election_data")
    data = cursor.fetchall()
    conn.close()

    columns = ['Precinct', 'Race', 'LegislativeDistrict', 'CountyCouncil', 
               'CongressionalDistrict', 'CounterGroup', 'CounterType', 'SumOfCount']
    data_dict = [dict(zip(columns, row)) for row in data]

    return render_template("view_data.html", data=data_dict)

# Insert Data page
@app.route("/insert_data", methods=["GET", "POST"])
def insert_data():
    if request.method == "POST":
        precinct = request.form["precinct"]
        race = request.form["race"]
        legislative_district = request.form["legislative_district"]
        county_council = request.form["county_council"]
        congressional_district = request.form["congressional_district"]
        counter_group = request.form["counter_group"]
        counter_type = request.form["counter_type"]
        
        try:
            sum_of_count = int(request.form["sum_of_count"])
        except ValueError:
            return "Invalid Sum of Count value. Please enter a valid number.", 400

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''INSERT INTO election_data (
                Precinct, Race, LegislativeDistrict, CountyCouncil,
                CongressionalDistrict, CounterGroup, CounterType, SumOfCount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
            (precinct, race, legislative_district, county_council,
             congressional_district, counter_group, counter_type, sum_of_count))

            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            return f"Database error: {e}", 500
        finally:
            conn.close()

        return redirect(url_for('view_data'))

    return render_template('insert_data.html')

@app.route("/about")
def about_data():
    return render_template("about_data.html")

if __name__ == "__main__":
    app.run(debug=True)
