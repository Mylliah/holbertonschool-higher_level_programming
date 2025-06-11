#!/usr/bin/python3
"""
Module for fetching and handling posts from an API.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch and print post titles from the API.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Error retrieving posts.")


def fetch_and_save_posts():
    """
    Fetch posts from the API and save them to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=['id', 'title', 'body']
            )
            writer.writeheader()
            writer.writerows(filtered_posts)
    else:
        print("Error retrieving posts.")
