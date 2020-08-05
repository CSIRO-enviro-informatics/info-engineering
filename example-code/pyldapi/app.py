import logging
import _config as conf
import pyldapi
from flask import Flask
from controller import pages, classes
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from jinja2 import Markup

app = Flask(__name__, template_folder=conf.TEMPLATES_DIR, static_folder=conf.STATIC_DIR)
CORS(app)

app.register_blueprint(pages.pages)
app.register_blueprint(classes.classes)

### swagger specific ###
SWAGGER_URL = '/api/doc'
API_URL = '/static/openapi.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Example LD API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

@app.context_processor
def utility_processor():
    def include_raw(url):
        import urllib.request
        import json
        res = urllib.request.urlopen(url)
        res_body = res.read()
        jo = json.loads(res_body.decode("utf-8"))
        j = json.dumps(jo, indent=4)
        #return u'{}'.format(url)
        #return j
        return Markup(j)
        
    return dict(include_raw=include_raw)
    
# run the Flask app
if __name__ == '__main__':
    logging.basicConfig(filename=conf.LOGFILE,
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(message)s')

    app.run(host="0.0.0.0", port=int("3000"), debug=conf.DEBUG)
