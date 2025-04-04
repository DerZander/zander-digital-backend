from flask_restx import Resource, Namespace

from database.models.education import Education

namespace = Namespace('education', description='Education related operations')


@namespace.route('/')
class EducationEndpoint(Resource):
    def get(self):
        educations = Education.query.all()
        return [education.as_dict() for education in educations]
