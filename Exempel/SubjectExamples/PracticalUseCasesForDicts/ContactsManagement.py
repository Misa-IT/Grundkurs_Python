# Detta exempel är helt AI-genererat

# Creating a contacts dictionary
contacts = {
    "John": {
        "phone": "555-1234",
        "email": "john@example.com",
        "address": "123 Main St"
    },
    "Sarah": {
        "phone": "555-5678",
        "email": "sarah@example.com",
        "address": "456 Oak Ave"
    },
    "Mike": {
        "phone": "555-9012",
        "email": "mike@example.com",
        "address": "789 Pine Rd"
    }
}

# Accessing specific information
print(f"John's phone number: {contacts['John']['phone']}")

# Adding a new contact
contacts["Lisa"] = {
    "phone": "555-3456",
    "email": "lisa@example.com",
    "address": "321 Elm St"
}

# Updating information
contacts["John"]["phone"] = "555-4321"

# Iterating through all contacts
print("\nAll contacts:")
for name, info in contacts.items():
    print(f"{name}: {info['phone']}, {info['email']}")

# Searching for contacts by name fragment
search_term = "sa"
print(f"\nContacts containing '{search_term}':")
for name in contacts:
    if search_term.lower() in name.lower():
        print(f"{name}: {contacts[name]['phone']}")