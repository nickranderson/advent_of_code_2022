# -*- coding: utf-8 -*-
strategy_guide_file = open("C:/Users/Nick Anderson/Desktop/input.txt",)
strategy_guide_list = strategy_guide_file.readlines()
my_score = 0
battle_result = 0
#    A is rock, B is paper, C is scissors
#    X is rock, Y is paper, Z is scissors
win_dict = {"A":"Y","B":"Z","C":"X"}
lose_dict = {"A":"Z","B":"X","C":"Y"}
point_dict = {"X":1,"Y":2,"Z":3}

for ii in range(len(strategy_guide_list)):
    current_battle = strategy_guide_list[ii].rstrip()

    [opponent_move,my_move] = current_battle.split(" ")
    if my_move == win_dict[opponent_move]:
        my_score = my_score + 6 + point_dict[my_move]
    elif my_move == lose_dict[opponent_move]:
        my_score = my_score + 0 + point_dict[my_move]
    else:
        my_score = my_score + 3 + point_dict[my_move]    
    
print("Assuming move: ",my_score)
#   X is lose, Y is draw, Z is win
result_dict = {"X":1,"Y":2,"Z":3}
draw_dict = {"A":"X","B":"Y","C":"Z"}
my_score = 0
for ii in range(len(strategy_guide_list)):
    current_battle = strategy_guide_list[ii].rstrip()
    [opponent_move,needed_result] = current_battle.split(" ")
    if result_dict[needed_result] == 1:
        my_score = my_score + 0 + point_dict[lose_dict[opponent_move]]
    elif result_dict[needed_result] == 2:
        my_score = my_score + 3 + point_dict[draw_dict[opponent_move]]
    if result_dict[needed_result] == 3:
        my_score = my_score + 6 + point_dict[win_dict[opponent_move]]

print("Assuming result ",my_score)
strategy_guide_file.close()