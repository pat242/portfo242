import csv
from flask import Flask , render_template , request ,redirect
app = Flask(__name__)
print(__name__)


@app.route('/')  # everytime / is used, def function and run it
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # everytime / is used, def function and run it
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt' ,'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data =  request.form.to_dict()
    	write_to_csv(data)
    	return  redirect ('/thankyou.html')
    else :
    	return 'something went wrong, try again later'


def write_to_csv(data):
    with open('database.csv' ,'a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


"""@app.route('/works.html')  # everytime / is used, def function and run it
def works_page():
    return render_template('works.html')


@app.route('/about.html')  # everytime / is used, def function and run it
def about_page():
    return render_template('about.html')


@app.route('/contact.html')  # everytime / is used, def function and run it
def contact_page():
    return render_template('contact.html')


@app.route('/components.html')  # everytime / is used, def function and run it
def components_page():
    return render_template('components.html')


@app.route('/work.html')  # everytime / is used, def function and run it
def work_page():
    return render_template('work.html')"""

'''@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return '%d' % post_id'''
