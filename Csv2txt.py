import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('your_data.csv')

# Step 2: Perform one-hot encoding for labels
df = pd.get_dummies(df, columns=['label_column'])  # Assuming 'label_column' is the name of your label column

# Step 3: Convert data into libsvm format and write to a new file
with open('converted_data.txt', 'w') as f:
    # Write header containing the number of samples, features, and labels
    f.write(f"{len(df)} {len(df.columns)-1} {len(df.columns)-1}\n")

    # Iterate over each row
    for index, row in df.iterrows():
        label = int(row[-len(df.columns)+1:])  # Extract the one-hot encoded label
        features = row.drop(labels=df.columns[-len(df.columns)+1:])  # Drop the label columns
        feature_values = ' '.join(f"{i+1}:{value}" for i, value in enumerate(features) if value != 0)
        f.write(f"{label} {feature_values}\n")

print("Conversion completed. Data written to 'converted_data.txt'.")
