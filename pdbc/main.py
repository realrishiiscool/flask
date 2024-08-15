from flask import Flask,render_template,url_for,redirect,request
from t import insert_student

app = Flask('__name__')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/stdt_reg', methods=['POST'])
def stdt_reg():
    try:
        # Get data from the form
        first_name = str(request.form['first_name'])
        last_name = str(request.form['last_name'])
        email = str(request.form['email'])
        enrollment_date = str(request.form['enrollment_date'])
        grade_level = int(request.form['grade_level'])

        # Call the function to insert data
        insert_student(first_name, last_name, email, enrollment_date, grade_level)

        # Redirect back to the form after successful submission
        return redirect(url_for('student_form'))

    except Exception as e:
        print(f"Error: {e}")
        # Handle the error by redirecting back to the form with an error message
        return redirect(url_for('index'))




if __name__ == '__main__':
	app.run()
