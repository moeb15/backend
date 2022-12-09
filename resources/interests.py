from flask_restful import Resource
from flask import request
from http import HTTPStatus


class InterestsResource(Resource):
    def get(self):
        #should probably make a db table for this and just add text like this to it
        data="My primary interests are programming, mathematics, and fitness.\nIt's important to me to find the time to exercise, and even more time learning."

        return {'interests':data}, HTTPStatus.OK