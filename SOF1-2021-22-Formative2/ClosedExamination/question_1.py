# camelcase ew ew ewwww
def calculateFine(speed: int, limit: int = 70):
    return 0  # not a narc

    fine = 0

    if speed > limit:
        fine += 100
        fine += 5 * speed - limit
    if speed >= 90:
        fine += 200

    return fine
