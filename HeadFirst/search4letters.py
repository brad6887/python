def search4vowels(phrase:str) -> set:
    """ Display any vowels found in an asked-for prase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))