import csv
from appfunctions import *


def register(username, password, old_frame, new_frame):
    db = open("database.csv", "a+", newline='')
    if len(username.strip()) <= 8:
        if username.strip() in open("database.csv").read():
            user_taken()
        else:
            with db:
                write = csv.writer(db)
                write.writerow([username.strip(), password.strip()])
                success_r()
                frame_change(old_frame, new_frame)
    else:
        user_long(username)


def login(username, password, old_frame, new_frame, user_var):
    validator = False
    with open("database.csv", "r+") as db:
        reader = csv.reader(db)
        for row in reader:
            if row == [username, password]:
                user_var = username
                frame_change(old_frame, new_frame)
                validator = True
    if validator == False:
        wrong_cred()





if __name__ == "__main__":
    print("=====")