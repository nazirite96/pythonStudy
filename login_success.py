def solution(id_pw, db):
    answer = ''
    db_dict = {x[0]: x[1] for x in db}
    user_pw = db_dict.get(id_pw[0])
    if user_pw != None:
        if user_pw == id_pw[1]:
            return 'login'
        else:
            return 'wrong pw'
    else:
        return "fail"
    return answer


id_pw = ["meosseugi", "1234"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

print(solution(id_pw, db))
