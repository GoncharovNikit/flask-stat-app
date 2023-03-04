def init_routes(app):
    @app.route('/')
    def root():
        return '<h1>Hello Here!</h1>'