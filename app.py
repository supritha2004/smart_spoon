
from flask import Flask, request, render_template
from taste_model import predict_taste
from feedback_analysis import analyze_sentiment
from food_recognition import recognize_food_name
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        file = request.files['food_image']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        food, salt = recognize_food_name(file.filename)
        rating = int(request.form['rating'])
        taste = predict_taste(salt, rating)
        feedback = request.form['feedback']
        sentiment = analyze_sentiment(feedback)

        result = {
            'food': food, 'salt': salt, 'taste': taste,
            'feedback': feedback, 'sentiment': sentiment
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
