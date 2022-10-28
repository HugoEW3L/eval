print(""".__                         
|  |__  __ __  ____   ____  
|  |  \|  |  \/ ___\ /  _ \ 
|   Y  \  |  / /_/  >  <_> )
|___|  /____/\___  / \____/ 
     \/     /_____/  """)

print("Entrez un chiffre : ")
print("1. Afficher le nombre de ligne")
print("2. Afficher le nombre de mots")
print("3. Afficher la frequence d'apparition de chaque mot")

operation = input()

if operation == 1:
    file = open("read.txt")

    count = 0

    for line in file:
        count = count + 1

    print("Nombre de lignes dans le fichier : ", count)
elif operation == 2:
    file = open("read.txt")

    inp = file.read()

    print(len(inp))

    print("Nombre de mots dans le fichier : ", len(inp))
elif operation == 3:
    file = open("read.txt", 'r')
    listUnique = []
    content = file.read()
    listMots = content.split()
    file.close()
    for mot in listMots:
        if mot not in listUnique:
            listUnique.append(mot)
        print("Voici la frequence d'apparition de : " + mot, listMots.count(mot))