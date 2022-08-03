import sqlite3


class Personne:
    def __init__(self):
        self.nom = "a",
        self.prenom = "b"
        self.age = "0"

    def getConnection(self):
        try:

            cnx = sqlite3.connect('presonne.db')
            return cnx

        except Exception as e:
            return e

    def createTable(self, cnx):

        # cnx.execute("DROP TABLE personne")
        cnx.execute("CREATE TABLE personne(""id INT AUTO_INCREMENT PRIMARY KEY NOT NULL  ,""nom VARCHAR(50),""age INT)")

        cnx.close()

        def insertData(self,cnx,pers):
            cnx.execute("INSERT INTO personne VALUES(""{},{}}))".format(['nom'],pers['age']))

            cnx.commit()
            cnx.close()



pers1 = Personne()
cnx = pers1.getConnection()
#creat table personn1

nom = input("Entrer un nom:")
age = int(input("Entrer age:"))
#pers1.createTable(cnx)
persona ={"nom": nom,"age":age}
