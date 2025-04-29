import os
from pathlib import Path
from cryptography.fernet import Fernet

# Base directories
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'

# Data paths
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
SAMPLE_DATA_DIR = DATA_DIR / 'sample'

# Create directories if they don't exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, SAMPLE_DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Data file paths
RAW_DATASET_PATH = RAW_DATA_DIR / 'phishing_dataset.csv'
PROCESSED_DATASET_PATH = PROCESSED_DATA_DIR / 'processed_dataset.csv'
SAMPLE_DATASET_PATH = SAMPLE_DATA_DIR / 'sample_dataset.csv'

# Security settings
ENCRYPTION_KEY = Fernet.generate_key().decode()
DATA_ACCESS_LEVEL = os.getenv('DATA_ACCESS_LEVEL', 'restricted')  # 'restricted' or 'public'

# Data validation settings
MIN_EMAIL_LENGTH = 5
MAX_EMAIL_LENGTH = 254
ALLOWED_DOMAINS = ['gmail.com', 'outlook.com', 'yahoo.com']  # Add more as needed

# Logging settings
LOG_FILE = "data_handler.log"
LOG_LEVEL = "INFO"

# Email validation settings
MIN_EMAIL_LENGTH = 5
MAX_EMAIL_LENGTH = 254

# File paths
SAMPLE_DATASET_PATH = "data/sample_dataset.csv" 