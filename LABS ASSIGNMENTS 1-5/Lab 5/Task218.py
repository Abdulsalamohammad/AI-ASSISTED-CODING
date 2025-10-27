import json
import hashlib
import os

# File to store user data
USER_FILE = "users.json"

# Load existing users if file exists
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Hash password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register new user
def register_user():
    users = load_users()

    print("\n--- Register New User ---")
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()

    if email in users:
        print("⚠️ Email already registered.")
        return

    password = input("Enter your password: ").strip()
    hashed_pw = hash_password(password)

    users[email] = {"name": name, "password": hashed_pw}
    save_users(users)
    print("✅ User registered successfully!")

# Show all users in a table format
def show_users():
    users = load_users()
    if not users:
        print("\nNo users registered yet.")
        return

    print("\n--- Registered Users ---")
    print(f"{'Name':<20} {'Email':<30}")
    print("-" * 55)
    for email, data in users.items():
        print(f"{data['name']:<20} {email:<30}")
    print("-" * 55)

# Main menu
if __name__ == "__main__":
    while True:
        print("\n" + "=" * 40)
        print("  🧑‍💻 User Data Management System")
        print("=" * 40)
        print("1. Register User")
        print("2. Show Users")
        print("3. Exit")
        print("=" * 40)

        choice = input("👉 Choose an option (1-3): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            print("👋 Exiting... Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
