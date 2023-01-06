def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        temp = list(skill)

        for i in skills:
            if i in temp:
                if i != temp.pop(0):
                    break

        else:
            answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))