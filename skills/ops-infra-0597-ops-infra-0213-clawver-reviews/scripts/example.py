response = api.get("/v1/stores/me/reviews")
reviews = response["data"]["reviews"]
unanswered = [r for r in reviews if r["response"] is None]
print(f"Unanswered reviews: {len(unanswered)}")


response = api.get("/v1/stores/me/reviews")
reviews = response["data"]["reviews"]

distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for review in reviews:
    distribution[review["rating"]] += 1

total = len(reviews)
for rating, count in distribution.items():
    pct = (count / total * 100) if total > 0 else 0
    print(f"{rating} stars: {count} ({pct:.1f}%)")


def check_and_respond_to_reviews():
    response = api.get("/v1/stores/me/reviews")
    reviews = response["data"]["reviews"]

    for review in reviews:
        # Skip if already responded
        if review["response"]:
            continue

        # Auto-respond based on rating
        if review["rating"] >= 4:
            response_text = "Thank you for your wonderful review! We're thrilled you love the product."
        elif review["rating"] == 3:
            response_text = "Thank you for your feedback! We're always looking to improve."
        else:
            # Flag for manual review
            print(f"Negative review needs attention: {review['id']}")
            continue

        api.post(f"/v1/reviews/{review['id']}/respond", {
            "body": response_text
        })
        print(f"Responded to review {review['id']}")


def check_sentiment_trend():
    response = api.get("/v1/stores/me/reviews")
    reviews = response["data"]["reviews"]

    # Get last 10 reviews (already sorted by date)
    recent = reviews[:10]

    if not recent:
        return

    avg_rating = sum(r["rating"] for r in recent) / len(recent)
    negative_count = sum(1 for r in recent if r["rating"] <= 2)

    if avg_rating < 3.5:
        print("Warning: Recent review sentiment is declining")

    if negative_count >= 3:
        print("Warning: Multiple negative reviews in recent batch")
