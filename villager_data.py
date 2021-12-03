"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    with open(filename) as file:
      data = [line.split("|") for line in file.readlines()]
      species = {line[1] for line in data}
    return species


def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[list]: a list of lists
    """
    with open(filename) as file:
      data = [line.split("|") for line in file.readlines()]
      villagers = [line[0] for line in data if line[1] == species or species == 'All']
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    hobbies = ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    with open(filename) as file:
      groups = []
      data = [line.split("|") for line in file.readlines()]
      for hobby in hobbies:
        names = [hobby] + [line[0] for line in data if line[3] == hobby]
        groups.append(names)
    return groups
    
    # One-liner solution
    # return [[hobby] + [line[0] for line in data if line[3] == hobby] for hobby in hobbies]
    #
    # (We decided to add the hobby name to the beginning of each list!)


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    with open(filename) as file:
      data = [line.strip().split("|") for line in file.readlines()]
      return [tuple(line) for line in data]


def find_motto(filename, name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    with open(filename) as file:
      data = [line.strip().split("|") for line in file.readlines()]
      for line in data:
        if line[0] == name:
          return line[4]


def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""
    with open(filename) as file:
      data = [line.strip().split("|") for line in file.readlines()]
      for line in data:
        if line[0] == name:
          personality = line[2]
          break
    return {line[0] for line in data if line[2] == personality}


# PASSED: TEST 1 
# print(all_species('villagers.csv'))

# PASSED: TEST 2 
# print(get_villagers_by_species('villagers.csv', species="Monkey"))
# print(get_villagers_by_species('villagers.csv', species="All"))

# PASSED: TEST 3
# print(all_names_by_hobby('villagers.csv'))

# PASSED: TEST 4
# print(all_data('villagers.csv'))

# PASSED: TEST 5
# print(find_motto('villagers.csv', "Anchovy"))
# print(find_motto('villagers.csv', "aisdfoashd"))

# PASSED TEST 6:
# print(find_likeminded_villagers('villagers.csv', 'Poppy'))
# print(find_likeminded_villagers('villagers.csv', 'Midge'))