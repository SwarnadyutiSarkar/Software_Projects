from surprise import accuracy
import joblib

# Load the trained model
algo = joblib.load('svd_model.pkl')

# Predict ratings for the testset
predictions = algo.test(testset)

# Evaluate model performance (Root Mean Squared Error)
rmse = accuracy.rmse(predictions)
print(f'RMSE on test set: {rmse}')
