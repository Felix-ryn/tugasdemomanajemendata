from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Baca data
    df = pd.read_csv("data.csv")

    # Analisis sederhana
    avg_age = df["Age"].mean()
    avg_score = df["Score"].mean()
    max_score = df["Score"].max()
    min_score = df["Score"].min()

    # Kirim ke template
    return render_template("index.html",
                           avg_age=avg_age,
                           avg_score=avg_score,
                           max_score=max_score,
                           min_score=min_score,
                           data=df.to_html(classes="table table-striped"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
