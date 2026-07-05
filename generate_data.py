import pandas as pd
import numpy as np
from datetime import datetime,timedelta


np.random.seed(42)

devices = ['Device_A', 'Device_B', 'Device_C', 'Device_D', 'Device_E']
start_date = datetime(2026, 1, 1)
timestamps = [start_date + timedelta(minutes=15*i) for i in range(2880)]

data = []
for device in devices:
    base_temp = np.random.uniform(20, 25)
    base_energy = np.random.uniform(50, 100)
    for ts in timestamps:
        temp = base_temp + np.random.normal(0, 1.5)
        humidity = np.random.uniform(30, 60)
        energy = base_energy + np.random.normal(0, 5)
        vibration = np.random.uniform(0.1, 0.5)

        if np.random.rand() < 0.02:
            temp += np.random.uniform(10, 20)
            energy += np.random.uniform(30, 50)

        data.append([ts, device, round(temp,2), round(humidity,2),
                     round(energy,2), round(vibration,3)])

df = pd.DataFrame(data, columns=['timestamp','device_id','temperature',
                                   'humidity','energy_consumption','vibration'])
df.to_csv('iot_sensor_data.csv', index=False)
print(df.head())
print(f"Total rows: {len(df)}")