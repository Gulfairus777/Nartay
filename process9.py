import pandas as pd
from datetime import datetime

# Укажи путь к файлам
input_path = r'C:\Users\user\hw-2025\original9.csv'
output_path = r'C:\Users\user\hw-2025\result9.csv'

# Чтение оригинального CSV
df = pd.read_csv(input_path)

# Преобразуем в datetime
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])

# Расчёт разницы
time_diff = df['end_time'] - df['start_time']
df['days'] = time_diff.dt.days
df['hours'] = (time_diff.dt.total_seconds() // 3600).astype(int)
df['minutes'] = (time_diff.dt.total_seconds() // 60).astype(int)
df['seconds'] = time_diff.dt.total_seconds().astype(int)

# Сохраняем в новый CSV
df[['start_time', 'end_time', 'days', 'hours', 'minutes', 'seconds', 'participants', 'name']].to_csv(output_path, index=False)

print("✅ result9.csv успешно создан!")

