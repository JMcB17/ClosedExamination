def add_triathlon_data(entry: str, records: dict):
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
