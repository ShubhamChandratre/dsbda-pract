from bs4 import BeautifulSoup

# Load HTML
with open("Flipkart.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

# Extract reviews
reviews = soup.find_all("div", class_="EKFha-")

# Write to file
with open("flipkart_reviews.txt", "w", encoding="utf-8") as f:
    for review in reviews:
        name = review.select_one("p._2NsDsF.AwS1CA")
        rating = review.select_one(".XQDdHH.Ga3i8K")
        comment = review.select_one(".ZmyHeo div div")

        f.write(f"Name: {name.get_text(strip=True) if name else 'N/A'}\n")
        f.write(f"Rating: {rating.get_text(strip=True)[:1] if rating else 'N/A'}\n")
        f.write(f"Comment: {comment.get_text(strip=True) if comment else 'N/A'}\n")
        f.write("-" * 40 + "\n")

print("Saved to flipkart_reviews.txt")