from flask import Blueprint, render_template, redirect, request, session
from flask.views import MethodView

views = Blueprint("views", __name__)

class Index(MethodView):
    def get(self):
        return render_template("index.html")

class Auth(MethodView):
    def post(self):
        pass
    def get(self):
        return render_template("auth.html")

"""
class BoilerPlate(MethodView):
    def post(self):
        pass

    def get(self):
        pass
"""