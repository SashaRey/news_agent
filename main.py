import feedparser
from datetime import datetime

url = "https://habr.com/ru/rss/hub/machine_learning/all"
feed = feedparser.parse(url)


existing_links = set()
try:
    with open("news.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(', ')
            if len(parts) >= 2:
                existing_links.add(parts[-1])

except FileNotFoundError:
    pass

with open("news.txt", "a", encoding='utf-8') as f:
    count = 0
    for entry in feed.entries[:3]:
        if entry.link not in existing_links:
            dt = datetime(*entry.published_parsed[:6])
            f.write(f"{entry.title}, {dt.strftime('%Y-%m-%d %H:%M')}, {entry.link} \n")
            count += 1
            existing_links.add(entry.link)
    print(f"Добавлено {count} строк")
