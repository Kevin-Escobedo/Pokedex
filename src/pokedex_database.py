import sqlite3

if __name__ == "__main__": #Clean up and make functions for this later
    db = sqlite3.connect("pokedex.db")
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE pokemon(num INTEGER PRIMARY KEY, name TEXT,
    types TEXT, stats TEXT)
    ''')

    db.commit()

    num = 1

    file = open("pokedex.txt", "r")
    for line in file:
        line = line.split("\t")
        info = []
        for item in line:
            item = item.strip()
            if item != "":
                info.append(item)
        name = info[0]
        type_temp = info[1].split("/")
        temp = info[2].split("/")

        stats = "{}/{}/{}/{}/{}/{}".format(temp[0],
                temp[1], temp[2], temp[3], temp[4],
                temp[5])

        if len(type_temp) == 2:
            types = "{}/{}".format(type_temp[0], type_temp[1])

        else:
            types = type_temp[0]

        cursor.execute('''INSERT INTO pokemon(num, name, types, stats)
        VALUES(?, ?, ?, ?)''', (num, name, types, stats))

        num += 1

        db.commit()

    file.close()


