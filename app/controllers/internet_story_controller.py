from app.controllers.controller import ControllerBase
from flask import render_template

class InternetStoryController(ControllerBase):
    @staticmethod
    def get():
        return render_template('internet_story.html')