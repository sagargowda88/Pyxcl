import pandas as pd

# Step 1: Read the Excel file
excel_file = 'your_excel_file.xlsx'
df = pd.read_excel(excel_file)

# Extract features (assuming they are in columns 1 to n-1) and labels (last column)
features = df.iloc[:, :-1]
labels = df.iloc[:, -1]

# Step 2: Convert features and labels into LIBSVM format
def convert_to_libsvm_format(row):
    libsvm_format = []
    for i, value in enumerate(row):
        # Skip zero values (since LIBSVM format is sparse)
        if value != 0:
            libsvm_format.append(f"{i+1}:{value}")  # Indices in LIBSVM format are 1-based
    return ' '.join(libsvm_format)

libsvm_features = features.apply(convert_to_libsvm_format, axis=1)

# Step 3: Write features and labels to separate text files
features_file = 'features.txt'
labels_file = 'labels.txt'

with open(features_file, 'w') as f:
    f.write('\n'.join(libsvm_features) + '\n')

with open(labels_file, 'w') as f:
    f.write('\n'.join(labels.astype(str)) + '\n')

print("Conversion completed. Features written to '{}' and labels written to '{}'.".format(features_file, labels_file))
