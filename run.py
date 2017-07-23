from routes import setup


# --------------------------------------------------------------------------- #
#                                                                             #
#                               Launch                                        #
#                                                                             #
# --------------------------------------------------------------------------- #
def run(app):
    app = setup(app)
    app.run(
        host=app.HOST,
        port=app.PORT,
        debug=app.DEBUG,
        threaded=app.THREADED
    )

if __name__ == '__main__':
    from app import app
    run(app)
