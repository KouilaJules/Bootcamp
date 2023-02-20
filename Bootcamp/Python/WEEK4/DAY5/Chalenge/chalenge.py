# Lecture de la séquence de mots séparés par des virgules en entrée
input_string = input("Entrez une séquence de mots séparés par des virgules : ")

# Séparation des mots en utilisant la virgule comme délimiteur
words = input_string.split(",")

# Tri des mots par ordre alphabétique en utilisant la compréhension de liste
sorted_words = sorted([word.strip() for word in words])

# Concaténation des mots triés en une chaîne de caractères séparés par des virgules
output_string = ",".join(sorted_words)

# Affichage de la chaîne de caractères triée
print(output_string)