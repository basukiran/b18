from flask import Flask, render_template, request
import random

app = Flask(__name__)
guessing_number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    global guessing_number

    if request.method == "POST":
        try:
            user_input = int(request.form["guess"])
            if user_input > guessing_number:
                message = "Number is too big"
            elif user_input < guessing_number:
                message = "Number is too small"
            else:
                message = f"🎉 You guessed it! The number was {guessing_number}"
                guessing_number = random.randint(1, 100)  # reset game
        except ValueError:
            message = "Please enter a valid number!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
