from app.controllers.controller import ControllerBase
from flask import render_template

class OOPSController(ControllerBase):
    @staticmethod
    def get():
        return render_template('oops.html')
