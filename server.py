from flask import Flask, render_template, request, redirect  #, send_from_directory 13123123
import csv
# import os
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong, try again'


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# Three lines of code up above mean the same that everything underneath.
# The difference is that if we add another html file to /Templates the code above adds it dynamically,
# while in the code above we have to add every html by ourselves

# @app.route('/index.html')
# def index():
#     return render_template('index.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/contact.html')
# def contacts():
#     return render_template('contact.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
