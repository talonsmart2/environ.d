def router(app):
    from .views import views, Index, Auth
    views.add_url_rule("/", view_func=Index.as_view("index"))
    views.add_url_rule("/auth", view_func=Auth.as_view("auth"))
    app.register_blueprint(views)