#!/usr/bin/env python3

from app import app
from models import db, Activity, Signup, Camper

if __name__ == '__main__':
    with app.app_context():
        pass
        # c1 = Camper(name="Tri", age=5)
        # Signup(time=22)
        # import ipdb; ipdb.set_trace()

