import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the training data
train_data = pd.read_csv('C:\\Users\\vg8rw\\Documents\\homework\\hw2\\ML2025Spring-hw2-public\\train.csv')

# Load the test data
test_data = pd.read_csv('C:\\Users\\vg8rw\\Documents\\homework\\hw2\\ML2025Spring-hw2-public\\test.csv')

# Select the features with the highest correlation to 'tested_positive_day3'
features = ['tested_positive_day2', 'tested_positive_day1', 'hh_cmnty_cli_day1', 'nohh_cmnty_cli_day1', 'hh_cmnty_cli_day2', 'wnohh_cmnty_cli_day1', 'nohh_cmnty_cli_day2', 'wnohh_cmnty_cli_day2', 'hh_cmnty_cli_day3']

# Prepare the training data
X_train = train_data[features]
y_train = train_data['tested_positive_day3']

# Prepare the test data
X_test = test_data[features]

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Create the submission file
submission = pd.DataFrame({
    'id': test_data['id'],
    'tested_positive_day3': predictions
})

# Save the predictions
submission.to_csv('./submission.csv', index=False)