def add_triathlon_data(entry: str, records: dict):
    """Parse entry as one line of csv and insert it into records.
    
    The input string is a series of fields separated by a comma, 
    with the following order:
        Athlete's name
        Swim split time in seconds
        Bike split time in seconds
        Run split time in seconds
    The input dictionary has the following format:
        the data structure is a dictionary where the keys are athlete's names and the values are
        dictionaries containing the split times for that athlete.
        the dictionary containing the split times has the category's name for keys 
        (that is 'swim', 'bike', and 'run'),
        and the recorded time for that category as mapped values.
        for example
        {
            'Javier Gomez': {
                'run': 1756, 'swim': 1020, 'bike': 3556,
            },
            'Laurent Vidal': {'run': 1801, ...,},
        }
    The method returns True if the entry has been added successfully, False otherwise.
    An entry cannot be added successfully if:
        The name of the athlete already exists in record.
        The number of elements in the entry is not equal to 4.
        The time values are not int.
    """
    entry_fields_len_check = 4

    # split the fields and strip spaces
    entry_fields = [f.strip() for f in entry.split(',')]
    # check if entry is valid
    if len(entry_fields) != entry_fields_len_check:
        return False

    name = entry_fields[0]
    if name in records:
        return False

    try:
        split_swim = int(entry_fields[1])
        split_bike = int(entry_fields[2])
        split_run = int(entry_fields[3])
    except ValueError:
        return False

    # add entry
    records[name] = {
        'swim': split_swim,
        'bike': split_bike,
        'run': split_run,
    }
    return True
