###################################
# Code snippets for this task, the bcrypt library does have a range of other methods not required for this task
###################################

import bcrypt

# Plain text byte string
my_password = b"I Am All The Jedi"

# Salt to add to password before Hashing
salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

# Hashed Password
hashed_password = bcrypt.hashpw(password=my_password, salt=salt)

# Convert byte string to a string
print(f"Actual Password: {my_password.decode('utf-8')}")

# Print Hashed Password
print(f"Hashed Password: {hashed_password.decode('utf-8')}")

# Check if a plain text password matches a hashed password. It returns a Boolean value.
print(bcrypt.checkpw(my_password, hashed_password))
