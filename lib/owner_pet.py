class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []  # Class variable to store all pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Validate pet_type
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type '{self.pet_type}'. Must be one of {Pet.PET_TYPES}.")
        
        # Add to the list of all pets
        Pet.all.append(self)
        
        # If an owner is provided, add the pet to the owner's list of pets
        if self.owner:
            if not isinstance(self.owner, Owner):
                raise Exception("owner must be an instance of Owner")
            self.owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []  # List to store pets of this owner

    def pets(self):
        # Return the list of pets for the owner
        return self.pets_list

    def add_pet(self, pet):
        # Check that pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        
        # Add the pet to the owner's pet list if it isn't already added
        if pet not in self.pets_list:
            self.pets_list.append(pet)
            pet.owner = self  # Set the owner for the pet

    def get_sorted_pets(self):
        # Return a sorted list of pets by their names
        return sorted(self.pets_list, key=lambda pet: pet.name)

# Example usage
try:
    # Create owners
    owner1 = Owner("Alice")
    owner2 = Owner("Bob")

    # Create pets and associate them with owners
    pet1 = Pet("Buddy", "dog", owner1)
    pet2 = Pet("Milo", "cat", owner1)
    pet3 = Pet("Luna", "bird", owner2)

    # Add pets manually
    owner2.add_pet(pet1)

    # Get sorted pets of Alice
    print("Alice's sorted pets:", [pet.name for pet in owner1.get_sorted_pets()])
    
    # Get all pets of Bob
    print("Bob's pets:", [pet.name for pet in owner2.pets()])
except Exception as e:
    print(e)
