from flask import Flask, request
from flask_restful import Api, Resource
from extract_skills import extract_skills

app = Flask("101-Skiller")
api = Api(app)


class Skill(Resource):

    def post(self):
        data = request.get_json()
        resume_content = data.get("resume_content")
        official_skills, not_official_skills = extract_skills(resume_content)
        return {"official_skills": list(official_skills), "not_official_skills": list(not_official_skills)}

api.add_resource(Skill, "/skill")

if __name__ == '__main__':
    app.run()