#!/usr/bin/env python3

from app import app
from models import db, Activity, Signup, Camper

if __name__ == '__main__':
    with app.app_context():
        signup1 = db.session.query(Signup).first()
        print(signup1.camper.__repr__())
        print(signup1.activity.__repr__())
        # import ipdb; ipdb.set_trace()