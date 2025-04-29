import os
import sys
import pandas as pd

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.data_handler import SecureDataHandler
from config.data_config import *

def test_encryption_decryption():
    # Initialize the data handler
    handler = SecureDataHandler()
    
    # Create a sample DataFrame
    test_data = {
        'sender': ['test1@example.com', 'test2@example.com'],
        'subject': ['Test Subject 1', 'Test Subject 2'],
        'content': ['Test Content 1', 'Test Content 2']
    }
    df = pd.DataFrame(test_data)
    
    # Test file paths
    encrypted_file = 'test_encrypted.csv'
    decrypted_file = 'test_decrypted.csv'
    
    try:
        # Test encryption
        print("Testing encryption...")
        handler.save_data(df, encrypted_file, encrypt=True)
        print("✓ Encryption successful")
        
        # Test decryption
        print("\nTesting decryption...")
        decrypted_df = handler.load_data(encrypted_file, encrypted=True)
        print("✓ Decryption successful")
        
        # Verify data integrity
        print("\nVerifying data integrity...")
        assert df.equals(decrypted_df), "Data integrity check failed"
        print("✓ Data integrity verified")
        
        # Test email validation
        print("\nTesting email validation...")
        is_valid = handler.validate_email_data(df)
        assert is_valid, "Email validation failed"
        print("✓ Email validation successful")
        
        print("\nAll tests passed successfully!")
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
    finally:
        # Clean up test files
        if os.path.exists(encrypted_file):
            os.remove(encrypted_file)
        if os.path.exists(decrypted_file):
            os.remove(decrypted_file)

if __name__ == "__main__":
    test_encryption_decryption() 