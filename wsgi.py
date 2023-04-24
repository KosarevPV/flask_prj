from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()
if __name__ == "__main__":
    app.run()


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("create-users")
def create_users():

    from blog.models import User

    admin = User(username="admin", password=generate_password_hash('admin'), is_staff=True)
    pavel = User(username="Pavel", password=generate_password_hash('admin'))
    curtis = User(username="Curtis", password=generate_password_hash('admin'))
    gary = User(username="Gary", password=generate_password_hash('admin'))
    john = User(username="John", password=generate_password_hash('admin'))

    db.session.add(admin)
    db.session.add(pavel)
    db.session.add(curtis)
    db.session.add(gary)
    db.session.add(john)
    db.session.commit()
