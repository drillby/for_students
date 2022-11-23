import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="dbs.spskladno.cz",
    user="student17",
    password="spsnet",
    database="vyuka17"
)
    mycursor = mydb.cursor()
except Exception as e:
    print(e)


mycursor.execute(
    """
    SELECT * FROM Auto;
    """
)

myres = mycursor.fetchall()

print(myres)
for idx, spz, znacka, max_rychlost, nahon in myres:
    print(f"Auto s ID {idx}, má spz {spz} a max rychlost {max_rychlost} km/h")

#mycursor.execute(
    """
    CREATE TABLE Emil (
        id int PRIMARY KEY AUTO_INCREMENT,
        rychlost int,
        jmeno varchar(25)
    )
    """
#)
#mydb.commit()

mycursor.execute(
    """
    INSERT INTO Emil (rychlost, jmeno)
    VALUES
    (31, "Mojmír"),
    (50, "Luboš")
    """
)
mydb.commit()

mycursor.close()
mydb.close()