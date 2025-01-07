

mevalar = [
    {"nomi": "Olma", "narx": 5000, "yetishtiruvchi": "Namangan"},
    {"nomi": "Banan", "narx": 15000, "yetishtiruvchi": "Ekvador"},
    {"nomi": "Uzum", "narx": 7000, "yetishtiruvchi": "Samarqand"},
    {"nomi": "Anor", "narx": 12000, "yetishtiruvchi": "Surxondaryo"},
    {"nomi": "Shaftoli", "narx": 10000, "yetishtiruvchi": "Farg'ona"},
]

users = [
    {"ism": "Ali", "yosh": 19},
    {"ism": "Vali", "yosh": 21},
    {"ism": "Jon", "yosh": 25},
    {"ism": "Sherzod", "yosh": 30},
]

eng_katta = users[0]
for user in users[1:]:
    if user["yosh"] > eng_katta["yosh"]:
        eng_katta = user

puli = float(input("kiriting: "))

for meva in mevalar:
    miqdor = puli // meva["narx"] 
    print(f"- {meva['nomi']} ({meva['yetishtiruvchi']}): {miqdor:.0f} dona")


print(f"\nYoshi katta: {eng_katta['ism']}, Yoshi {eng_katta['yosh']}da.")