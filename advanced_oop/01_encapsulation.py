"Encapsulation just means keeping our data and function that work on the data together, and hiding the internal details so no one messes with then directly"

""" Shows strict data protection using protected and private attributes. """

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance      # protected 
        self.__token = "secret123"   # private. (Python renames it internally so it can’t be accessed accidentally.)


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit")
        self._balance += amount

    def _log_access(self):
        """Protected helper method."""
        print("Access loged")

    def get_token(self):
        """ """
        self._log_access()
        return self.__token
    

acc = Account(owner='shinas', balance=500)


print(acc.owner)        #shinas

acc.deposit(200)
print(acc._balance)     #700 (we can access it, but you're not supposed to)

print(acc.get_token())  # "secret123"

# trying to access private variable directly (won’t work)
print(acc.__token)      #AttributeError

print(acc._)
