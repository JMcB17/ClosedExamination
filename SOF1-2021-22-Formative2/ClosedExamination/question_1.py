# camelcase ew ew ewwww
def calculateFine(speed: int, limit: int = 70) -> int:
    fine = 0

    if speed > limit:
        fine += 100
        fine += 5 * (speed - limit)
    if speed >= 90:
        fine += 200

    return fine


if __name__ == '__main__':
    print(calculateFine(60, 60))
    print(calculateFine(90, 70))
    print(calculateFine(70, 70))
