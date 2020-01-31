import json
import pandas as pd


def add_users_and_books_into_result_file(rfile):
    results = list()
    with open('users.json', 'r') as users_file:
        users = json.load(users_file)
        books = pd.read_csv('books.csv')
        for user in users:
            user_books = books[['Title', 'Author', 'Height']].sample(2).to_dict(orient='records')
            new_user = {"name": user['name'], "gender": user['gender'], "address": user['address'], "books": user_books}
            results.append(new_user)
    with open(rfile, 'w') as r_file:
        json.dump(results, r_file, indent=4)


if __name__ == '__main__':
    result_file = 'result.json'
    add_users_and_books_into_result_file(result_file)
    with open(result_file, 'r') as result_reader:
        content = result_reader.read()
        print(content)
