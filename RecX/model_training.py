from surprise import SVD
from surprise.model_selection import train_test_split
import joblib

# Load dataset (assuming data is already loaded using data_loading.py)
# Split the dataset into train and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Use Singular Value Decomposition (SVD) algorithm
algo = SVD()

# Train the algorithm on the trainset
algo.fit(trainset)

# Save the trained model
joblib.dump(algo, 'svd_model.pkl')
