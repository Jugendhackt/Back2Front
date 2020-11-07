import praw
import csv
import os

# Erstelle eine Verbingung über den User JugendHackt_Reddit mit der Anwendung JugendHacktReddit
user = praw.Reddit(
    client_id=os.environ.get("CLIENT_ID"),
    client_secret=os.environ.get("CLIENT_SECRET"),
    user_agent="JugendHacktReddit",
    username="JugendHackt_Reddit",
    password=os.environ.get("REDDIT_PASSWORD")
)


def get_top_from(subreddit, post_limit):
    """
    Liest so viele Top-Posts des subreddits, wie in post_limit angegeben
    :param subreddit: Das Subreddit, aus dem die Posts gelesen werden sollen
    :param post_limit: Das Post-Limit
    :return: Die Dictionary-Liste der Posts
    """
    subred = user.subreddit(subreddit)
    top_posts = subred.top(limit=post_limit)

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
            content = post.selftext.replace("\n", "\\n")
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
    return post_list


def write_in_csv(path, post_list):
    """
    Schreibt die post_list in ein .csv File
    :param path: Der Pfad der .csv-Zieldatei
    :param post_list: Die Liste der Posts
    :return: None
    """
    with open(path, 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = post_list[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for post_data in post_list:
            writer.writerow(post_data)


# Führt die Funktionen aus

top = get_top_from("de", 100)

print(f"Das Post-Dictionary: {top}")
print(f"Die Anzahl der erhaltenen Posts: {len(top)}")

write_in_csv("../data/postdata.csv", top)
