from app.controllers.controller import ControllerBase
from flask import render_template


class FounderController(ControllerBase):
    @staticmethod
    def get():
        return render_template('page2.html')