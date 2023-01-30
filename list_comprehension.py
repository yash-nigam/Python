names = ["john smith", "jay santi", "eva kuki"]

newnames = [name.title() for name in names]

print(newnames)

usernames = ["john 1990", "alberta1970", "magnola2000"]

newu = [len(name) for name in usernames]
print(newu)

user_entries = ['10', '19.1', '20']
user_entries = [float(ue) for ue in user_entries]
print(user_entries)


user_entries2 = ['10', '19.1', '20']
user_entriesfl = [ float(uefl) for uefl in user_entries2]
print(sum(user_entriesfl))
