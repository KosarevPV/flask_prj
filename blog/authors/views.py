from flask import Blueprint, render_template
from blog.models import Author

authors = Blueprint("authors", __name__, url_prefix='/authors')


@authors.route("/", endpoint="list")
def authors_list():
    authors = Author.query.all()
    return render_template("authors/list.html", authors=authors)
