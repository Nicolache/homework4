from config import db, db_file
import models
import os
import sys

catalogue_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if catalogue_path not in sys.path:
    sys.path.append(catalogue_path)


if __name__ == '__main__':
    if os.path.exists(db_file):
        os.remove(db_file)
    db.create_all()
