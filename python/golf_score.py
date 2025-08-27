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


def judge_score(par, strokes):
    print("\n各コースの成績:")
    score = []
    for par, stroke in zip(par, strokes):
        if par == 5 and stroke == 1:
            score.append('コンドル')
            continue

        elif par == 5 and stroke == 2:
            score.append('アルバトロス')
            continue

        elif par == 4 and stroke == 1 or stroke == 1:
            score.append('ホールインワン')
            continue

        calculate_par_difference = (par - stroke) * -1

        if calculate_par_difference == 0:
            score.append('パー')

        elif calculate_par_difference == -1:
            score.append('バーディ')

        elif calculate_par_difference == -2:
            score.append('イーグル')

        elif calculate_par_difference == 1:
            score.append('ボギー')

        elif calculate_par_difference == 2:
            score.append('2ボギー')

        elif calculate_par_difference >= 3:
            num = calculate_par_difference
            score.append(f"{num}ボギー")
    print(','.join(score))


judge_score(course_par, player_strokes)
