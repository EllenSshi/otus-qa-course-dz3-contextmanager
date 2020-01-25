import csv
import json
import pandas as pd


def add_users_and_books_into_result_file():
    results = list()
    with open('users.json', 'r') as users_file:
        users = json.load(users_file)
        books = pd.read_csv('books.csv')
        for user in users:
            user_books = books[['Title', 'Author', 'Height']].sample(2).to_dict(orient='records')
            new_user = {"name": user['name'], "gender": user['gender'], "address": user['address'], "books": user_books}
            results.append(new_user)
    with open('result.json', 'w') as result_file:
        json.dump(results, result_file, indent=4)


if __name__ == '__main__':
    add_users_and_books_into_result_file()

