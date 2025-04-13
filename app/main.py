lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

# write your code here
def create_dictionary(*args):
    allowed_types = (int, float, str, bool, type(None), list, tuple, set, dict)
    result = {}
    
    for position, argument in enumerate(args):
        if isinstance(argument, allowed_types) or callable(argument):
            if isinstance(argument, (list, set, dict)):
                # Lists, sets, and dicts are not hashable, can't be used as keys
                print(f"Cannot add {argument} to the dict!")
            else:
                # Add the argument as a key and its position as the value
                result[argument] = position
        else:
            # Not an allowed type or function
            print(f"Cannot add {argument} to the dict!")

    return result