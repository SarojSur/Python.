#dictionary
Phonebook = {
   "Rahul":"Italy",
   "Taran":"India",
   "Mina":"USA",
   "Rina":"UK",
 }

print(Phonebook)
print(Phonebook.keys())
print(Phonebook.values())
print(Phonebook.get("Rahul"))
print(Phonebook.get("Taran"))
print(Phonebook.get("Mina"))
print(Phonebook.get("Rina"))

Phonebook["Rahul"]="Germany"
print(Phonebook.get("Rahul"))

Phonebook["Taran"]="Vatican city"

print(Phonebook.get("Taran"))

Phonebook["Mina"]="Brazil"

print(Phonebook.get("Mina"))

Phonebook["Rina"]="Russia"
print(Phonebook.get("Rina"))













   