from surprise import SVD
import joblib

# Load the trained model
algo = joblib.load('svd_model.pkl')

def recommend_items(user_id, n=5):
    """
    Recommend n items for a given user.
    """
    # Create a list of tuples (itemID, estimated_rating) for the user
    items_to_recommend = []
    for item_id in range(1, 6):  # Assuming items are from 1 to 5
        estimated_rating = algo.predict(user_id, item_id).est
        items_to_recommend.append((item_id, estimated_rating))

    # Sort items by estimated rating in descending order
    items_to_recommend.sort(key=lambda x: x[1], reverse=True)

    # Return top n items
    return items_to_recommend[:n]

# Example: Recommend items for user 1
user_id = 1
recommended_items = recommend_items(user_id)
print(f"Top 5 recommended items for user {user_id}:")
for item_id, estimated_rating in recommended_items:
    print(f"Item ID: {item_id}, Estimated Rating: {estimated_rating:.2f}")
