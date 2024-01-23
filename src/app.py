import os

# App Initialization
from . import create_app  # from __init__ file

application = create_app()


# Hello World!


application.run()

# flask db init
# flask db migrate
# flask db upgrade
# python -m pip uninstall flask-sqlalchemy
# python -m pip install flask-sqlalchemy
# http://localhost:5000/accounts
# http://localhost:5000/accounts/ACCOUNT_ID
