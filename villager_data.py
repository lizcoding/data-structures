"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    with open(filename) as file:
      data = file.readlines()
      species = set()
      for line in data:
        line = line.split("|")
        species.add(line[1])

    return species


def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[list]: a list of lists
    """
    # TODO: turn into list comprehension
    with open(filename) as file:
      data = file.readlines()
      villagers = []
      for line in data:
        line = line.split('|') 
        if species == "All" or line[1] == species:
          villagers.append(line[0])
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    hobbies = ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    groups = []
    with open(filename) as file:
      data = file.readlines()
      for hobby in hobbies:
        names = []
        for line in data:
          line = line.split("|")
          if line[3] == hobby:
            names.append(line[0])
        groups.append(names)       
    return groups


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
      data = file.readlines()
      entries = [tuple(line.strip().split("|")) for line in data]   
    return entries


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
      data = file.readlines()

      for line in data:
        line = line.strip().split("|")
        if line[0] == name:
          return line[4]


def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""
    with open(filename) as file:
      data = file.readlines()

      for line in data:
        line = line.strip().split("|")
        if line[0] == name:
          personality = line[2]
          break

      group = set()
      for line in data:
        line = line.strip().split("|")
        if line[2] == personality:
          group.add(line[0])
    return group


# PASSED: TEST 1 
# print(all_species('villagers.csv'))
# PASSED: TEST 2 
# print(get_villagers_by_species('villagers.csv', species="Monkey"))
# print(get_villagers_by_species('villagers.csv', species="All"))

# PASSED: TEST 3
#print()
# print(all_names_by_hobby('villagers.csv'))

# PASSED: TEST 4
# print(all_data('villagers.csv'))

# PASSED: TEST 5
# print(find_motto('villagers.csv', "Anchovy"))
# print(find_motto('villagers.csv', "aisdfoashd"))

# PASSED:
# print(find_likeminded_villagers('villagers.csv', 'Poppy'))
# print(find_likeminded_villagers('villagers.csv', 'Midge'))