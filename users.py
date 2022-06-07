# import the functions that will return an instance of a connection
from mysqlconnection import connectToMySQL


#model the class after the users table from database
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#use class method to query database
#call the connectToMySQL function with the targeting schema
#create an empty list to append the instances
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_schema.users;"
        result = connectToMySQL('users_schema').query_db(query)
        all_users = []
        for one_user in result:
            all_users.append(cls(one_user))
        return all_users


#class method to save all the users to the database
#return row number(ID) of the database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users_schema.users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW());"
        result = connectToMySQL('users_schema').query_db(query,data)
        print(result)
        return result
        # return connectToMySQL('users_schema').query_db(query,data)

#class method to show individual user to the database
#return instance of the user object of the row number(ID)
    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM users_schema.users WHERE id =%(id)s;"
        result = connectToMySQL('users_schema').query_db(query,data)
        print(result)
        return cls(result[0])

#class method to update the users to the database
    @classmethod
    def update(cls,data):
        query ="UPDATE users_schema.users SET first_name = %(fname)s, last_name= %(lname)s, email=%(email)s, updated_at=Now() WHERE id = %(id)s;"
        print(query)
        result = connectToMySQL('users_schema').query_db(query,data)
        print(result)
        return result

#class method to delete the users to the database
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users_schema.users WHERE id =%(id)s; "
        return connectToMySQL('users_schema').query_db(query,data)