import bottle
from bottle import template

main_app = bottle.app()

from app import app as app_routes
from api import api_routes

@main_app.error(404)
def handle_404(error):
    return template("not_found")

@main_app.error(500)
def handle_500(error):
    #return "500.error"
    return template("500_error")

main_app.merge(app_routes)
main_app.merge(api_routes)


#if __name__ == "__main__":
#run(reloader=True, debug=True)
#app.run(reloader=True, debug=True)
main_app.run()