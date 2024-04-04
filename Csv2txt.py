import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# Step 1: Read the Excel file
excel_file = 'your_excel_file.xlsx'
df = pd.read_excel(excel_file)

# Assuming your Excel file has features in columns 1 to n-1 and labels in the last column
features = df.iloc[:, :-1].values
labels = df.iloc[:, -1].values.reshape(-1, 1)  # Reshape labels to make it a column vector

# Step 2: Perform one-hot encoding for labels
mlb = MultiLabelBinarizer()
labels_one_hot = mlb.fit_transform(labels)

# Step 3: Write features and one-hot encoded labels to separate text files
features_file = 'features.txt'
labels_file = 'labels_one_hot.txt'

# Write features to file
with open(features_file, 'w') as f:
    for row in features:
        f.write(' '.join(map(str, row)) + '\n')

# Write one-hot encoded labels to file
with open(labels_file, 'w') as f:
    for row in labels_one_hot:
        f.write(' '.join(map(str, row)) + '\n')

print("Conversion completed. Features written to '{}' and one-hot encoded labels written to '{}'.".format(features_file, labels_file))
