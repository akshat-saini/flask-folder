from flask import Flask
from configuration.configs import Config

app = Flask(__name__)

from routes import route
app.config.from_object(Config)


# if __name__ == "__main__":
#     app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
