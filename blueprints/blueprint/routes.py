"""General page routes."""
from flask import Blueprint
from flask import render_template


# Blueprint Configuration
basic_bp = Blueprint(
    "basic_bp", __name__, template_folder="templates", static_folder="static", url_prefix="/basic"
)


@basic_bp.route("/", methods=["GET"])
def home():
    """Homepage."""
    return render_template(
        "index.html",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
    )