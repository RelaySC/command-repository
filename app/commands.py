from . import app, db

@app.cli.command()
def create_database():
    db.create_all()