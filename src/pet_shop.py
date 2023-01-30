# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop): 
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, money):
    pet_shop["admin"]["total_cash"] += money


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, pets_sold):
   pet_shop["admin"]["pets_sold"] += pets_sold


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
    

def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)

    return found_pets


def find_pet_by_name(pet_shop, name):
   for pet_name in pet_shop["pets"]:
        if pet_name["name"] == name:
            return pet_name
    

# def remove_pet_by_name(pet_shop, name):
    # pet = find_pet_by_name(pet_shop, name)
    # pet_shop["name"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    
    
def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    

def get_customer_pet_count(customer):
    if customer["pets"] == []:
        return 0
    else:
        return len(customer["pets"])
         
            
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    

# what is the function called?
# what parameters does it need?
# what does the function need to return?
# what does the function need to do?

# --- OPTIONAL section ---

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    elif customer["cash"] < new_pet["price"]:
        return False 


# Integration tests section 

# def sell_pet_to_customer(pet_shop, pet, customer):

    # updating pet count of the customer 
    # updating pets sold of the pet store 
    # getting customers cash
    # updating/getting the total cash of the pet store
