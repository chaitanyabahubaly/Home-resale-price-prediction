import pandas as pd
import numpy as np

# Generate synthetic data
num_records = 400
data = {
    'area': np.random.randint(500, 5000, num_records),  # Area in square feet
    'bedrooms': np.random.randint(1, 5, num_records),  # Number of bedrooms
    'bathrooms': np.random.randint(1, 4, num_records),  # Number of bathrooms
    'location': np.random.choice(
        ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
         'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
         'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
         'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
         'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'], num_records),  # Indian states
    'year_built': np.random.randint(1950, 2023, num_records),  # Year built
}

# Calculate sale price with some random noise
base_price = 50000
data['sale_price'] = (
    base_price +
    data['area'] * 150 +
    data['bedrooms'] * 10000 +
    data['bathrooms'] * 8000 +
    np.where(data['location'] == 'Urban', 50000, np.where(data['location'] == 'Suburban', 30000, 10000)) +
    (2023 - data['year_built']) * -200 +  # Depreciation over time
    np.random.randint(-10000, 10000, num_records)  # Random noise
)

# Create DataFrame
house_data = pd.DataFrame(data)

# Save to CSV
csv_file_path = '/mnt/data/house_data_indian_states.csv'
house_data.to_csv(csv_file_path, index=False)

csv_file_path
