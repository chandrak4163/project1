import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Step 1: Sample restaurant review dataset
data = {
    "review": [
        "The food was amazing and the service was excellent!",
        "Horrible experience, the waiter was rude.",
        "I loved the ambience and the menu choices.",
        "The pasta was undercooked and tasteless.",
        "Absolutely fantastic! Will come again.",
        "Worst restaurant I've been to.",
        "Delicious desserts, very satisfied.",
        "Not worth the price. Very disappointed.",
        "Great place for a family dinner.",
        "Terrible hygiene and long wait times."
    ],
    "sentiment": [
        "positive", "negative", "positive", "negative", "positive",
        "negative", "positive", "negative", "positive", "negative"
    ]
}

# Step 2: Load into DataFrame
df = pd.DataFrame(data)

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(
    df["review"], df["sentiment"], test_size=0.3, random_state=42
)

# Step 4: Text vectorization using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Step 5: Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train_vectors, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test_vectors)
print("Model Evaluation:\n")
print(classification_report(y_test, y_pred))

# Step 7: Define a prediction function
def predict_sentiment(review):
    review = review.strip()
    if not review:
        return "Invalid input. Please enter a non-empty review."
    vec = vectorizer.transform([review])
    prediction = model.predict(vec)[0]
    return prediction

# Step 8: Take user input
new_review = input("\nEnter a restaurant review: ").strip()
result = predict_sentiment(new_review)
print("\nReview:", new_review)
print("Predicted Sentiment:", result)
