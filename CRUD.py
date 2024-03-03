from pymongo import MongoClient

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB """

    def __init__(self, user_name, password):
        # initializing the MongoClient. This helps to
        # access the MongoDB databses and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        # 
        # Connection Variables 
        #
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize connection
        #
        self.client = MongoClient(f'mongodb://{user_name}:{password}@nv-desktop-services.apporto.com:31962/?directConnection=true&appName=mongosh+1.8.0')
        self.database = self.client['%s' %(DB)]
        self.collection = self.database['%s' % (COL)]

        # Complete this create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data) #data should be dictionary

        else:
            raise Exception("Nothing to save becase data parameter is empty")

    # Create method to implement the R un CRUD.
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria, {"_id": False})
        else: 
            data = self.database.animals.find({},{"_id": False})
            
        return data
            
    
    def update(self, query, data):
        if data is not None:
            return self.database.animals.update_one(query, data)
        else:
            raise Exception("Could not update document")
        
    def delete(self, data):
        if data is not None:
            self.database.animals.delete_one(data)
        else:
            raise Exception("Could not delete document")

