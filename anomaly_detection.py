import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

df=pd.read_csv('iot_features.csv')

features = ['vibration', 'acoustic', 'temperature', 'current', 'IMF_1', 'IMF_2', 'IMF_3']

model= IsolationForest(contamination=0.1,random_state=42)
df['prediction'] = model.fit_predict(df[features])

df['predicted_status'] = df['prediction'].apply(lambda x:'Fault' if x == -1 else 'Normal')

print("Model Performance Report:")
print(classification_report(df['label'], df['prediction'].apply(lambda x: 1 if x == -1 else 0)))

df.to_csv('iot_final_with_anomalies.csv',index=False)


print("\nAnomaly detection complete!")
print(f"Predicted Fault count: {(df['predicted_status']=='Fault').sum()}")
print(f"Actual Fault count: {(df['status']=='Fault').sum()}")
print("\nSaved as: iot_final_with_anomalies.csv")