from flask import Flask, render_template, request

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    birthday_month = request.form['birthday_month']

    zodiac_sign = predict_zodiac_sign(birthday_month)

    return render_template('result.html', name=name, zodiac_sign=zodiac_sign, birthday_month=birthday_month)

def predict_zodiac_sign(month):
    zodiac_signs = {
        'January': 'Capricorn',
        'February': 'Aquarius',
        'March': 'Pisces',
        'April': 'Aries',
        'May': 'Taurus',
        'June': 'Gemini',
        'July': 'Cancer',
        'August': 'Leo',
        'September': 'Virgo',
        'October': 'Libra',
        'November': 'Scorpio',
        'December': 'Sagittarius'
    }

    return zodiac_signs.get(month, 'Unknown')

if __name__ == '__main__':
    app.run(debug=True)
