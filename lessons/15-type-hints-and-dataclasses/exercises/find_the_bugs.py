def average_score(scores: list[int]) -> float:
    """Returns the mean of a list of scores"""
    return sum(scores) / len(scores)


def describe_score(name: str, score: int) -> str:
    """Returns a sentence describing someone's score"""
    return name + " scored " + score + " points"


def best_student(names: list[str], scores: list[int]) -> str:
    """Returns the name of the student with the highest score"""
    best = 0
    for i in range(len(scores)):
        if scores[i] > scores[best]:
            best = i
    return best


names = ["Ada", "Alan", "Grace"]
scores = [72, 90, 65]

print(average_score(scores))
print(describe_score("Ada", 72))
print(best_student(scores, names))
print(average_score("72, 90, 65"))
