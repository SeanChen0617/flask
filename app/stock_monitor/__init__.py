def create_module(app, **kwargs):
    print('=====>> stock_monitor: creating module <<=====')
    from .routes import sm_blueprint
    app.register_blueprint(sm_blueprint, url_prefix='/stock_monitor')