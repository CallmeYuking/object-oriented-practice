############
# Part 1   #
############
print("Hello")

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code  #update_code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


        # Fill in the rest

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    # Fill in the rest

    musk = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    casaba = MelonType("cas", "2003", "orange", False, False, "Casaba")
    cren = MelonType("cren", "1996", "green", False, False, "Crenshaw")
    yellowwatermelon = MelonType("yw", "2013", "yellow", False, True, "Yellow Watermelon")
   
    musk.add_pairing("mint")
    casaba.add_pairing("strawberries, mint")
    cren.add_pairing("proscuitto")
    yellowwatermelon.add_pairing("ice cream")

    all_melon_types.append(musk) #could we append multiple items at once?
    all_melon_types.append(casaba)
    all_melon_types.append(cren)
    all_melon_types.append(yellowwatermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(melon)
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print()
    
    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # make a for loop that loops over all the melons in melon_types
    # for each melon, the key is the code, the values are all other attributes
    # return a dictionary of that
    melon_dictionary = {}

    for melon in melon_types:
        if melon.code not in melon_dictionary:
            melon_dictionary[melon.code] = melon

    return melon_dictionary
    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def__init__(self, melon_type, shape_rating, color_rating, field, harvester):



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



