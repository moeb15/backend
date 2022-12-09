from flask_restful import Resource
from http import HTTPStatus

class Homepage(Resource):
    def get(self):
        data = {'title':'Welcome!',
                'message':"I'm Mujtaba, an aspiring Software Developer",
                'subtext':'Through the links above, you can find pages displaying my projects, cv, and interests.',
                'contact_me':'If you want to reach out, fill out my contact form below, thanks!'}
        return data, HTTPStatus.OK