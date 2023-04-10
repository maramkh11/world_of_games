from flask import Flask, render_template
import os
import Utils

app = Flask(__name__,template_folder='templates')

@app.route("/")
def score_server():
    file_name = Utils.SCORES_FILE_NAME

    if os.path.exists(file_name):
        score_file = open(Utils.SCORES_FILE_NAME, "r")
        current_score = score_file.read()
        score_file.close()
        return render_template("scoreGames.html", score=current_score)
    else:
        error_number = Utils.BAD_RETURN_CODE
        return render_template("error.html", error=error_number)


if __name__ == "__main__":
    app.run()