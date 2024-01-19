import os
import hashlib
from datetime import datetime

def is_id_exists(user_id, file_name):
    
    with open(file_name, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:  
                stored_id = parts[0]
                if user_id == stored_id:
                    return True
    return False

def generate_password_file():
    while True:
        user_id = input("Enter your ID (lowercase letters only): ")
        if not user_id.islower():
            print("The ID should only contain lowercase letters.")
            continue

        if is_id_exists(user_id, "hashpasswd"):
            print("The ID already exists.")
            choice = input("Would you like to enter another ID and Password (Y/N)? ")
            if choice.lower() != 'y':
                break
            continue

        password = input("Enter your password (at least 8 characters): ")
        if len(password) < 8:
            print("The password should contain at least 8 characters.")
            continue

   
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        
        with open("hashpasswd", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{user_id} {hashed_password} {timestamp}\n")

        choice = input("Would you like to enter another ID and Password (Y/N)? ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    generate_password_file()
