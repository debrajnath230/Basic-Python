# Importing
from flask import Flask, render_template, request

# Interaction
web = Flask(__name__)

# Mapping
@web.route('/')
@web.route('/register')
# Inputs
def homepage():
    return render_template('register.html')

# Mapping
@web.route('/confirmation', methods=['POST', 'GET'])
# Inputs
def register():
    if request.method == "POST":
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone_number')
        return render_template('confirmation.html', name=n, city=c, phone_number=p)

# Main
if __name__ == "__main__":
    web.run(debug=True, port=8080)
