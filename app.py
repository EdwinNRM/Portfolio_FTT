from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email,senha,secret

app = Flask(__name__)
app.secret_key = secret

mail_settings = {
    "MAIL_SERVER": 'smtp.office365.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)

mail = Mail(app)

class Contato:
    def __init__(self,nome,email,mensagem):
        self.nome = nome,
        self.email = email,
        self.mensagem = mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods =['GET','POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
            )
        
        msg = Message(
            subject = f'{formContato.nome} enviou uma mensagem',
            sender = app.config.get("MAIL_USERNAME"),
            recipients=["unievangelica.ftt@gmail.com"],
            body = f'''

            {formContato.nome} com o email {formContato.email}, te enviou uma mensagem:
            
            {formContato.mensagem}

            '''
        )

        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')


if __name__ == 'main':
    app.run(debug=True)