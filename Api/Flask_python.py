from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        usia = request.form.get("usia")

        # (opsional) debug
        print(name, email, password, usia)

        return redirect(url_for("tab2"))

    return render_template("index.html")


@app.route("/tab2", methods=["GET", "POST"])
def tab2():
    if request.method == "POST":
        user_id = request.form.get("id")
        print(user_id)

    return render_template("tab2_index.html")


# 🔥 WAJIB buat Vercel
def handler(request):
    return app(request.environ, lambda *args: None)
