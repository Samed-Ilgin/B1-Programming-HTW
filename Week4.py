#EXERCISE 1

login_attempts = [("alice", "success"), ("bob", "failed"), ("bob", "failed"), ("charlie", "success"), ("bob", "failed"), ("alice", "failed")]

failed_attempts = {}

for user,attempt_result in login_attempts:
    if attempt_result == "failed":
        if user in failed_attempts:
         failed_attempts[user] = failed_attempts[user] + 1
        else: failed_attempts[user] = 1
         
for user, count in failed_attempts.items():
    if count >= 3:
        print(f"ALERT: User '{user}' has {count} failed login attempts")



#EXERCISE 2

devices = [("192.168.1.10", [22, 80, 443]), ("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23, 80, 3389])]

risky_ports = [21, 23, 3389]

for ip, ports in devices:
    for port in ports:
        if port in risky_ports:
            print(f"Warning: Risky port found! IP: {ip}, Port: {port}")





#EXERCISE 3

passwords = ["Pass123", "SecurePassword1", "weak", "MyP@ssw0rd", "NOLOWER123"]

valid_passwords = []
invalid_passwords = []

for password in passwords:
    print(f"Checking: {password}")
    
    if len(password) < 8:
        print("Invalid: Too short")
        invalid_passwords.append(password)
    elif not any(c.isupper() for c in password):
        print("Invalid: No uppercase letters included")
        invalid_passwords.append(password)
    elif not any(c.islower() for c in password):
        print("Invalid: No lowercase letters included")
        invalid_passwords.append(password)
    elif not any(c.isdigit() for c in password):
        print("Invalid: No digits included")
        invalid_passwords.append(password)
    else:
        print("Password is valid!")
        valid_passwords.append(password)

print("Summary:")

print(f"Valid passwords: {valid_passwords}")
print(f"Invalid passwords: {invalid_passwords}")