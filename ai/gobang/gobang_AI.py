from graphics import *
from math import *
import numpy as np


def ai():
    """
    AI计算落子位置
    """
    maxmin(True, DEPTH, -99999999, 99999999)
    return next_point[0], next_point[1]


def maxmin(is_ai, depth, alpha, beta):
    """
    负值极大算法搜索 alpha + beta剪枝
    """
    # 游戏是否结束 | | 探索的递归深度是否到边界
    if game_win(list1) or game_win(list2) or depth == 0:
        return evaluation(is_ai)

    blank_list = list(set(list_all).difference(set(list3)))
    order(blank_list)  # 搜索顺序排序  提高剪枝效率
    # 遍历每一个候选步
    for next_step in blank_list[0:60]:

        # 如果要评估的位置没有相邻的子， 则不去评估  减少计算
        if not has_neightnor(next_step):
            continue

        if is_ai:
            list1.append(next_step)
        else:
            list2.append(next_step)
        list3.append(next_step)

        value = -maxmin(not is_ai, depth - 1, -beta, -alpha)
        if is_ai:
            list1.remove(next_step)
        else:
            list2.remove(next_step)
        list3.remove(next_step)

        if value > alpha:
            if depth == DEPTH:
                next_point[0] = next_step[0]
                next_point[1] = next_step[1]
            # alpha + beta剪枝点
            if value >= beta:
                return beta
            alpha = value
    return alpha


def order(blank_list):
    """
    离最后落子的邻居位置最有可能是最优点

    计算最后落子点的8个方向邻居节点
    若未落子，则插入到blank列表的最前端

    :param blank_list: 未落子节点集合
    :return: blank_list
    """
    last_pt = list3[-1]
    # for item in blank_list:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (last_pt[0] + i, last_pt[1] + j) in blank_list:
                blank_list.remove((last_pt[0] + i, last_pt[1] + j))
                blank_list.insert(0, (last_pt[0] + i, last_pt[1] + j))


def has_neightnor(pt):
    """
    判断是否有邻居节点
    :param pt: 待评测节点
    :return:
    """
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (pt[0] + i, pt[1] + j) in list3:
                return True
    return False


def evaluation(is_ai):
    """
    评估函数
    """
    if is_ai:
        my_list = list1
        enemy_list = list2
    else:
        my_list = list2
        enemy_list = list1
    # 算自己的得分
    score_all_arr = []  # 得分形状的位置 用于计算如果有相交 得分翻倍
    my_score = 0
    for pt in my_list:
        m = pt[0]
        n = pt[1]
        my_score += cal_score(m, n, 0, 1, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, 1, 0, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, 1, 1, enemy_list, my_list, score_all_arr)
        my_score += cal_score(m, n, -1, 1, enemy_list, my_list, score_all_arr)
    #  算敌人的得分， 并减去
    score_all_arr_enemy = []
    enemy_score = 0
    for pt in enemy_list:
        m = pt[0]
        n = pt[1]
        enemy_score += cal_score(m, n, 0, 1, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, 1, 0, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, 1, 1, my_list, enemy_list, score_all_arr_enemy)
        enemy_score += cal_score(m, n, -1, 1, my_list, enemy_list, score_all_arr_enemy)

    total_score = my_score - enemy_score * 0.1
    return total_score


def cal_score(m, n, x_decrict, y_derice, enemy_list, my_list, score_all_arr):
    """
    每个方向上的分值计算
    :param m:
    :param n:
    :param x_decrict:
    :param y_derice:
    :param enemy_list:
    :param my_list:
    :param score_all_arr:
    :return:
    """
    add_score = 0  # 加分项
    # 在一个方向上， 只取最大的得分项
    max_score_shape = (0, None)

    # 如果此方向上，该点已经有得分形状，不重复计算
    for item in score_all_arr:
        for pt in item[1]:
            if m == pt[0] and n == pt[1] and x_decrict == item[2][0] and y_derice == item[2][1]:
                return 0

    # 在落子点 左右方向上循环查找得分形状
    for offset in range(-5, 1):
        # offset = -2
        pos = []
        for i in range(0, 6):
            if (m + (i + offset) * x_decrict, n + (i + offset) * y_derice) in enemy_list:
                pos.append(2)
            elif (m + (i + offset) * x_decrict, n + (i + offset) * y_derice) in my_list:
                pos.append(1)
            else:
                pos.append(0)
        tmp_shap5 = (pos[0], pos[1], pos[2], pos[3], pos[4])
        tmp_shap6 = (pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

        for (score, shape) in shape_score:
            if tmp_shap5 == shape or tmp_shap6 == shape:
                if score > max_score_shape[0]:
                    max_score_shape = (score, ((m + (0 + offset) * x_decrict, n + (0 + offset) * y_derice),
                                               (m + (1 + offset) * x_decrict, n + (1 + offset) * y_derice),
                                               (m + (2 + offset) * x_decrict, n + (2 + offset) * y_derice),
                                               (m + (3 + offset) * x_decrict, n + (3 + offset) * y_derice),
                                               (m + (4 + offset) * x_decrict, n + (4 + offset) * y_derice)),
                                       (x_decrict, y_derice))

    # 计算两个形状相交， 如两个3活 相交， 得分增加 一个子的除外
    if max_score_shape[1] is not None:
        for item in score_all_arr:
            for pt1 in item[1]:
                for pt2 in max_score_shape[1]:
                    if pt1 == pt2 and max_score_shape[0] > 10 and item[0] > 10:
                        add_score += item[0] + max_score_shape[0]

        score_all_arr.append(max_score_shape)

    return add_score + max_score_shape[0]


def game_win(list):
    """
    胜利条件判断
    """
    # for m in range(COLUMN):
    #     for n in range(ROW):
    #         if n < ROW - 4 and (m, n) in list and (m, n + 1) in list and (m, n + 2) in list and (
    #                 m, n + 3) in list and (m, n + 4) in list:
    #             return True
    #         elif m < ROW - 4 and (m, n) in list and (m + 1, n) in list and (m + 2, n) in list and (
    #                 m + 3, n) in list and (m + 4, n) in list:
    #             return True
    #         elif m < ROW - 4 and n < ROW - 4 and (m, n) in list and (m + 1, n + 1) in list and (
    #                 m + 2, n + 2) in list and (m + 3, n + 3) in list and (m + 4, n + 4) in list:
    #             return True
    #         elif m < ROW - 4 and n > 3 and (m, n) in list and (m + 1, n - 1) in list and (
    #                 m + 2, n - 2) in list and (m + 3, n - 3) in list and (m + 4, n - 4) in list:
    #             return True
    return False


def draw_window():
    """
    绘制棋盘
    """
    # 绘制画板
    win = GraphWin("五子棋", GRAPH_HEIGHT, GRAPH_WIDTH)
    win.setBackground("gray")
    # 绘制列
    i1 = 0
    while i1 <= GRID_WIDTH * COLUMN:
        i1 = i1 + GRID_WIDTH
        l = Line(Point(i1, GRID_WIDTH), Point(i1, GRID_WIDTH * COLUMN))
        l.draw(win)
    # 绘制行
    i2 = 0
    while i2 <= GRID_WIDTH * ROW:
        i2 = i2 + GRID_WIDTH
        l = Line(Point(GRID_WIDTH, i2), Point(GRID_WIDTH * ROW, i2))
        l.draw(win)
    return win


def main():
    """
    程序循环
    :return:
    """
    mode = int(input("先手 AI先手 ? 1 0 \n"))
    # 绘制棋盘
    win = draw_window()
    # 添加棋盘所有点
    for i in range(COLUMN + 1):
        for j in range(ROW + 1):
            list_all.append((i, j))
    # 循环条件
    g = 0
    change = 0
    # 开始循环
    while g == 0:
        # AI
        if change % 2 == mode:
            # AI先手 走天元
            if change == 0:
                pos = (6, 6)
            else:
                pos = ai()
            # 添加落子
            list1.append(pos)
            list3.append(pos)
            # 绘制白棋
            piece = Circle(Point(GRID_WIDTH * (pos[0]), GRID_WIDTH * (pos[1])), 12)
            piece.setFill('white')
            piece.draw(win)
            # AI胜利
            if game_win(list1):
                message = Text(Point(GRAPH_WIDTH / 2, GRID_WIDTH / 2), "AI获胜")
                message.draw(win)
                g = 1
            change = change + 1

        # User
        else:
            p2 = win.getMouse()
            x = round((p2.getX()) / GRID_WIDTH)
            y = round((p2.getY()) / GRID_WIDTH)

            # 若点未被选取过
            if not (x, y) in list3:
                # 添加落子
                list2.append((x, y))
                list3.append((x, y))
                # 绘制黑棋
                piece = Circle(Point(GRID_WIDTH * x, GRID_WIDTH * y), 12)
                piece.setFill('black')
                piece.draw(win)
                # 胜利
                if game_win(list2):
                    message = Text(Point(GRAPH_WIDTH / 2, GRID_WIDTH / 2), "人类胜利")
                    message.draw(win)
                    g = 1
                change = change + 1

    message = Text(Point(GRAPH_WIDTH / 2 + 100, GRID_WIDTH / 2), "游戏结束")
    message.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    GRID_WIDTH = 40
    COLUMN = 11
    ROW = 11
    GRAPH_WIDTH = GRID_WIDTH * (ROW + 1)
    GRAPH_HEIGHT = GRID_WIDTH * (COLUMN + 1)

    list1 = []  # AI
    list2 = []  # human
    list3 = []  # all
    list_all = []  # 整个棋盘的点
    next_point = [0, 0]  # AI下一步最应该下的位置

    mode=int(input("请选择: 快不准 或 慢却准 ? 1 : 0 \n"))
    if mode==1:
        DEPTH=1
    elif mode==0:
        DEPTH=3
    else:
        DEPTH=3

    shape_score = [(50, (0, 1, 1, 0, 0)),
                   (50, (0, 0, 1, 1, 0)),
                   (200, (1, 1, 0, 1, 0)),
                   (500, (0, 0, 1, 1, 1)),
                   (500, (1, 1, 1, 0, 0)),
                   (5000, (0, 1, 1, 1, 0)),
                   (5000, (0, 1, 0, 1, 1, 0)),
                   (5000, (0, 1, 1, 0, 1, 0)),
                   (5000, (1, 1, 1, 0, 1)),
                   (5000, (1, 1, 0, 1, 1)),
                   (5000, (1, 0, 1, 1, 1)),
                   (5000, (1, 1, 1, 1, 0)),
                   (5000, (0, 1, 1, 1, 1)),
                   (50000, (0, 1, 1, 1, 1, 0)),
                   (99999999, (1, 1, 1, 1, 1))]
    main()
