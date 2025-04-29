import pandas as pd
import os
from pathlib import Path
import logging
from cryptography.fernet import Fernet
import sys

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.data_config import *

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SecureDataHandler:
    def __init__(self):
        self.fernet = Fernet(ENCRYPTION_KEY.encode()) if ENCRYPTION_KEY else None
        
    def load_data(self, file_path, encrypted=False):
        """Securely load data from file"""
        try:
            if encrypted and self.fernet:
                with open(file_path, 'rb') as file:
                    encrypted_data = file.read()
                    decrypted_data = self.fernet.decrypt(encrypted_data)
                    return pd.read_csv(pd.io.common.StringIO(decrypted_data.decode()))
            return pd.read_csv(file_path)
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise

    def save_data(self, df, file_path, encrypt=False):
        """Securely save data to file"""
        try:
            if encrypt and self.fernet:
                csv_data = df.to_csv(index=False)
                encrypted_data = self.fernet.encrypt(csv_data.encode())
                with open(file_path, 'wb') as file:
                    file.write(encrypted_data)
            else:
                df.to_csv(file_path, index=False)
            logger.info(f"Data saved successfully to {file_path}")
        except Exception as e:
            logger.error(f"Error saving data: {str(e)}")
            raise

    def validate_email_data(self, df):
        """Validate email data for security"""
        try:
            # Check email length
            df['email_length'] = df['sender'].str.len()
            invalid_emails = df[
                (df['email_length'] < MIN_EMAIL_LENGTH) | 
                (df['email_length'] > MAX_EMAIL_LENGTH)
            ]
            
            if not invalid_emails.empty:
                logger.warning(f"Found {len(invalid_emails)} invalid emails")
                return False
            return True
        except Exception as e:
            logger.error(f"Error validating email data: {str(e)}")
            raise

    def create_sample_dataset(self, original_df, sample_size=100):
        """Create a sample dataset for public use"""
        try:
            # Remove sensitive information
            sample_df = original_df.copy()
            sample_df['sender'] = sample_df['sender'].apply(
                lambda x: f"user{hash(x) % 1000}@example.com"
            )
            # Add more anonymization as needed
            
            # Save sample dataset
            self.save_data(sample_df, SAMPLE_DATASET_PATH)
            logger.info(f"Sample dataset created with {sample_size} records")
            return sample_df
        except Exception as e:
            logger.error(f"Error creating sample dataset: {str(e)}")
            raise 