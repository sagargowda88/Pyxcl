import pandas as pd

# Read the CSV file with labels
data = pd.read_csv('your_csv_file.csv')

# Split the data into train and test based on the presence of labels
train_data = data[data['label'].notnull()]
test_data = data[data['label'].isnull()]

# Save the train and test data to separate CSV files
train_data.to_csv('train.csv', index=False)
test_data.to_csv('test.csv', index=False)
