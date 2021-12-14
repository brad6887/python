def read_cows(input_file, num_cows):
    """[summary]
    input_file is a file open for reading; cow information is next to read.
    num_cows is the number of cows in the file.

    Read teh cows' favorite pastures from the input_file.
    return a listof lists of each cow's favorite 2 pastures;
    each value in the list is a slist of two values giving the 
    favorite pastures of one cow.


    """
    favorites = []
    for i in range(num_cows):
        lst = input_file.readline().split()
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        favorites.append(lst)
    return favorites


def cows_with_favorite(favorites, pasture):
    """
    favorites is a list of favorite pastures, as returned by read_cows.
    pasture is a number.

    Return list of cows that care about that pasture.
    """
    cows = []
    for i in range(len(favorites)):
        if favorites[i][0] == pasture or favorites[i][1] == pasture:
            cows.append(i)
    return cows


def types_used(favorites, cows, pasture_types):
    """ 
    favorites is a list of favorite pastures, as returned by read_cows.
    cows is a list of cows.
    pasture_types is a list of grass types.
    
    Return a list of the gras types already used by cows.
    """
    used = []
    for cow in cows:
        pasture_a = favorites[cow][0]
        pasture_b = favorites[cow][1]
        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used


def smallest_available(used):
    """ 
    used is a list of used grass types.
    
    Return the smallest-numbered grass type that is not used.
    """
    grass_type = 1
    while grass_type in used:
        grass_type = grass_type + 1
    return grass_type


def write_pastures(output_file, pasture_types):
    """ 
    output file is a file open for writing.
    pasture_types is a list of integer grass types.
    
    Output pasture_types to an output file
    """
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)
    output_file.write(output + '\n')

# Main Program

input_file = open('revegetate.in', 'r')
output_file = open('revegeate.out', 'w')


# Read input
lst = input_file.readline().split()
num_pastures = int(lst[0])
num_cows = int(lst[1])
favorites = read_cows(input_file, num_cows)

pasture_types = [0]
for i in range(1, num_pastures + 1):
    
    # Identify cows that care about pasture
    cows = cows_with_favorite(favorites, i)

    # Eliminale grass types for pasture
    eliminated = types_used(favorites, cows, pasture_types)

    #Choose smallest-numbered grass type for pasture
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

# write ouptut
pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()