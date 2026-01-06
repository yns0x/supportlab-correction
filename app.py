from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Pour l'instant : "fausse BDD" en mémoire
tickets = []
next_id = 1


@app.route("/")
def index():
    return redirect(url_for("tickets_list"))


@app.route("/tickets")
def tickets_list():
    return render_template("tickets_list.html", tickets=tickets)


@app.route("/tickets/new", methods=["GET", "POST"])
def ticket_new():
    global next_id

    if request.method == "POST":
        titre = request.form.get("titre")
        description = request.form.get("description")
        priorite = request.form.get("priorite")

        ticket = {
            "id": next_id,
            "titre": titre,
            "description": description,
            "priorite": priorite,
            "statut": "Ouvert",
        }
        tickets.append(ticket)
        next_id += 1

        return redirect(url_for("tickets_list"))

    return render_template("ticket_new.html")


if __name__ == "__main__":
    app.run(debug=True)
