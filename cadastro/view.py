from cadastro import app, db
from flask import render_template, request
from cadastro.models import Contato


@app.route("/", methods = ['GET', 'POST'])
def homepage():
    context = {}
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        datanascimento = request.form['datanascimento']
        senha = request.form['senha']
    

        contato = Contato(
            nome = nome,
            email = email,
            datanascimento = datanascimento,
            senha = senha
        )
        
        db.session.add(contato)
        db.session.commit()


    return render_template("index.html", context = context)
