import json
from flask import Flask, request, abort, render_template, send_from_directory
from flask_cors import CORS
from config import db

app = Flask(__name__)
CORS(app) # disable CORS check

@app.get("/")
def home():
    return render_template("index.html");

@app.get("/static/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)

@app.get("/manifest.json")
def serve_manifest():
    return send_from_directory("static","manifest.json")


def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj


@app.get('/api/pets')
def get_pets():
    cursor = db.pets.find({})
    all_pets = []
    for pet in cursor:
        all_pets.append(fix_id(pet))

    return json.dumps(all_pets)


@app.post("/api/pets")
def save_pets():
    pet = request.get_json()
    # save to db
    db.pets.insert_one(pet)

    fix_id(pet) #fix the id before returning any object from DB
    return json.dumps(pet)

@app.get('/api/comments')
def get_comments():
    cursor = db.comments.find({})
    all_comments = []
    for comments in cursor:
        all_comments.append(fix_id(comments))

    return json.dumps(all_comments)


@app.post("/api/comments")
def save_comments():
    comment = request.get_json()
    # save to db
    db.comments.insert_one(comment)

    fix_id(comment) #fix the id before returning any object from DB
    return json.dumps(comment)




@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html");


# to run the project
# activate venv: source venv/bin/activate
# flask --app server --debug run