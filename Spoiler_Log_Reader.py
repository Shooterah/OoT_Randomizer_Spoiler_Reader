import json
import os

# Ce programme vas lire tous les spoilers log au format .json contenu dans le dossier Spoiler_logs
# Il vas enregistrer le nombre d'item majeure contenus dans chaque check (dans le noeuds "locations")

# La liste des items majeurs est dans la variable "items"
listeItems = ["Bomb Bag", "Rutos Letter", "Progressive Strength Upgrade", "Bow", "Lens of Truth", "Goron Tunic", "Magic Meter", "Slingshot", "Light Arrows", "Boomerang", "Progressive Hookshot", "Bottle with Milk", "Progressive Wallet", "Fire Arrows", "Iron Boots", "Hover Boots", "Progressive Scale", "Mirror Shield", "Megaton Hammer", "Dins Fire", "Claim Check", "Bottle with Red Potion", "Bottle with Green Potion", "Bottle with Blue Potion", "Bottle with Fairy", "Bottle with Fish", "Bottle with Blue Fire", "Bottle with Bugs", "Bottle with Poe", "Bottle with Big Poe", "Bottle"]

# La liste des locations est dans la variable "locations"
listeLocations = [
    "KF Midos Top Left Chest",
    "KF Midos Top Right Chest",
    "KF Midos Bottom Left Chest",
    "KF Midos Bottom Right Chest",
    "KF Kokiri Sword Chest",
    "KF Storms Grotto Chest",
    "LW Ocarina Memory Game",
    "LW Target in Woods",
    "LW Near Shortcuts Grotto Chest",
    "Deku Theater Skull Mask",
    "LW Skull Kid",
    "LW Deku Scrub Near Bridge",
    "LW Deku Scrub Grotto Front",
    "SFM Wolfos Grotto Chest",
    "HF Near Market Grotto Chest",
    "HF Tektite Grotto Freestanding PoH",
    "HF Southeast Grotto Chest",
    "HF Open Grotto Chest",
    "HF Deku Scrub Grotto",
    "Market Shooting Gallery Reward",
    "Market Bombchu Bowling First Prize",
    "Market Bombchu Bowling Second Prize",
    "Market Lost Dog",
    "Market Treasure Chest Game Reward",
    "Market 10 Big Poes",
    "ToT Light Arrows Cutscene",
    "HC Great Fairy Reward",
    "LLR Talons Chickens",
    "LLR Freestanding PoH",
    "Kak Anju as Child",
    "Kak Anju as Adult",
    "Kak Impas House Freestanding PoH",
    "Kak Windmill Freestanding PoH",
    "Kak Man on Roof",
    "Kak Open Grotto Chest",
    "Kak Redead Grotto Chest",
    "Kak Shooting Gallery Reward",
    "Kak 10 Gold Skulltula Reward",
    "Kak 20 Gold Skulltula Reward",
    "Kak 30 Gold Skulltula Reward",
    "Kak 40 Gold Skulltula Reward",
    "Kak 50 Gold Skulltula Reward",
    "Graveyard Shield Grave Chest",
    "Graveyard Heart Piece Grave Chest",
    "Graveyard Royal Familys Tomb Chest",
    "Graveyard Freestanding PoH",
    "Graveyard Dampe Gravedigging Tour",
    "Graveyard Dampe Race Hookshot Chest",
    "Graveyard Dampe Race Freestanding PoH",
    "DMT Freestanding PoH",
    "DMT Chest",
    "DMT Storms Grotto Chest",
    "DMT Great Fairy Reward",
    "DMT Biggoron",
    "GC Darunias Joy",
    "GC Pot Freestanding PoH",
    "GC Rolling Goron as Child",
    "GC Rolling Goron as Adult",
    "GC Maze Left Chest",
    "GC Maze Right Chest",
    "GC Maze Center Chest",
    "DMC Volcano Freestanding PoH",
    "DMC Wall Freestanding PoH",
    "DMC Upper Grotto Chest",
    "DMC Great Fairy Reward",
    "ZR Open Grotto Chest",
    "ZR Frogs in the Rain",
    "ZR Frogs Ocarina Game",
    "ZR Near Open Grotto Freestanding PoH",
    "ZR Near Domain Freestanding PoH",
    "ZD Diving Minigame",
    "ZD Chest",
    "ZD King Zora Thawed",
    "ZF Great Fairy Reward",
    "ZF Iceberg Freestanding PoH",
    "ZF Bottom Freestanding PoH",
    "LH Underwater Item",
    "LH Child Fishing",
    "LH Adult Fishing",
    "LH Lab Dive",
    "LH Freestanding PoH",
    "LH Sun",
    "GV Crate Freestanding PoH",
    "GV Waterfall Freestanding PoH",
    "GV Chest",
    "GF Chest",
    "GF HBA 1000 Points",
    "GF HBA 1500 Points",
    "Wasteland Chest",
    "Colossus Great Fairy Reward",
    "Colossus Freestanding PoH",
    "OGC Great Fairy Reward",
    "Deku Tree Map Chest",
    "Deku Tree Slingshot Room Side Chest",
    "Deku Tree Slingshot Chest",
    "Deku Tree Compass Chest",
    "Deku Tree Compass Room Side Chest",
    "Deku Tree Basement Chest",
    "Deku Tree Queen Gohma Heart",
    "Dodongos Cavern Map Chest",
    "Dodongos Cavern Compass Chest",
    "Dodongos Cavern Bomb Flower Platform Chest",
    "Dodongos Cavern Bomb Bag Chest",
    "Dodongos Cavern End of Bridge Chest",
    "Dodongos Cavern Boss Room Chest",
    "Dodongos Cavern King Dodongo Heart",
    "Jabu Jabus Belly Boomerang Chest",
    "Jabu Jabus Belly Map Chest",
    "Jabu Jabus Belly Compass Chest",
    "Jabu Jabus Belly Barinade Heart",
    "Bottom of the Well Front Left Fake Wall Chest",
    "Bottom of the Well Front Center Bombable Chest",
    "Bottom of the Well Back Left Bombable Chest",
    "Bottom of the Well Underwater Left Chest",
    "Bottom of the Well Freestanding Key",
    "Bottom of the Well Compass Chest",
    "Bottom of the Well Center Skulltula Chest",
    "Bottom of the Well Right Bottom Fake Wall Chest",
    "Bottom of the Well Fire Keese Chest",
    "Bottom of the Well Like Like Chest",
    "Bottom of the Well Map Chest",
    "Bottom of the Well Underwater Front Chest",
    "Bottom of the Well Invisible Chest",
    "Bottom of the Well Lens of Truth Chest",
    "Forest Temple First Room Chest",
    "Forest Temple First Stalfos Chest",
    "Forest Temple Raised Island Courtyard Chest",
    "Forest Temple Map Chest",
    "Forest Temple Well Chest",
    "Forest Temple Eye Switch Chest",
    "Forest Temple Boss Key Chest",
    "Forest Temple Floormaster Chest",
    "Forest Temple Red Poe Chest",
    "Forest Temple Bow Chest",
    "Forest Temple Blue Poe Chest",
    "Forest Temple Falling Ceiling Room Chest",
    "Forest Temple Basement Chest",
    "Forest Temple Phantom Ganon Heart",
    "Fire Temple Near Boss Chest",
    "Fire Temple Flare Dancer Chest",
    "Fire Temple Boss Key Chest",
    "Fire Temple Big Lava Room Lower Open Door Chest",
    "Fire Temple Big Lava Room Blocked Door Chest",
    "Fire Temple Boulder Maze Lower Chest",
    "Fire Temple Boulder Maze Side Room Chest",
    "Fire Temple Map Chest",
    "Fire Temple Boulder Maze Shortcut Chest",
    "Fire Temple Boulder Maze Upper Chest",
    "Fire Temple Scarecrow Chest",
    "Fire Temple Compass Chest",
    "Fire Temple Megaton Hammer Chest",
    "Fire Temple Highest Goron Chest",
    "Fire Temple Volvagia Heart",
    "Water Temple Compass Chest",
    "Water Temple Map Chest",
    "Water Temple Cracked Wall Chest",
    "Water Temple Torches Chest",
    "Water Temple Boss Key Chest",
    "Water Temple Central Pillar Chest",
    "Water Temple Central Bow Target Chest",
    "Water Temple Longshot Chest",
    "Water Temple River Chest",
    "Water Temple Dragon Chest",
    "Water Temple Morpha Heart",
    "Shadow Temple Map Chest",
    "Shadow Temple Hover Boots Chest",
    "Shadow Temple Compass Chest",
    "Shadow Temple Early Silver Rupee Chest",
    "Shadow Temple Invisible Blades Visible Chest",
    "Shadow Temple Invisible Blades Invisible Chest",
    "Shadow Temple Falling Spikes Lower Chest",
    "Shadow Temple Falling Spikes Upper Chest",
    "Shadow Temple Falling Spikes Switch Chest",
    "Shadow Temple Invisible Spikes Chest",
    "Shadow Temple Freestanding Key",
    "Shadow Temple Wind Hint Chest",
    "Shadow Temple After Wind Enemy Chest",
    "Shadow Temple After Wind Hidden Chest",
    "Shadow Temple Spike Walls Left Chest",
    "Shadow Temple Boss Key Chest",
    "Shadow Temple Invisible Floormaster Chest",
    "Shadow Temple Bongo Bongo Heart",
    "Spirit Temple Child Bridge Chest",
    "Spirit Temple Child Early Torches Chest",
    "Spirit Temple Child Climb North Chest",
    "Spirit Temple Child Climb East Chest",
    "Spirit Temple Map Chest",
    "Spirit Temple Sun Block Room Chest",
    "Spirit Temple Silver Gauntlets Chest",
    "Spirit Temple Compass Chest",
    "Spirit Temple Early Adult Right Chest",
    "Spirit Temple First Mirror Left Chest",
    "Spirit Temple First Mirror Right Chest",
    "Spirit Temple Statue Room Northeast Chest",
    "Spirit Temple Statue Room Hand Chest",
    "Spirit Temple Near Four Armos Chest",
    "Spirit Temple Hallway Right Invisible Chest",
    "Spirit Temple Hallway Left Invisible Chest",
    "Spirit Temple Mirror Shield Chest",
    "Spirit Temple Boss Key Chest",
    "Spirit Temple Topmost Chest",
    "Spirit Temple Twinrova Heart",
    "Ice Cavern Map Chest",
    "Ice Cavern Compass Chest",
    "Ice Cavern Iron Boots Chest",
    "Ice Cavern Freestanding PoH",
    "Gerudo Training Ground Lobby Left Chest",
    "Gerudo Training Ground Lobby Right Chest",
    "Gerudo Training Ground Stalfos Chest",
    "Gerudo Training Ground Before Heavy Block Chest",
    "Gerudo Training Ground Heavy Block First Chest",
    "Gerudo Training Ground Heavy Block Second Chest",
    "Gerudo Training Ground Heavy Block Third Chest",
    "Gerudo Training Ground Heavy Block Fourth Chest",
    "Gerudo Training Ground Eye Statue Chest",
    "Gerudo Training Ground Near Scarecrow Chest",
    "Gerudo Training Ground Hammer Room Clear Chest",
    "Gerudo Training Ground Hammer Room Switch Chest",
    "Gerudo Training Ground Freestanding Key",
    "Gerudo Training Ground Maze Right Central Chest",
    "Gerudo Training Ground Maze Right Side Chest",
    "Gerudo Training Ground Underwater Silver Rupee Chest",
    "Gerudo Training Ground Beamos Chest",
    "Gerudo Training Ground Hidden Ceiling Chest",
    "Gerudo Training Ground Maze Path First Chest",
    "Gerudo Training Ground Maze Path Second Chest",
    "Gerudo Training Ground Maze Path Third Chest",
    "Gerudo Training Ground Maze Path Final Chest",
    "Ganons Castle Forest Trial Chest",
    "Ganons Castle Water Trial Left Chest",
    "Ganons Castle Water Trial Right Chest",
    "Ganons Castle Shadow Trial Front Chest",
    "Ganons Castle Shadow Trial Golden Gauntlets Chest",
    "Ganons Castle Light Trial First Left Chest",
    "Ganons Castle Light Trial Second Left Chest",
    "Ganons Castle Light Trial Third Left Chest",
    "Ganons Castle Light Trial First Right Chest",
    "Ganons Castle Light Trial Second Right Chest",
    "Ganons Castle Light Trial Third Right Chest",
    "Ganons Castle Light Trial Invisible Enemies Chest",
    "Ganons Castle Light Trial Lullaby Chest",
    "Ganons Castle Spirit Trial Crystal Switch Chest",
    "Ganons Castle Spirit Trial Invisible Chest",
    "Ganons Tower Boss Key Chest"
]

listeZones = [
    "Ganons Castle",
    "Gerudo Training Ground",
    "Ice Cavern",
    "Spirit Temple",
    "Water Temple",
    "Shadow Temple",
    "Fire Temple",
    "Forest Temple",
    "Bottom of the Well",
    "Jabu Jabus Belly",
    "Dodongos Cavern",
    "Deku Tree",
    "OGC",
    "Wasteland",
    "GF",
    "GV",
    "LH",
    "ZF",
    "ZD",
    "ZR",
    "DMC",
    "DMT",
    "GC",
    "Graveyard",
    "Kak",
    "LLR",
    "HC",
    "ToT",
    "Market",
    "HF",
    "SFM",
    "LW",
    "KF",
]

# On trie par ordre alphabétique
listeItems.sort()
listeLocations.sort()
listeZones.sort()

# Classe qui vas contenir les items contenus dans une location de la façon suivante:
# - Nombre d'item majeur
# - Liste des items majeurs (Nom de l'item et nombre d'item)
class itemsInLocation:
    def __init__(self):
        # Nombre d'item majeur
        self.nbItems = 0
        # Liste des items majeurs (Nom de l'item et nombre d'item) pour tous les items dans la liste "listeItems"
        self.items = []
        for i in range(len(listeItems)):
            self.items.append([listeItems[i], 0])
            
# Classe qui vas contenir les items contenus dans une zone de la façon suivante:
# - Nombre d'item majeur
# - Liste des items majeurs (Nom de l'item et nombre d'item)
class itemsInZone:
    def __init__(self):
        # Nombre d'item majeur
        self.nbItems = 0
        # Liste des items majeurs (Nom de l'item et nombre d'item) pour tous les items dans la liste "listeItems"
        self.items = []
        for i in range(len(listeItems)):
            self.items.append([listeItems[i], 0])

# Liste des locations et des items qu'elles contiennent (Nom de la location et objet itemsInLocation)
listeLocationsItems = []
for i in range(len(listeLocations)):
    listeLocationsItems.append([listeLocations[i], itemsInLocation()])
    
# Liste des zones et des items qu'elles contiennent (Nom de la zone et objet itemsInZone)
listeZonesItems = []
for i in range(len(listeZones)):
    listeZonesItems.append([listeZones[i], itemsInZone()])

# Fonction qui permet de récupérer l'objet itemsInZone d'une zone
def getZoneItems(zone):
    for i in range(len(listeZonesItems)):
        if listeZonesItems[i][0] == zone:
            return listeZonesItems[i][1]
    return None
    
# Fonction qui permet de récupérer l'objet itemsInLocation d'une location
def getItemsInLocation(location):
    for i in range(len(listeLocationsItems)):
        if listeLocationsItems[i][0] == location:
            return listeLocationsItems[i][1]
    return None

# Fonction qui permet de récupérer l'objet itemsInLocation d'une zone

# Fonction qui vas lire les fichier .json du dossier "data", vas rechercher la section "locations" et vas mettre à jour la liste des locations et des items qu'elles contiennent
def getLocationsItems():
    nbFichierLus = 0
    # On récupère la liste des fichiers .json du dossier "data"
    files = os.listdir("Spoiler_logs")
    for file in files:
        nbFichierLus += 1
        print("Lecture du fichier " + str(nbFichierLus) + "/" + str(len(files)) + " : " + file)
        # On ouvre le fichier
        with open("Spoiler_logs/" + file, "r") as f:
            # On récupère le contenu du fichier
            data = json.load(f)
            # On récupère la section "locations"
            locations = data["locations"]
            # Pour chaque location
            for location in locations:
                # On regarde si la location est dans la liste des locations
                if location in listeLocations:
                    # On récupère la valeur de l'objet associé à la location dans le fichier .json
                    item = locations[location]
                    if type(item) is not str:
                        item = item["item"]
                    # Si l'item est un item majeur
                    if item in listeItems:
                        # On l'ajoute à la liste des locations et des items qu'elles contiennent
                        getItemsInLocation(location).items[listeItems.index(item)][1] += 1
                        # On incrémente le nombre d'item majeur de la location
                        getItemsInLocation(location).nbItems += 1
                        # Test pour les zone aux nom bizarre
                        if location == "Deku Theater Skull Mask":
                            # On ajoute l'item a  la liste des zones "LW"
                            getZoneItems("LW").items[listeItems.index(item)][1] += 1
                            # On incrémente le nombre d'item majeur de la zone "LW"
                            getZoneItems("LW").nbItems += 1
                        elif location == "Ganons Tower Boss Key Chest":
                            # On ajoute l'item a  la liste des zones "Ganons Castle"
                            getZoneItems("Ganons Castle").items[listeItems.index(item)][1] += 1
                            # On incrémente le nombre d'item majeur de la zone "Ganons Castle"
                            getZoneItems("Ganons Castle").nbItems += 1
                        # Ajouter l'item a la liste des zones a comme nom un morceau du nom de la location
                        for zone in listeZones:
                            # Si la location contient un morceau du nom de la zone
                            if zone in location:
                                # On ajoute l'item a  la liste des zones
                                getZoneItems(zone).items[listeItems.index(item)][1] += 1
                                # On incrémente le nombre d'item majeur de la zone
                                getZoneItems(zone).nbItems += 1
                                break
                            if location == "OGC Great Fairy Reward":
                                # On ajoute l'item a  la liste des zones "OGC"
                                getZoneItems("OGC").items[listeItems.index(item)][1] += 1
                                # On incrémente le nombre d'item majeur de la zone "OGC"
                                getZoneItems("OGC").nbItems += 1
                                break
                            


# Fonction qui affiche sous la forme d'un arbre a indentations les items contenus dans les locations avec le nombre d'item majeur
def printLocationsItems():
    for location in listeLocationsItems:
        # On affiche la location avec le nombre d'item majeur
        print(location[0] + " (" + str(location[1].nbItems) + ")")
        # On affiche les items de la location
        for item in location[1].items:
            # Si l'item est présent dans la location
            if item[1] > 0:
                # On affiche l'item
                print("\t" + item[0] + " (" + str(item[1]) + ")")
                
# Fonction qui affiche sous la forme d'un arbre a indentations les items contenus dans les zones avec le nombre d'item majeur
def printZonesItems():
    for zone in listeZonesItems:
        # On affiche la zone avec le nombre d'item majeur
        print(zone[0] + " (" + str(zone[1].nbItems) + ")")
        # On affiche les items de la zone
        for item in zone[1].items:
            # Si l'item est présent dans la zone
            if item[1] > 0:
                # On affiche l'item
                print("\t" + item[0] + " (" + str(item[1]) + ")")
                
# Fonction qui trie la liste des locations et des items qu'elles contiennent par nombre d'item majeur
def sortLocationsItems():
    listeLocationsItems.sort(key=lambda x: x[1].nbItems, reverse=True)

# Fonction qui trie la liste des zones et des items qu'elles contiennent par nombre d'item majeur
def sortZonesItems():
    listeZonesItems.sort(key=lambda x: x[1].nbItems, reverse=True)
    
# Fonction qui permet de sauvegarder les données de la liste des locations et des items qu'elles contiennent dans un fichier .json
def saveLocationsItems():
    # On ouvre le fichier
    with open("locationsItems.json", "w") as f:
        # Noeud racine (locations)
        root = {}
        # On ajoute les locations
        root["locations"] = []
        for location in listeLocationsItems:
            # On ajoute la location
            root["locations"].append({location[0]: []})
            # On ajoute le nombre d'item majeur
            root["locations"][-1][location[0]].append({"nbItems": location[1].nbItems})
            # On ajoute les items de la location dans un noeud "items"
            root["locations"][-1][location[0]].append({"items": []})
            for item in location[1].items:
                # On ajoute l'item
                root["locations"][-1][location[0]][1]["items"].append({item[0]: item[1]})
        # On sauvegarde le fichier
        json.dump(root, f, indent=4)
        
# Fonction qui permet de sauvegarder les données de la liste des zones et des items qu'elles contiennent dans un fichier .json
def saveZonesItems():
    # On ouvre le fichier
    with open("zonesItems.json", "w") as f:
        # Noeud racine (zones)
        root = {}
        # On ajoute les zones
        root["zones"] = []
        for zone in listeZonesItems:
            # On ajoute la zone
            root["zones"].append({zone[0]: []})
            # On ajoute le nombre d'item majeur
            root["zones"][-1][zone[0]].append({"nbItems": zone[1].nbItems})
            # On ajoute les items de la zone dans un noeud "items"
            root["zones"][-1][zone[0]].append({"items": []})
            for item in zone[1].items:
                # On ajoute l'item
                root["zones"][-1][zone[0]][1]["items"].append({item[0]: item[1]})
        # On sauvegarde le fichier
        json.dump(root, f, indent=4)

                
getLocationsItems()
sortLocationsItems()
sortZonesItems()

printLocationsItems()
printZonesItems()

saveLocationsItems()
saveZonesItems()
