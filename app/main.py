from flask import Blueprint, render_template as render, flash, redirect, url_for
from .models import Post
from . import db
from .forms import PostForm
from flask_login import current_user, login_required

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render("index.html")


@bp.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(
            title=form.title.data, content=form.content.data, author=current_user
        )
        db.session.add(new_post)
        db.session.commit()
        flash("Post muvaffaqiyatli yaratildi.", "success")
        return redirect(url_for("main.create_post"))
    return render("create-post.html", form=form)
