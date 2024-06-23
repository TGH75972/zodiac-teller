from flask import Flask, render_template, request

app = Flask(__name__)

zodiac_info = {
    'Aries': 'Aries are known for being passionate, motivated, and confident leaders. They are driven, determined, and don’t shy away from competition.',
    'Taurus': 'Taurus individuals are known for being reliable, practical, and ambitious. They appreciate the finer things in life and have a strong connection to the earth.',
    'Gemini': 'Geminis are adaptable, outgoing, and intelligent. They are quick-witted and love to engage in intellectual conversations.',
    'Cancer': 'Cancer signs are known for being highly intuitive, emotional, and compassionate. They are deeply connected to their family and home.',
    'Leo': 'Leos are known for their enthusiasm, creativity, and leadership. They are generous and warm-hearted, often taking center stage.',
    'Virgo': 'Virgos are known for their practicality, attention to detail, and analytical nature. They are methodical and value cleanliness and order.',
    'Libra': 'Libras are known for their sense of balance, justice, and fairness. They value harmony in relationships and are often charming and diplomatic.',
    'Scorpio': 'Scorpios are known for their intensity, passion, and resourcefulness. They are determined and often have a magnetic personality.',
    'Sagittarius': 'Sagittarius individuals are known for their adventurous spirit, optimism, and love for freedom. They are enthusiastic and love to explore new ideas and places.',
    'Capricorn': 'Capricorns are known for their discipline, ambition, and practicality. They are hardworking and often achieve great success through their determination.',
    'Aquarius': 'Aquarius signs are known for their originality, independence, and humanitarian nature. They are often seen as visionaries and are deeply intellectual.',
    'Pisces': 'Pisces are known for their empathy, artistic nature, and intuition. They are compassionate and often have a deep understanding of the world around them.'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    birthday_month = request.form['birthday_month']
    zodiac_sign = predict_zodiac(birthday_month)
    return render_template('result.html', name=name, birthday_month=birthday_month, zodiac_sign=zodiac_sign)

@app.route('/info/<sign>')
def info(sign):
    info = zodiac_info.get(sign, "Information not available.")
    return render_template('info.html', sign=sign, info=info)

def predict_zodiac(month):
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
        'December': 'Sagittarius',
    }
    return zodiac_signs.get(month, 'Unknown')

if __name__ == '__main__':
    app.run(debug=True)
