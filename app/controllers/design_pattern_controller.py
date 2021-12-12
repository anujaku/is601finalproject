from app.controllers.controller import ControllerBase
from flask import render_template

class DesignPatternController(ControllerBase):
    @staticmethod
    def get():
        return render_template('design_pattern.html')