from flask import Flask

app = Flask(__name__)

from flask import request, redirect

from flask import render_template

@app.route('/mypage/me', methods=['GET'])
def me():
#    print("We received GET")
    return render_template("me.html")



@app.route("/mypage/contact")
def contact():
    return render_template("contact.html", success=False)

@app.route("/mypage/send-message", methods=["POST"])
def send_message():
    # Pobranie wiadomości z formularza
    message = request.form.get("message")
    if message:
        # Zwróć wiadomość do szablonu i ustaw 'success' na True
        return render_template("contact.html", success=True, message=message)
    else:
        return render_template("contact.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)