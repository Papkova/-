from . import app
from .models import Article, db
from .models.user import User
from flask import redirect, render_template, request


@app.route("/")
def base():
    return render_template("base.html", title="Python course")


@app.route("/create-article", methods=["POST", "GET"])
def create_article():
    if request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        text = request.form["text"]

        article = Article(
            title=title,
            intro=intro,
            text=text
        )
        try:
            db.session.add(article)
            db.session.commit()
            return redirect("/articles")
        except Exception as exc:
            return f"ПРи збереженні запису у базу даних виникла помилка: {exc}"
    else:
        return render_template("create_article.html")


@app.route("/articles")
def list_articles():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("articles.html", articles=articles)


@app.route("/articles/<int:id>/")
def article_detail(id):
    article = Article.query.get(id)
    return render_template("article_detail.html", article=article)


@app.route("/articles/<int:id>/delete")
def article_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect("/articles")
    except Exception as exc:
        return f"При видаленні виникла помилка: {exc}"


@app.route("/articles/<int:id>/update", methods=["POST", "GET"])
def article_update(id):
    article = Article.query.get(id)

    if request.method == "POST":
        article.title = request.form["title"]
        article.intro = request.form["intro"]
        article.text = request.form["text"]

        try:
            db.session.commit()
            return redirect("/articles")
        except Exception as exc:
            return f"При оновленні запису виникла помилка: {exc}"
    else:
        return render_template("article_update.html", article=article)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]

        user = session.query(User).where(User.username == username).first()

        if user:
            flash("Цей користувач вже існує!")
            return redirect("login")

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )
        try:
            session.add(new_user)
            session.commit()
        except Exception as exc:
            return f"При збереженні користувача виникла помилка: {exc}"
        finally:
            session.close()
            return redirect("/login")
    else:
        return render_template("signup.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
