from flask_restful import Resource
from http import HTTPStatus


class CV(Resource):
    def get(self):

        skills_data = {
            'programming':'Knowledge of JavaScript, React, Python, Flask, from both professional and personal development settings',
            'ides':'Experience with VSCode, Visual Studio, Eclipse IDE',
            'testing':'Familiarity with tools such as Postman for API Testing, issue tracking tools like JIRA, and version control tools like Perforce and Git'
        }

        job_data = {
            'Opentext':{
                'company':'Opentext',
                'job_title':'Software Engineer-Intern',
                'job_responsibilities':"""The team I had been apart of worked on Opentext's flagship project, Content Server.
                My responsibilities were to write unit tests for the web application, test endpoints using Postman, and work on bugfixes and feature
                 implementations for the web application. The web app had been written using proprietary tools, so the language used was developed by
                  Opentext, aside from this JavaScript had been used on the job."""
            },
            'WISL':{
                'company':'WISL',
                'job_title':'QA-Intern',
                'job_responsibilities':"""At WISL(Waterloo Information Systems Ltd.) we had been working on a web application meant to
                 teach frontend and backend development to highschoolers. My job had been to manually test the web app, document bugs, 
                 and implement changes on the frontend using HTML, CSS, and JavaScript."""
            }
        }

        education_data = {
            'data':"""Pursuing a BMath at the Univeristy of Waterloo, majoring in Applied Mathematics, graduating in December 2022.
            Throughout my education at the University of Waterloo I have taken a variety of courses touching on topics like cryptography,
             computer science, and computational mathematics."""
        }

        data = [skills_data, job_data, education_data]
        
        return data, HTTPStatus.OK