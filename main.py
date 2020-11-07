

import praw
import csv


user = praw.Reddit(
    client_id="O52kntr4n-4zYQ",
    client_secret="8lrLj6TnHRfonXdiaZJ-amgKz2CqXg",
    user_agent="JugendHackt_Reddit",
    username="JugendHackt_Reddit",
    password="ichmagalpakas"
)

subred = user.subreddit("de")
top_posts = subred.top(limit=100)


post_list = []

for post in top_posts:

    # Wenn es keinen Flair gibt, dann wird "[none]" übergeben
    if post.link_flair_text is not None:
        flair = post.link_flair_text
    else:
        flair = "[none]"

    # Wenn der Autor nicht mehr existiert, dann wird "[unknown]" übergeben
    if post.author is not None:
        author_name = post.author.name
    else:
        author_name = "[unknown]"

    # Wenn es sich beim Content um ein Bild handelt, wird dessen URL übergeben
    if post.is_self:
        content = post.selftext
    else:
        content = post.url


    # Übergibt die Werte in ein Dictionary
    post_dict = {
        "title": post.title,
        "flair": flair,
        "author": author_name,
        "created_utc": post.created_utc,
        "content": content,
        "score": post.score,
        "ratio": post.upvote_ratio,
        "award_count": len(post.awarders)
    }

    post_list.append(post_dict)


print(post_list)

"""
with open('postdata.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = post_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for post_data in post_list:
        writer.writerow(post_data)
"""
