import pandas as pd
import re

log_data = []

# Regex pattern to capture the Timestamp, ID, DLC, and the rest of the payload
pattern = re.compile(r"Timestamp:\s+([\d\.]+)\s+ID:\s+([0-9a-fA-F]+)\s+\d+\s+DLC:\s+(\d+)\s+(.*)")

with open('normal_run_data.txt', 'r') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            timestamp = float(match.group(1))
            can_id = match.group(2)
            dlc = int(match.group(3))
            
            # Extract the hex payload and split it by spaces into a list
            payload_str = match.group(4).strip()
            payload_bytes = payload_str.split()
            
            # Ensure there are exactly 8 data bytes. If DLC < 8, pad with '00'
            while len(payload_bytes) < 8:
                payload_bytes.append('00')
            
            # Build the row and append the label (0 = Normal)
            row = [timestamp, can_id, dlc] + payload_bytes[:8] + [0]
            log_data.append(row)

# Convert the parsed list into a DataFrame matching the CSV structure
columns = ['Timestamp', 'CAN_ID', 'DLC', 'DATA_0', 'DATA_1', 'DATA_2', 
           'DATA_3', 'DATA_4', 'DATA_5', 'DATA_6', 'DATA_7', 'Label']

df_normal = pd.DataFrame(log_data, columns=columns)