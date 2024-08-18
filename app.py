from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

Doctors=[
  {
    'id':'1',
    'name':'Dr. Amit',
    'speciality':'Cardiology',
    'location':'Delhi',
    'rating':'4.5',
  },
  {
    'id':'2',
    'name':'Dr. Karan',
    'speciality':'Dentist',
    'location':'Delhi',
    'rating':'4.5',
  },
  {
    'id':'3',
    'name':'Dr. Shalini',
    'speciality':'Gynecology',
    'location':'Delhi',
    'rating':'4.5',
  },
  {
    'id':'4',
    'name':'Dr. Saakshi',
    'speciality':'Opthalmology',
    'location':'Delhi',
    'rating':'4.5',
  }
]


@app.route("/")
def hello():
  return render_template("home.html", doc=Doctors)

@app.route("/finddoc")
def finddoc():
  return render_template("finddoc.html", doc=Doctors)

@app.route("/api/doc")
def doc_list():
  return jsonify(Doctors)

if (__name__ == "__main__"):
  app.run(host="0.0.0.0", debug=True)
