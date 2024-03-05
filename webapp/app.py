from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']

    
    if not test_string.strip() or not regex_pattern.strip():
        return render_template('index.html')

    
    matches = re.finditer(regex_pattern, test_string)

    
    matched_strings = []
    for match in matches:
        matched_strings.append(match.group())

    return render_template('index.html', matched_strings=matched_strings)

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form.get('email')
    if not email.strip():
        return render_template('index.html')

    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(email_pattern, email):
        email_validation_message = 'Valid email address'
    else:
        email_validation_message = 'Invalid email address'

    return render_template('index.html', email_validation_message=email_validation_message)

if __name__ == '__main__':
    app.run(debug=True, host ="0.0.0.0")
