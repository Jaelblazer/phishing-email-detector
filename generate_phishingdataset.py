import pandas as pd
import random
from datetime import datetime, timedelta
import csv

# Lists for generating random data
senders_phishing = [
    'security@bank-alert.com', 'noreply@paypa1.com', 'admin@micros0ft.com',
    'support@amaz0n-deals.com', 'alerts@chasebankk.com', 'unknown@suspicious.com'
]
senders_legit = [
    'john.doe@gmail.com', 'support@linkedin.com', 'notifications@github.com',
    'team@trello.com', 'info@outlook.com', 'updates@google.com'
]

subjects_phishing = [
    'Urgent: Account Verification Required!',
    'Claim Your Prize Now!',
    'Security Alert: Suspicious Login',
    'You Won $1000 - Click to Redeem',
    'Update Your Payment Info Immediately'
]
subjects_legit = [
    'Meeting Reminder: 2 PM Today',
    'Your Monthly Statement',
    'Project Update from Team',
    'Welcome to Our Service!',
    'Password Reset Confirmation'
]

keywords_phishing = [
    'urgent security update', 'win free prize', 'claim now',
    'crypto bonus', 'verify immediately', 'winner alert'
]
keywords_legit = [
    'meeting agenda', 'invoice details', 'team collaboration',
    'welcome message', 'reset instructions', 'update notification'
]

# Function to generate random timestamp within last year
def random_timestamp():
    start_date = datetime.now() - timedelta(days=365)
    random_days = random.randint(0, 365)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    return (start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)).strftime('%Y-%m-%d %H:%M')

# Generate dataset
data = []
num_entries = 3500  # More than 1200 entries

for _ in range(num_entries):
    is_phishing = random.choice([True, False])
    
    if is_phishing:
        sender = random.choice(senders_phishing)
        subject = random.choice(subjects_phishing)
        keywords = random.choice(keywords_phishing)
        label = 'phishing'
    else:
        sender = random.choice(senders_legit)
        subject = random.choice(subjects_legit)
        keywords = random.choice(keywords_legit)
        label = 'legitimate'
    
    has_url = random.choice([0, 1])
    has_attachment = random.choice([0, 1])
    timestamp = random_timestamp()
    
    data.append({
        'sender': sender,
        'subject': subject,
        'keywords': keywords,
        'has_url': has_url,
        'has_attachment': has_attachment,
        'timestamp': timestamp,
        'label': label
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('phishingdataset.csv', index=False, quoting=csv.QUOTE_ALL)

print(f"Generated phishingdataset.csv with {len(df)} entries.")