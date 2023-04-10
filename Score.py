import os
import Utils


def add_score(difficulty):
    file_name = Utils.SCORES_FILE_NAME
    points_of_winning = int(difficulty) * 3 + 5

    if os.path.exists(file_name):
        score_file = open(file_name, "r")
        current_score = score_file.read()
        score_file.close()
        score_file = open(file_name, "w")
        score_file.write(str(int(current_score) + points_of_winning))
        score_file.close()
    else:
        score_file = open(file_name, "w")
        score_file.write(str(points_of_winning))
        score_file.close()