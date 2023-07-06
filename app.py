from flask import Flask, request
from flask_restful import Api, Resource
from application.api.extract_skills import extract_skills
from application.api.extract_titles import extract_titles

app = Flask("101-Skiller")
api = Api(app)

class Extractor(Resource):

    def post(self):
        data = request.get_json()
        resume_content = data.get("resume_content")
        official_skills, not_official_skills = extract_skills(resume_content)
        official_titles, not_official_titles = extract_titles(resume_content)

        response = {}
        if(official_skills):
            response["official_skills"] = list(official_skills)
        if(not_official_skills):
            response["not_official_skills"] = list(not_official_skills)
        if(official_titles):
            response["official_titles"] = list(official_titles)
        if(not_official_titles):
            response["not_official_titles"] = list(not_official_titles)

        return response

api.add_resource(Extractor, "/extractor")

if __name__ == '__main__':
    app.run()