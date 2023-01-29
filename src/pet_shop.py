# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop): 
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, money):
    if money > 0:
        pet_shop["admin"]["total_cash"] += money
     

# def missing here 

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, pets_sold):
   pet_shop["admin"]["pets_sold"] += pets_sold


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    

# what is the function called?
# what parameters does it need?
# what does the function need to return?
# what does the function need to do?



