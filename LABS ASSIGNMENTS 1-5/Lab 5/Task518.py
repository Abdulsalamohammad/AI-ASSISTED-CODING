from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample product dataset
products = [
    {"id": 1, "name": "iPhone 14", "category": "Smartphone", "brand": "Apple", "price": 799, "rating": 4.7},
    {"id": 2, "name": "Samsung Galaxy S23", "category": "Smartphone", "brand": "Samsung", "price": 749, "rating": 4.6},
    {"id": 3, "name": "MacBook Air", "category": "Laptop", "brand": "Apple", "price": 999, "rating": 4.8},
    {"id": 4, "name": "Dell XPS 13", "category": "Laptop", "brand": "Dell", "price": 899, "rating": 4.5},
    {"id": 5, "name": "iPad Pro", "category": "Tablet", "brand": "Apple", "price": 799, "rating": 4.7},
    {"id": 6, "name": "Samsung Galaxy Tab", "category": "Tablet", "brand": "Samsung", "price": 699, "rating": 4.4}
]

# Convert product category + brand into text features
corpus = [p["category"] + " " + p["brand"] for p in products]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Compute similarity
similarity_matrix = cosine_similarity(X)

def recommend_products(product_name, top_n=3):
    # Find the product index
    product_idx = None
    for idx, p in enumerate(products):
        if p["name"].lower() == product_name.lower():
            product_idx = idx
            break
    if product_idx is None:
        return f"❌ Product '{product_name}' not found."
    
    scores = list(enumerate(similarity_matrix[product_idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for idx, score in scores[1:top_n+1]:
        reason = []
        target = products[product_idx]
        candidate = products[idx]

        # Reason 1: Same Category
        if target["category"] == candidate["category"]:
            reason.append("Same category")
        # Reason 2: Same Brand
        if target["brand"] == candidate["brand"]:
            reason.append("Same brand")
        # Reason 3: Similar Price Range
        if abs(target["price"] - candidate["price"]) <= 100:
            reason.append("Similar price range")
        # Reason 4: Both Highly Rated
        if target["rating"] >= 4.5 and candidate["rating"] >= 4.5:
            reason.append("Both are highly rated")

        recommendations.append({
            "product": candidate["name"],
            "similarity": round(score, 2),
            "reasons": reason if reason else ["Similar customer preferences"]
        })

    return recommendations


# Example usage
product = "iPhone 14"
results = recommend_products(product)

print(f"🛒 Because you viewed **{product}**, we recommend:")
for rec in results:
    print(f"- {rec['product']} (Similarity: {rec['similarity']})")
    print(f"  👉 Reasons: {', '.join(rec['reasons'])}")
