class service:
    
    def __init__(self, authorized, entity_id):
        self.entity_id = entity_id
    
    def get_money(self):
        # fetch account based on entity_id (based on current model)
        # return money associated with that account_id (implied entity_id)

        # eventually we will also want to track when a user inspects their balance
        return None

    def deposit(self, amount):
        # fetch account based on entity_id (based on current model)
        # we then transact with that account to deposit the money into that account_id
        #           ^--- We also need to append to the transaction table for this

        # return the total after the transaction is made
        return None
    
    def withdraw(self, amount):
        # fetch account based on entity_id (based on current model)
        # we then transact with that account to withdraw the money into that account_id
        #           ^--- We also need to append to the transaction table for this

        # return the total after the transaction is made
        return None

    def transfer(self, amount, account_id):
        # fetch account based on entity_id (based on current model)
        # we transact to subtract from invokers account_id
        # we trasnact to add to requestors account_id

        # return the total after the transaction is made
        return None

    def whats_wrong(self):
	# Ask Martin what's wrong
        print("Doshita Martin-san")
