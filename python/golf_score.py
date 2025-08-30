file = 'case_1.txt'
with open(file) as file_data:
    print("各コースの規定打数:")
    line = file_data.readline()
    course_par = [int(x) for x in line.split(',')]
    print(course_par)

    print("\n各コースのプレイヤーの打数:")
    line2 = file_data.readline()
    player_strokes = [int(x) for x in line2.split(',')]
    print(player_strokes)
    
    SCORE_MAPPING = {
    -4: "コンドル",
    -3: "アルバトロス",
    -2: "イーグル",
    -1: "バーディ",
    0: "パー",
    1: "ボギー",
    }


def judge_score(par, strokes):
    
    print("\n各コースの成績:")
    score = []
    for par, stroke in zip(par, strokes):
        
        result = stroke - par

        if par == 4 and stroke == 1 or not par == 5 and stroke == 1:
            score.append('ホールインワン')
            continue

        elif result >= 2:
            num = result
            score.append(f"{num}ボギー")
            continue

        score.append(SCORE_MAPPING[result])
        
    print(','.join(score))


judge_score(course_par, player_strokes)
