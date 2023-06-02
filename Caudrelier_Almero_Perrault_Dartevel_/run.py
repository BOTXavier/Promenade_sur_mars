from myApp.config import DEBUG, WEB_SERVER
from myApp.views import app
#import myApp.model.bdd

if __name__ == '__main__':
    app.run(
        host = WEB_SERVER['host'],
        port= WEB_SERVER['port'],
        debug=DEBUG
    )