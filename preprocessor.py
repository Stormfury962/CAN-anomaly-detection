def preprocess_can_data(df):
    # 1. Convert Hex to Decimal
    df['CAN_ID_Dec'] = df['CAN_ID'].apply(lambda x: int(str(x), 16))
    for i in range(8):
        df[f'DATA_{i}_Dec'] = df[f'DATA_{i}'].apply(lambda x: int(str(x), 16))
        
    # 2. Sort by timestamp (critical for timing features)
    df = df.sort_values(by='Timestamp').reset_index(drop=True)
    
    # 3. Calculate time intervals between messages of the same ID
    df['Delta_Time'] = df.groupby('CAN_ID_Dec')['Timestamp'].diff().fillna(0)
    
    # 4. Keep only the machine-learning ready columns
    numerical_cols = ['Delta_Time', 'CAN_ID_Dec'] + [f'DATA_{i}_Dec' for i in range(8)] + ['Label']
    
    return df[numerical_cols]

