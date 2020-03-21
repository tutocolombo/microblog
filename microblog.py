from app import app, cli


@app.shell_context_processor
def make_shell_context():
    from app import db
    from app.models import User, Post
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":
    app.run()
