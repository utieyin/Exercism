"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    new_scores = [round(scores) for scores in student_scores]
    return new_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    scores_list = [scores for scores in student_scores if scores <= 40]
    return len(scores_list)


count_failed_students(student_scores=[90, 40, 55, 70, 30, 25, 80, 95, 38, 40])


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    higher_students = [scores for scores in student_scores if scores >= threshold]
    return higher_students


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    diff = (highest - 40) // 4
    highest_list = [41]
    count = 0
    while count < 3:
        highest_list.append(highest_list[count] + diff)
        count += 1

    return highest_list


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    matching_result = []
    for index, students in enumerate(student_names):
        score = f"{index+1}. {students}: {student_scores[index]}"
        matching_result.append(score)
    return matching_result


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    perfect_s = [info for info in student_info if 100 in info]
    return perfect_s[0] if perfect_s else []
