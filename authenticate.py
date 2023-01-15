import csv
from appfunctions import *


def register(username, password):
    db = open("database.csv", "a+", newline='')
    if username.strip() in open("database.csv").read():
        user_taken()
    else:
        with db:
            write = csv.writer(db)
            write.writerow([username.strip(), password.strip()])


def login(username, password, old_frame, new_frame):
    validator = False
    with open("database.csv", "r+") as db:
        reader = csv.reader(db)
        for row in reader:
            if row == [username, password]:
                old_frame.grid_forget()
                new_frame.grid(row=1, column=0, columnspan=3)
                validator = True
    if validator == False:
        wrong_cred()


if __name__ == "__main__":
    print("=====")