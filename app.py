# Build Flask API

from flask import Flask, jsonify
import pandas as pd
import threading
import seaborn as sns
import numpy as np

app = Flask(__name__)
df = sns.load_dataset('titanic') # loads dataset directly, no file needed

def clean(records):
    """Replace NaN/None with None so JSON serializes to null."""
    return [
        {k: (None if isinstance(v, float) and np.isnan(v) else v)
         for k, v in row.items()}
        for row in records
    ]

@app.route('/passengers')
def all_passengers():
    records = df[['survived','pclass','sex','age','fare']].head(20).to_dict(orient='records')
    return jsonify(clean(records))

# Background thread so Jupyter cell doesn't block
t = threading.Thread(target=lambda: app.run(port=5000))
t.daemon = True
t.start()
print("Flask API running on http://localhost:5000")