import encryption_functions as ef
import getpass
import os

def main():
    while True:
        print("\nAdvanced Encryption Tool")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the path to the file to encrypt: ")
            if not os.path.exists(file_path):
                print("Error: File not found.")
                continue
            password = getpass.getpass("Enter the encryption password: ")
            if ef.encrypt_file(file_path, password):
                print("File encrypted successfully.")
            else:
                print("File encryption failed.")

        elif choice == '2':
            file_path = input("Enter the path to the file to decrypt: ")
            if not os.path.exists(file_path):
                print("Error: File not found.")
                continue
            password = getpass.getpass("Enter the decryption password: ")
            if ef.decrypt_file(file_path, password):
                print("File decrypted successfully.")
            else:
                print("File decryption failed.")

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()