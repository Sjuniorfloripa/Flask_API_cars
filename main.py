from app import create_app
from app.routes import init_routes
from app.auth_routes import init_auth_routes


app = create_app()
init_routes(app)
init_auth_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
