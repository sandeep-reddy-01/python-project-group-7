 
# 🗳️ Election Data Web App

A full-stack Flask web application for viewing, inserting, searching, and managing election data. It supports importing data from external sources (like GitHub CSVs), preprocessing it, and saving it to a SQLite database.

---

## 📦 Features

- Load and preprocess election data from a GitHub-hosted CSV
- Run EDA to understand the dataset
- Store cleaned data in SQLite
- View all data in a web interface
- Search across multiple fields using a keyword
- Insert new election data entries manually via form
- User-friendly interface using Flask and Jinja templates

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- SQLite
- Pandas
- HTML/CSS (Jinja2 templates)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/election-data-app.git
cd election-data-app
```

### 2. Set up a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Load and preprocess the data

```python
from data_collection.collect_data import load_data
from data_collection.eda import run_eda
from data_collection.preprocess import preprocess_data
from data_collection.save_to_db import save_to_db

df = load_data()
run_eda(df)  # Optional step to explore the data
clean_df = preprocess_data(df)
save_to_db(clean_df)
```

### 5. Run the Flask App

```bash
python app.py
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 6. Run Full Pipeline

To run the full data processing pipeline (load data, EDA, preprocessing, and save to the database), use the `main.py` script.

```python
python main.py
```

This will perform the following steps:

1. Load data from the source
2. Run exploratory data analysis (EDA)
3. Preprocess the data (cleaning and transformation)
4. Save the cleaned data into the SQLite database

Ensure that the `database/elections.db` exists before running the script. It will be populated with the preprocessed data.

---

## 📁 Project Structure

```
election-data-app/
├── main.py  # New file to run the entire pipeline
├── app.py
├── data_collection/
│   ├── collect_data.py
├── data_processing/
│   ├── eda_analysis.py
│   └── process.py
├── database/
│   └── elections.db
├── templates/
│   ├── index.html
│   ├── search.html
│   ├── view_data.html
│   ├── insert_data.html
│   └── about_data.html
├── static/
│   └── styles.css
├── uploads/
│   └── sample.csv
├── requirements.txt
└── README.md
```

---

## 🌐 Dataset Source

CSV loaded from:

```
https://raw.githubusercontent.com/sandeep-reddy-01/datasets/main/feb_2025_elections_dataset.csv
```

Expected columns include:

- `Precinct`
- `Race`
- `LegislativeDistrict`
- `CountyCouncil`
- `CongressionalDistrict`
- `CounterGroup`
- `CounterType`
- `SumOfCount`

---

## ✅ To Do

- Add user authentication
- Add pagination for large datasets
- Export data to CSV or Excel
- Add charts and visualizations

---

## 📃 License

This project is licensed under the MIT License.
