
# homework8_joshua_erlandsen.py
# Conditional Lists + Nested Dictionaries assignment

# -----------------------------
# Conditional Lists
# -----------------------------
web_users = ["mick_jagger", "keith_richards", "jimmy_page", "robert_plant", "john_lennon"]

new_users = ["kurt_cobain", "layne_staley", "eddie_vedder", "mick_jagger", "john_lennon"]

for user in new_users:
    if user in web_users:
        print("This user name is already in use. Please choose a different user name.")
    else:
        print("This user name is available.")

print("\n")  # blank line between sections


# -----------------------------
# Nested Dictionaries
# -----------------------------
cities = {}

cities["Seattle"] = {
    "country": "United States",
    "population": 749256,
    "fact": "Software / cloud technology exports (major hub for tech)."
}

cities["Jakarta"] = {
    "country": "Indonesia",
    "population": 10770487,
    "fact": "Manufactured goods and textiles are major export categories."
}

cities["Oslo"] = {
    "country": "Norway",
    "population": 709037,
    "fact": "Petroleum and petroleum-related products are Norway’s largest exports."
}

for city_name, details in cities.items():
    print(f"City: {city_name}")
    print(f"\tCountry: {details['country']}")
    print(f"\tPopulation: {details['population']}")
    print(f"\tFact: {details['fact']}")
