from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("rf_salary_prediction.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Experience
        experience = int(request.form["experience"])
        # print(experience)
        
        # Miles from Metropolis
        miles = int(request.form["milesfromMetropolis"])
        # print(miles)

        # Job Type
        # CEO = 0 (not in column)
        jobType=request.form['jobType']
        if(jobType=='CTO'):
            cto = 1
            cfo = 0
            vice_president = 0
            manager = 0
            senior = 0
            junior = 0
            janitor = 0

        elif (jobType=='CFO'):
            cto = 0
            cfo = 1
            vice_president = 0
            manager = 0
            senior = 0
            junior = 0
            janitor = 0

        elif (jobType=='VICE_PRESIDENT'):
            cto = 0
            cfo = 0
            vice_president = 1
            manager = 0
            senior = 0
            junior = 0
            janitor = 0
            
        elif (jobType=='MANAGER'):
            cto = 0
            cfo = 0
            vice_president = 0
            manager = 1
            senior = 0
            junior = 0
            janitor = 0
            
        elif (jobType=='SENIOR'):
            cto = 0
            cfo = 0
            vice_president = 0
            manager = 0
            senior = 1
            junior = 0
            janitor = 0
            
        elif (jobType=='JUNIOR'):
            cto = 0
            cfo = 0
            vice_president = 0
            manager = 0
            senior = 0
            junior = 1
            janitor = 0
            
        elif (jobType=='JANITOR'):
            cto = o
            cfo = 0
            vice_president = 0
            manager = 0
            senior = 0
            junior = 0
            janitor = 1

        else:
            cto = 0
            cfo = 0
            vice_president = 0
            manager = 0
            senior = 0
            junior = 0
            janitor = 0
            
        # print(cto, cfo, vise_prsident, manager, senior, junior, janitor)

        # Degree
            # BACHELORS = 0 (not in column)
        degree=request.form['degree']
        if(degree=='DOCTORAL'):
            doctoral = 1
            masters = 0
            high_school = 0
            no_degree = 0

        elif (degree=='MASTERS'):
            doctoral = 0
            masters = 1
            high_school = 0
            no_degree = 0

        elif (degree=='HIGH_SCHOOL'):
            doctoral = 0
            masters = 0
            high_school = 1
            no_degree = 0
            
        elif (degree=='NONE'):
            doctoral = 0
            masters = 0
            high_school = 0
            no_degree = 1
            
        else:
            doctoral = 0
            masters = 0
            high_school = 0
            no_degree = 0
            
        # print(doctoral, masters, high_school, none)

        # Major
        # BIOLOGY = 0 (not in column)
        major=request.form['major']
        if (major == 'MATH'):
            maths = 1
            chemistry = 0
            engineering = 0
            literature = 0
            business = 0
            physics = 0
            computer_sci = 0
            no_major = 0
        
        elif (major == 'CHEMISTRY'):
            maths = 0
            chemistry = 1
            engineering = 0
            literature = 0
            business = 0
            physics = 0
            computer_sci = 0
            no_major = 0

        elif (major == 'ENGINEERING'):
            maths = 0
            chemistry = 0
            engineering = 1
            literature = 0
            business = 0
            physics = 0
            computer_sci = 0
            no_major = 0

        elif (major == 'LITERATURE'):
            maths = 0
            chemistry = 0
            engineering = 0
            literature = 1
            business = 0
            physics = 0
            computer_sci = 0
            no_major = 0

        elif (major == 'BUSINESS'):
            maths = 0
            chemistry = 0
            engineering = 0
            literature = 0
            business = 1
            physics = 0
            computer_sci = 0
            no_major = 0
            
        elif (major == 'PHYSICS'):
            maths = 0
            chemistry = 0
            engineering = 0
            literature = 0
            business = 0
            physics = 1
            computer_sci = 0
            no_major = 0
            
        elif (major == 'COMP_SCI'):
            maths = 0
            chemistry = 0
            engineering = 0
            literature = 0
            business = 0
            physics = 0
            computer_sci = 1
            no_major = 0
            
        elif (major == 'NONE'):
            maths = 0
            chemistry = 0
            engineering = 0
            literature = 0
            business = 0
            physics = 0
            computer_sci = 0
            no_major = 1
            
        else:
            maths = 0
            chemistry = 0
            engineering = 0
            literature = 0
            business = 0
            physics = 0
            computer_sci = 0
            no_major = 0

        # print(maths, chemistry, engineering, literature, business, physics, computer_sci, none)
        
        # Industry
        # AUTO = 0 (not in column)
        industry = request.form['industry']
        if (industry == 'OIL'):
            oil = 1
            service = 0
            finance = 0
            health = 0
            web = 0
            education = 0
        
        elif (industry == 'SERVICE'):
            oil = 0
            service = 1
            finance = 0
            health = 0
            web = 0
            education = 0

        elif (industry == 'FINANCE'):
            oil = 0
            service = 0
            finance = 1
            health = 0
            web = 0
            education = 0

        elif (industry == 'HEALTH'):
            oil = 0
            service = 0
            finance = 0
            health = 1
            web = 0
            education = 0

        elif (industry == 'WEB'):
            oil = 0
            service = 0
            finance = 0
            health = 0
            web = 1
            education = 0
            
        elif (industry == 'EDUCATION'):
            oil = 0
            service = 0
            finance = 0
            health = 0
            web = 0
            education = 1
            
        else:
            oil = 0
            service = 0
            finance = 0
            health = 0
            web = 0
            education = 0
            
        # print(oil, services, finance, health, web, education)
        
        
        prediction = model.predict([[experience, miles, cfo, cto, janitor, junior, manager,
       senior, vice_president, doctoral, high_school, masters, no_degree, business,
       chemistry, computer_sci, engineering, literature, maths, no_major, physics,
       education, finance, health, oil, service, web]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="You can expect a salary of ${}k".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
