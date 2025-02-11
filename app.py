from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('imdb_anime.csv')

print(df.dtypes)

df['User Rating'] = pd.to_numeric(df['User Rating'], errors='coerce')

def recommend_anime(genre, certificate, min_rating, max_rating):
    # Filter the DataFrame based on user input
    filtered_df = df[
        (df['Genre'].str.contains(genre, case=False)) &
        (df['Certificate'] == certificate) &
        (df['User Rating'] >= float(min_rating)) &
        (df['User Rating'] <= float(max_rating))
    ]
    
    recommendations = filtered_df[['Title', 'Year']].head(10)
    
    return recommendations.to_html(index=False, classes='table table-striped')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    genre = request.form['genre']
    certificate = request.form['certificate']
    min_rating = request.form['min_rating']
    max_rating = request.form['max_rating']

    recommended_anime = recommend_anime(genre, certificate, min_rating, max_rating)

    return render_template('recommendations.html', tables=recommended_anime)

if __name__ == '__main__':
    app.run(debug=True)
