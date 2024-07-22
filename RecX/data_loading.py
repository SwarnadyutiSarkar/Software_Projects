import pandas as pd
from surprise import Dataset, Reader

# File path to your dataset
file_path = 'ratings.csv'

# Define the format of the dataset
reader = Reader(line_format='user item rating', sep=',')

# Load dataset
data = Dataset.load_from_file(file_path, reader=reader)

# Optionally, you can convert the dataset to a Pandas DataFrame for further analysis
df = pd.DataFrame(data.raw_ratings, columns=['user', 'item', 'rating', 'timestamp'])
print(df.head())
