import pandas as pd

# Real Kaggle dataset load karein
df = pd.read_csv('predictive_maintenance_dataset.csv', parse_dates=['timestamp'])

# Missing values check karein
print("Missing values:")
print(df.isnull().sum())

# Duplicate rows remove karein
df = df.drop_duplicates()

# Time-based features add karein
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.date
df['day_of_week'] = df['timestamp'].dt.day_name()

# Sort karein machine aur time ke hisaab se
df = df.sort_values(['machine_id', 'timestamp'])

# Rolling averages add karein (last 5 minute ka average, real-time smoothing)
df['temp_rolling_avg'] = df.groupby('machine_id')['temperature'].transform(
    lambda x: x.rolling(5, min_periods=1).mean())

df['vibration_rolling_avg'] = df.groupby('machine_id')['vibration'].transform(
    lambda x: x.rolling(5, min_periods=1).mean())

df['current_rolling_avg'] = df.groupby('machine_id')['current'].transform(
    lambda x: x.rolling(5, min_periods=1).mean())

# Label ko readable banayein
df['status'] = df['label'].apply(lambda x: 'Fault' if x == 1 else 'Normal')

# Final cleaned file save karein
df.to_csv('iot_features.csv', index=False)

print("\nCleaning complete!")
print(f"Total rows after cleaning: {len(df)}")
print(f"Fault count: {(df['label']==1).sum()}")
print(f"Normal count: {(df['label']==0).sum()}")
print("\nSaved as: iot_features.csv")