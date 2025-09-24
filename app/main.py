from flask import Blueprint, render_template as render, flash, redirect, url_for
from .models import Post
from . import db
from .forms import PostForm
from flask_login import current_user, login_required

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render("index.html", posts=posts)


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


@bp.route("/read-post/<int:id>/")
def read_post(id):
    post = Post.query.get_or_404(id)
    return render("read-post.html", post=post)
