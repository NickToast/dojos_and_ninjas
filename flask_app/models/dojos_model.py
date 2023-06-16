from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas_model

#Class is modeling the data from Dojo Table
class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = """
        SELECT *
        FROM dojos;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = [];
        for row in results:
            dojos.append(cls(row))
        print (dojos)
        return dojos
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(dojoname)s);
        """

        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT *
        FROM dojos
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    #import the cLass of ninja to join tables
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """
        SELECT * FROM dojos
        JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        one_dojo = cls(results[0])
        
        for row in results:
            ninja_data = {
                "id":  row['ninjas.id'],
                "first_name":  row['first_name'],
                "last_name":  row['last_name'],
                "age":  row['age'],
                "created_at":  row['ninjas.created_at'],
                "updated_at":  row['ninjas.updated_at'],
                "dojo_id": row['dojo_id']
            }
            one_dojo.ninjas.append(ninjas_model.Ninja(ninja_data))
            print(one_dojo)
        return one_dojo
    
