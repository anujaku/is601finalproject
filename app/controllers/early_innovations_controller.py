from app.controllers.controller import ControllerBase
from flask import render_template

class EarlyInnovationsController(ControllerBase):
    @staticmethod
    def get():
        return render_template('early_innovations.html')
