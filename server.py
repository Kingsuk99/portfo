# Run the 2 commands
#  py -3 -m venv .web server
#  py -3 -m venv venv
# and then run the command
# Run the code with flask --app server.py run --debug

from flask import Flask,render_template,url_for,request,redirect
import csv
# Run the code with flask --app server.py run --debug
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/index.html')
# def my_homes():
#     return render_template('index.html')
# @app.route('/works.html')
# def works():
#     # return 'Hello World.Today is a great day.Test data'
#    return render_template('works.html')
#
# @app.route('/about.html')
# def about_me():
#     # return 'Hello World.Today is a great day.Test data'
#    return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     # return 'Hello World.Today is a great day.Test data'
#    return render_template('contact.html')
#
# @app.route('/work.html')
# def work():
#     # return 'Hello World.Today is a great day.Test data'
#    return render_template('work.html')
#
# @app.route('/components.html')
# def components():
#     # return 'Hello World.Today is a great day.Test data'
#    return render_template('components.html')

# Making the routes dynamic
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
def write_to_file(data):
     with open('database.txt', mode ='a') as database:
         email =data["email"]
         subject= data["subject"]
         message = data["message"]
         file =database.write(f'\n{email},{subject},{message}')

# def write_to_csv(data):
#     with open('database.csv', mode='a',newline ='') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database2,delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email,subject,message])

def write_to_csv(data):
  with open('database.csv', mode='a', newline='') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    # return 'form submitted hooray'
 if request.method == 'POST':
     try:
         data = request.form.to_dict()
         print(data)
         # write_to_file(data)
         write_to_csv(data)
         # return 'form submitted'
         return redirect('/thankyou.html')
     except:
         return 'did not save to database'

 else :
     return 'Something went wrong.Try again'

