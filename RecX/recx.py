# recx.py
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load dataset
file_path = 'ratings.csv'
reader = Reader(line_format='user item rating', sep=',')
data = Dataset.load_from_file(file_path, reader=reader)

# Split the dataset into train and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Use Singular Value Decomposition (SVD) algorithm
algo = SVD()

# Train the algorithm on the trainset
algo.fit(trainset)

# Predict ratings for the testset
predictions = algo.test(testset)

# Evaluate model performance (Root Mean Squared Error)
accuracy.rmse(predictions)

# Example: Recommend items for a given user
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
