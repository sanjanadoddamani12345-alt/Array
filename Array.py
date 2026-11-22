
def read_scores():
    scores = input("Enter scores separated by spaces: ")

    numbers = [float(x) for x in scores.split()]

    return numbers


def calculate_sum_average(scores):
    total = sum(scores)
    average = total / len(scores)

    print("Sum:", total)
    print("Average:", average)


def main():
    scores = read_scores()

    print("Scores:", scores)

    calculate_sum_average(scores)
if __name__ == "__main__":
    main()
