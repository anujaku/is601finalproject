from app.controllers.controller import ControllerBase
from flask import render_template

class AAAController(ControllerBase):
    @staticmethod
    def get():
        return render_template('aaa_testing.html')
