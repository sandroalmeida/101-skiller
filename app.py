from flask import Flask, request
from flask_restful import Api, Resource
from application.api.extract_skills import extract_skills

app = Flask("101-Skiller")
api = Api(app)

class Extractor(Resource):

    def post(self):
        data = request.get_json()
        resume_content = data.get("resume_content")
        official_skills, not_official_skills = extract_skills(resume_content)
        return {"official_skills": list(official_skills), "not_official_skills": list(not_official_skills)}

api.add_resource(Extractor, "/extractor")

if __name__ == '__main__':
    app.run()