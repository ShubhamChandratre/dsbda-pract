from bs4 import BeautifulSoup

# Load HTML
with open("Meesho.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

# Extract reviews
reviews = soup.find_all("div", class_="sc-iBYQkv fCRAHG")

# Write to file
with open("meesho_reviews.txt", "w", encoding="utf-8") as f:
    for review in reviews:
        name = review.select_one("span.sc-eDvSVe.dugLmN")
        rating = review.select_one("span.sc-eDvSVe.laVOtN")
        comment = review.select_one("span.sc-eDvSVe.gUjMRV.Comment__CommentText-sc-1ju5q0e-3")

        f.write(f"Name: {name.get_text(strip=True) if name else 'N/A'}\n")
        f.write(f"Rating: {rating.get_text(strip=True) if rating else 'N/A'}\n")
        f.write(f"Comment: {comment.get_text(strip=True) if comment else 'N/A'}\n")
        f.write("-" * 40 + "\n")

print("Saved to meesho_reviews.txt")