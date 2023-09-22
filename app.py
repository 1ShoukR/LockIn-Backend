from flask import Flask
import re
import typing as t
import routes
from flask import current_app, Flask, g, request



app = Flask(__name__)

app.register_blueprint(routes.user.bp, url_prefix='/user')
app.register_blueprint(routes.auth.bp, url_prefix='/auth')




if __name__ == '__main__':
    app.run(debug=True)
