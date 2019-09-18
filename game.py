import random
from tkinter import *
import os
from os import system
from tkinter import messagebox
from math import inf as infinity
from dataclasses import dataclass
import copy

@dataclass
class Branch:
    up: bool
    down: bool
    left: bool
    right: bool
    top_left: bool
    top_right: bool
    bottom_left: bool
    bottom_right: bool


option_gui = Tk()
option_gui.geometry("500x300")
option_gui.title('Who moves first?')

choice_frame = Frame(option_gui) #adding a frame
choice_frame.pack()

root = Tk()
root.geometry("800x500") #window size
root.title('Gomoku ')

frame = Frame(root) #adding a frame
frame.pack()

human = 1
computer = -1
matrix_size = 10
click_counter = -1

first_human = True

MIN = -1000000000
MAX = 1000000000

btn_list = []

btn_text = [[ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ],
            [ '', '' ,'', '', '', '', '', '', '','' ]]



def get_branch(i,j):

    branch = Branch(False,False,False,False,False,False,False,False)

    if((j-(matrix_size-1)) >= 0): branch.left = True
    if((j+(matrix_size-1)) <= matrix_size-1): branch.right = True
    if((i-(matrix_size-1)) >= 0): branch.up = True
    if((i+(matrix_size-1)) <= matrix_size-1): branch.down = True
    if(branch.up == True and branch.left == True)   :branch.top_left = True
    if(branch.up == True and branch.right == True)  :branch.top_right = True
    if(branch.down == True and branch.left == True) :branch.bottom_left = True
    if(branch.down == True and branch.right == True):branch.bottom_right = True

    return branch


def print_branch(i,j,branch):

    print('i: ',i,' j: ', j)

    print('left: ', branch.left)
    print('right: ',branch.right)
    print('up: ',branch.up)
    print('down: ',branch.down)

    print('top left: ', branch.top_left)
    print('top right: ',branch.top_right)
    print('bottom left: ',branch.bottom_left)
    print('bottom right: ',branch.bottom_right)



#Every choice and message function here


def show_match_message(message):
    messagebox.showinfo("Match found", message)



def want_to_replay():
    choice = messagebox.askquestion('Play again','Do you want to play again?')

    if choice == 'yes':
        reset_all()
        #get_move_choice()

    else:
        root.destroy()
        cli_clear()


def cli_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def reset_all():
    #print('reset function is callled!')

    for i in range(0,100):
        btn_list[i].config(text='')

    for i in range(0,10):
        for j in range(0,10):
            btn_text[i][j] = ''

    global click_counter
    click_counter = -1
    cli_clear()


def exit_game():

    choice = messagebox.askquestion('Exit Game','Are you sure you want to exit the game',icon = 'warning')

    if choice == 'yes':
        root.destroy()
        cli_clear()



#Operational functions are here!

def do_five_matches(i,j,branch):

    print('five match is caled for human player!')
    ch = btn_text[i][j]
    current_range = 5

    if(branch.left == True):
        is_matched = True
        for x in range(0, current_range):
            if(btn_text[i][j-x] != ch):
                is_matched = False
                break

        if(is_matched):
            show_match_message('five in a row in left!')
            return True


    if(branch.right == True):
        is_matched = True
        for x in range(0, current_range):
            if(btn_text[i][j+x] != ch):
                is_matched = False
                break

        if(is_matched):
            show_match_message('five in a row in left!')
            return True


    if(branch.up == True):
        is_matched = True
        for x in range(0, current_range):
            if(btn_text[i-x][j] != ch):
                is_matched = False
                break

        if(is_matched):
            show_match_message('five in a row in up!')
            return True

    if(branch.down == True):
        is_matched = True
        for x in range(0, current_range):
            if(btn_text[i+x][j] != ch):
                is_matched = False
                break

        if(is_matched):
            show_match_message('five in a row in down!')
            return True

    if(branch.top_left == True):
        is_matched = True
        for x in range(0, current_range):
            if(btn_text[i-x][j-x] != ch):
                is_matched = False
                break

        if(is_matched):
            show_match_message('five in a row in top left!')
            return True


    if(branch.top_right == True):
        is_matched = True
        for x in range(0, current_range):
            if(btn_text[i-x][j+x] != ch):
                is_matched = False
                break

        if(is_matched):
            show_match_message('five in a row in top right!')
            return True

    if(branch.bottom_left == True):
        is_matched = True

        for x in range(0, current_range):
            if(btn_text[i+x][j-x] != ch):
                is_matched = False
                break

        if(is_matched):
            show_match_message('five in a row in bottom left!')
            return True

    if(branch.bottom_right == True):
        is_matched = True
        for x in range(0, current_range):
            if(btn_text[i+x][j+x] != ch):
                is_matched = False
                break

        if(is_matched):
            show_match_message('five in a row in bottom right!')
            return True




def new_win_state(state):
    return                                    


def win_state(state):

    current_range = 5 #no of match needed to win in the game!
    winnable_situation = []

    for i in range(0,matrix_size):
        for j in range(0,matrix_size):

            if(state[i][j] == ''):
                continue #if an index is empty ,then it's not added!

            index_list = []
            branch = get_branch(i,j)

            if(branch.left == True):
                for x in range(0, current_range):
                    index_list.append(state[i][j-x])
                winnable_situation.append(index_list)
                index_list.clear()

            if(branch.right == True):
                for x in range(0, current_range):
                    index_list.append(state[i][j+x])
                winnable_situation.append(index_list)
                index_list.clear()

            if(branch.up == True):
                for x in range(0, current_range):
                    index_list.append(state[i-x][j])
                winnable_situation.append(index_list)
                index_list.clear()

            if(branch.down == True):
                for x in range(0, current_range):
                    index_list.append(state[i+x][j])
                winnable_situation.append(index_list)
                index_list.clear()

            if(branch.top_left == True):
                for x in range(0, current_range):
                    index_list.append(state[i-x][j-x])
                winnable_situation.append(index_list)
                index_list.clear()

            if(branch.top_right == True):
                for x in range(0, current_range):
                    index_list.append(state[i-x][j+x])
                winnable_situation.append(index_list)
                index_list.clear()

            if(branch.bottom_left == True):
                for x in range(0, current_range):
                    index_list.append(state[i+x][j-x])
                winnable_situation.append(index_list)
                index_list.clear()

            if(branch.bottom_right == True):
                for x in range(0, current_range):
                    index_list.append(state[i+x][j+x])
                winnable_situation.append(index_list)
                index_list.clear()

    return winnable_situation



def game_ovar(state,player): #game_over ta teo evaluation function ta kaaj korbo win_state na

    index = win_state(state)
    #print('length of the empty list:',len(index))

    if(player == 1):
        ch = '*'
    else:
        ch = 'o'

    if [ch,ch,ch,ch,ch] in index:
        print('match found!')
        return True
    else:
        return False

def who_won(state,player):

    index_list = win_state(state)
    #print('List size: ',len(index_list))
    if(player == -1):
        ch = '*'
    else:
        ch = 'o'

    if [ch,ch,ch,ch,ch] in index_list:
        if ch == '*':
            return 1
        elif ch == 'o':
            return -1
    else:
        return 0

def getScore(state,player,forHuman,humansTurn):
    return evaluateHorizontal(state,player,forHuman,humansTurn) + evaluateVertical(state,player,forHuman,humansTurn) + evaluateDiagonal(state,player,forHuman,humansTurn)

def myEvaluation(state,player):

    computer_score = 0
    human_score = 0
    # if(1 == player):
    #     computer_score = getScore(state,-1,True)
    #     human_score = getScore(state,1,False)
    # else:
    #     computer_score = getScore(state,-1,False)
    #     human_score = getScore(state,1,True)

    human_score = getScore(state,1,True,player == 1)
    computer_score = getScore(state,-1,False,player == 1)

    if(human_score == 0):
        human_score = 1.0
    return computer_score/human_score;

def evaluateHorizontal(state,player,forHuman,humansTurn):
    score = 0
    count = 0
    ch = ''
    group = 2

    if(player == -1):
        ch = 'o'
    else:
        ch = '*'

    for i in range(matrix_size):
        for j in range(matrix_size):
            if(state[i][j] == ch):
                count+=1
            elif(state[i][j] == ''):
                if(count > 0):
                    group-=1
                    score += getGroupScore(count,group,forHuman==humansTurn)
                    group = 1
                else:
                    group = 1
            elif(count > 0):
                score += getGroupScore(count,group,forHuman==humansTurn)
                count = 0
                group = 2
            else:
                group = 2
        if(count > 0):
            score += getGroupScore(count,group,forHuman==humansTurn)
        count = 0
        group = 2
    return score

def evaluateVertical(state,player,forHuman,humansTurn):
    score = 0
    count = 0
    ch = ''
    group = 2

    if(player == -1):
        ch = 'o'
    else:
        ch = '*'
    for j in range(matrix_size):
        for i in range(matrix_size):
            if(state[i][j] == ch):
                count+=1
            elif(state[i][j] == ''):
                if(count > 0):
                    group-=1
                    score += getGroupScore(count,group,forHuman==humansTurn)
                    group = 1
                else:
                    group = 1
            elif(count > 0):
                score += getGroupScore(count,group,forHuman==humansTurn)
                count = 0
                group = 2
            else:
                group = 2
        if(count > 0):
            score += getGroupScore(count,group,forHuman==humansTurn)
        count = 0
        group = 2
    return score

def evaluateDiagonal(state,player,forHuman,humansTurn):
    score = 0
    count = 0
    ch = ''
    group = 2

    if(player == -1):
        ch = 'o'
    else:
        ch = '*'

    for line in range(-9,10):
        start = max(0, line)
        end = min(9+line,9)
        for i in range(start,end+1):
            j = i-line
            if(state[i][j] == ch):
                count+=1
            elif(state[i][j] == ''):
                if(count > 0):
                    group -=1
                    score += getGroupScore(count,group,forHuman==humansTurn)
                    group = 1
                else:
                    group = 1
            elif(count > 0):
                score += getGroupScore(count,group,forHuman==humansTurn)
                count = 0
                group = 2
            else:
                group = 2
        if(count > 0):
            score += getGroupScore(count,group,forHuman==humansTurn)
        count = 0
        group = 2

    count = 0
    group = 2

    for line in range(19):
        start =  max(0,line-9)
        end = min(9,line)
        for i in range(start,end+1):
            j = line-i
            if(state[i][j] == ch):
                count +=1
            elif(state[i][j] == ''):
                if(count > 0):
                    group-=1
                    score += getGroupScore(count,group,forHuman==humansTurn)
                    group = 1
                else:
                    group = 1
            elif(count > 0):
                score += getGroupScore(count,group,forHuman==humansTurn)
                count = 0
                group = 2
            else:
                group = 2
        if(count > 0):
            score += getGroupScore(count,group,forHuman==humansTurn)
        count = 0
        group = 2

    return score

def getGroupScore(count,group,groundTruth):

    winPossiblity = 1000000
    if(group == 2 and count<5):
        return 0
    if(count == 5):
        return 100000000
    elif(count == 4):
        if(groundTruth):
            return winPossiblity
        else:
            if(group == 0):
                return winPossiblity/4
            else:
                return 200
    elif(count == 3):
        if(group == 0):
            if(groundTruth):
                return 50000
            else:
                return 200
        else:
            if(groundTruth):
                return 10
            else:
                return 5
    elif(count == 2):
        if(group==0):
            if(groundTruth):
                return 7
            else:
                return 5
        else:
            return 3
    elif(count == 1):
        return 1

    return 100000000*2

def check_match(i,j):

    branch = get_branch(i,j)
    print_branch(i,j,branch)
    if(do_five_matches(i,j,branch) == True):
        return True
    else:
        return False


def get_counter():

    global click_counter
    click_counter = click_counter + 1
    if(click_counter%2 == 0):
        return 0
    else:
        return 1


def get_empty_index(state):
    empty_index_list = []
    for i in range(10):
        for j in range(10):
            if(state[i][j] != ''):
                continue
            if(i > 0):
                if(j > 0):
                    if(state[i-1][j-1] != '' or state[i][j-1] != ''):
                        empty_index_list.append([i,j])
                        continue

                if(j < matrix_size-1):
                    if(state[i-1][j+1] != '' or state[i][j+1] != ''):
                        empty_index_list.append([i,j])
                        continue
                    if(state[i-1][j] != ''):
                        empty_index_list.append([i,j])
                        continue

            if( i < matrix_size-1):
                if(j > 0):
                    if(state[i+1][j-1] != '' or state[i][j-1] != ''):
                        empty_index_list.append([i,j])
                        continue

                if(j < matrix_size-1):
                    if(state[i+1][j+1] != '' or state[i][j+1] != ''):
                        empty_index_list.append([i,j])
                        continue
                    if(state[i+1][j] != ''):
                        empty_index_list.append([i,j])
                        continue

    return empty_index_list



def evaluate(state):
    return 0 #match tie beacuse it's already checked if someone has alraedy won the game.


def minimax(state, depth, player,alpha,beta):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == 1:
        #print('minimax called for human')
        best = [-1, -1, +infinity]
    else:
        #print('minimax called for computer')
        best = [-1, -1, -infinity]

    possible_moves = get_empty_index(state)
    if (depth == 0) or (possible_moves == None):
        # print("last depth reached")
        winner_score = myEvaluation(state,-player)  
        return [-1, -1, winner_score]

    # if player == computer:
    #     best = MIN

    #     for index in get_empty_index(state):
    #         i = index[0]
    #         j = index[1]
    #         val = minimax(depth + 1, nodeIndex * 2 + i,False, values, alpha, beta)
    #         best = max(best, val)
    #         alpha = max(alpha, best)
    #         # Alpha Beta Pruning
    #         if beta <= alpha:
    #             break
    #     return best
    #
    # else:
    #     best = MAX
    #     for i in range(0, 2):
    #         val = minimax(depth + 1, nodeIndex * 2 + i,True, values, alpha, beta)
    #         best = min(best, val)
    #         beta = min(beta, best)
    #         # Alpha Beta Pruning
    #         if beta <= alpha:
    #             break
    #     return best

    for index in possible_moves:
        i = index[0]
        j = index[1]

        if(player == 1):
            state[i][j] = '*'
        else:
            state[i][j] = 'o'

        score = minimax(state, depth - 1, -player,alpha,beta)

        state[i][j] = ''
        score[0] = i
        score[1] = j

        #print('score type:',type(score[2]))
        #print('best type',type(best[2]))

        if player == -1:
            if score[2] > best[2]:
                best = score  # max value
            if score[2] > alpha:
                alpha = score[2]
        else:
            if score[2] < best[2]:
                best = score  # min value
            if score[2] < beta:
                beta = score[2]
        if(beta <= alpha):
            # print(alpha)
            # print(beta)
            # print("pruned")
            break
    #print(best)
    return best


def searchWinningMove(state):
    possible_moves = get_empty_index(state)

    winning_move = []
    for index in possible_moves:
        dummy_state = copy.deepcopy(state)
        dummy_state[index[0]][index[1]] = 'o'
        hello = getScore(dummy_state,-1,False,False)
        if(hello >= 100000000):
            winning_move.append(index[0])
            winning_move.append(index[1])
            print(hello)
            print("winning move found")
            return winning_move
    return None

def get_computer_move(state):

    #print("computer move called")
    empty_index_list = get_empty_index(state)
    depth = 3

    #print(len(state)*len(state[0]))
    #print(depth)
    print(empty_index_list)

    winning_move = searchWinningMove(state)

    if(winning_move is not None):
        i = winning_move[0]
        j = winning_move[1]
        if(get_counter() == 0):
            state[i][j] = '*'
        else:
            state[i][j] = 'o'

        btn_list[i*10+j].config(text=state[i][j])

    else:
        index = minimax(btn_text,depth,computer,MIN,MAX)

        i = index[0]
        j = index[1]

        if(get_counter() == 0):
            state[i][j] = '*'
        else:
            state[i][j] = 'o'

        btn_list[i*10+j].config(text=state[i][j])

def check_winner(state):
    if(getScore(state,1,True,False) >= 100000000):
        return 1
    if(getScore(state,-1,False,True) >= 100000000):
        return -1
    return 0


def update_btn_text(index):

    i = int(index[0])
    j = int(index[1])

    if(btn_text[i][j] == ''):

        if(get_counter() == 0):
            btn_text[i][j] = '*'
        else:
            btn_text[i][j] = 'o'
        btn_list[i*10+j].config(text=btn_text[i][j])

        winner = check_winner(btn_text)

        if(winner == 1):
            show_match_message("You won, Congrats!!!")
            want_to_replay()
        else:
            get_computer_move(btn_text)
            winner = check_winner(btn_text)
            if(winner == -1):
                show_match_message("Computer won, Shame!!!")
                want_to_replay()

        # is_game_over = check_match(i,j)
        # if(is_game_over == True):
        #     want_to_replay()
        # else:
        #     if(get_computer_move(btn_text) == True):
        #         show_match_message("Computer won, Shame !")
        #         want_to_replay()




def create_board(choice):


    button00 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('00'))
    button01 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('01'))
    button02 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('02'))
    button03 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('03'))
    button04 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('04'))
    button05 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('05'))
    button06 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('06'))
    button07 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('07'))
    button08 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('08'))
    button09 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('09'))

    button10 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('10'))
    button11 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('11'))
    button12 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('12'))
    button13 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('13'))
    button14 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('14'))
    button15 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('15'))
    button16 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('16'))
    button17 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('17'))
    button18 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('18'))
    button19 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('19'))

    button20 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('20'))
    button21 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('21'))
    button22 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('22'))
    button23 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('23'))
    button24 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('24'))
    button25 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('25'))
    button26 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('26'))
    button27 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('27'))
    button28 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('28'))
    button29 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('29'))

    button30 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('30'))
    button30 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('30'))
    button31 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('31'))
    button32 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('32'))
    button33 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('33'))
    button34 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('34'))
    button35 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('35'))
    button36 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('36'))
    button37 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('37'))
    button38 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('38'))
    button39 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('39'))

    button40 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('40'))
    button41 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('41'))
    button42 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('42'))
    button43 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('43'))
    button44 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('44'))
    button45 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('45'))
    button46 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('46'))
    button47 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('47'))
    button48 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('48'))
    button49 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('49'))

    button50 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('50'))
    button51 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('51'))
    button52 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('52'))
    button53 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('53'))
    button54 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('54'))
    button55 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('55'))
    button56 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('56'))
    button57 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('57'))
    button58 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('58'))
    button59 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('59'))

    button60 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('60'))
    button61 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('61'))
    button62 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('62'))
    button63 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('63'))
    button64 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('64'))
    button65 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('65'))
    button66 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('66'))
    button67 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('67'))
    button68 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('68'))
    button69 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('69'))

    button70 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('70'))
    button71 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('71'))
    button72 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('72'))
    button73 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('73'))
    button74 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('74'))
    button75 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('75'))
    button76 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('76'))
    button77 = Button(frame,height='1', width='2',font="Verdana 14 bold", fg = 'red',command = lambda: update_btn_text('77'))
    button78 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('78'))
    button79 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('79'))

    button80 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('80'))
    button81 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('81'))
    button82 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('82'))
    button83 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('83'))
    button84 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('84'))
    button85 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('85'))
    button86 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('86'))
    button87 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('87'))
    button88 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('88'))
    button89 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('89'))

    button90 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('90'))
    button91 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('91'))
    button92 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('92'))
    button93 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('93'))
    button94 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('94'))
    button95 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('95'))
    button96 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('96'))
    button97 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('97'))
    button98 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('98'))
    button99 = Button(frame, height='1', width='2',font="Verdana 14 bold",fg = 'red',command = lambda: update_btn_text('99'))

    button_replay = Button(frame,height='1', width='5',font="Verdana 14 bold",fg = 'red',text='Replay', command= lambda: reset_all())
    button_exit = Button(frame,height='1', width='4',font="Verdana 14 bold",fg = 'red',text='Exit',command= lambda: exit_game())


    button00.grid(row = 0, column=0)
    button01.grid(row = 0, column=1)
    button02.grid(row = 0, column=2)
    button03.grid(row = 0, column=3)
    button04.grid(row = 0, column=4)
    button05.grid(row = 0, column=5)
    button06.grid(row = 0, column=6)
    button07.grid(row = 0, column=7)
    button08.grid(row = 0, column=8)
    button09.grid(row = 0, column=9)

    button10.grid(row = 1, column=0)
    button11.grid(row = 1, column=1)
    button12.grid(row = 1, column=2)
    button13.grid(row = 1, column=3)
    button14.grid(row = 1, column=4)
    button15.grid(row = 1, column=5)
    button16.grid(row = 1, column=6)
    button17.grid(row = 1, column=7)
    button18.grid(row = 1, column=8)
    button19.grid(row = 1, column=9)

    button20.grid(row =  2, column=0)
    button21.grid(row =  2, column=1)
    button22.grid(row =  2, column=2)
    button23.grid(row =  2, column=3)
    button24.grid(row =  2, column=4)
    button25.grid(row =  2, column=5)
    button26.grid(row =  2, column=6)
    button27.grid(row =  2, column=7)
    button28.grid(row =  2, column=8)
    button29.grid(row =  2, column=9)

    button30.grid(row =  3, column=0)
    button31.grid(row =  3, column=1)
    button32.grid(row =  3, column=2)
    button33.grid(row =  3, column=3)
    button34.grid(row =  3, column=4)
    button35.grid(row =  3, column=5)
    button36.grid(row =  3, column=6)
    button37.grid(row =  3, column=7)
    button38.grid(row =  3, column=8)
    button39.grid(row =  3, column=9)

    button40.grid(row =  4, column=0)
    button41.grid(row =  4, column=1)
    button42.grid(row =  4, column=2)
    button43.grid(row =  4, column=3)
    button44.grid(row =  4, column=4)
    button45.grid(row =  4, column=5)
    button46.grid(row =  4, column=6)
    button47.grid(row =  4, column=7)
    button48.grid(row =  4, column=8)
    button49.grid(row =  4, column=9)

    button50.grid(row =  5, column=0)
    button51.grid(row =  5, column=1)
    button52.grid(row =  5, column=2)
    button53.grid(row =  5, column=3)
    button54.grid(row =  5, column=4)
    button55.grid(row =  5, column=5)
    button56.grid(row =  5, column=6)
    button57.grid(row =  5, column=7)
    button58.grid(row =  5, column=8)
    button59.grid(row =  5, column=9)

    button60.grid(row =  6, column=0)
    button61.grid(row =  6, column=1)
    button62.grid(row =  6, column=2)
    button63.grid(row =  6, column=3)
    button64.grid(row =  6, column=4)
    button65.grid(row =  6, column=5)
    button66.grid(row =  6, column=6)
    button67.grid(row =  6, column=7)
    button68.grid(row =  6, column=8)
    button69.grid(row =  6, column=9)

    button70.grid(row =  7, column=0)
    button71.grid(row =  7, column=1)
    button72.grid(row =  7, column=2)
    button73.grid(row =  7, column=3)
    button74.grid(row =  7, column=4)
    button75.grid(row =  7, column=5)
    button76.grid(row =  7, column=6)
    button77.grid(row =  7, column=7)
    button78.grid(row =  7, column=8)
    button79.grid(row =  7, column=9)

    button80.grid(row =  8, column=0)
    button81.grid(row =  8, column=1)
    button82.grid(row =  8, column=2)
    button83.grid(row =  8, column=3)
    button84.grid(row =  8, column=4)
    button85.grid(row =  8, column=5)
    button86.grid(row =  8, column=6)
    button87.grid(row =  8, column=7)
    button88.grid(row =  8, column=8)
    button89.grid(row =  8, column=9)

    button90.grid(row =  9, column=0)
    button91.grid(row =  9, column=1)
    button92.grid(row =  9, column=2)
    button93.grid(row =  9, column=3)
    button94.grid(row =  9, column=4)
    button95.grid(row =  9, column=5)
    button96.grid(row =  9, column=6)
    button97.grid(row =  9, column=7)
    button98.grid(row =  9, column=8)
    button99.grid(row =  9, column=9)

    button_replay.grid(row = 10,column=0, columnspan=2,sticky=W+E)
    button_exit.grid(row = 10 ,column=8, columnspan=2,sticky=W+E)

    btn_list.append(button00)
    btn_list.append(button01)
    btn_list.append(button02)
    btn_list.append(button03)
    btn_list.append(button04)
    btn_list.append(button05)
    btn_list.append(button06)
    btn_list.append(button07)
    btn_list.append(button08)
    btn_list.append(button09)

    btn_list.append(button10)
    btn_list.append(button11)
    btn_list.append(button12)
    btn_list.append(button13)
    btn_list.append(button14)
    btn_list.append(button15)
    btn_list.append(button16)
    btn_list.append(button17)
    btn_list.append(button18)
    btn_list.append(button19)

    btn_list.append(button20)
    btn_list.append(button21)
    btn_list.append(button22)
    btn_list.append(button23)
    btn_list.append(button24)
    btn_list.append(button25)
    btn_list.append(button26)
    btn_list.append(button27)
    btn_list.append(button28)
    btn_list.append(button29)

    btn_list.append(button30)
    btn_list.append(button31)
    btn_list.append(button32)
    btn_list.append(button33)
    btn_list.append(button34)
    btn_list.append(button35)
    btn_list.append(button36)
    btn_list.append(button37)
    btn_list.append(button38)
    btn_list.append(button39)

    btn_list.append(button40)
    btn_list.append(button41)
    btn_list.append(button42)
    btn_list.append(button43)
    btn_list.append(button44)
    btn_list.append(button45)
    btn_list.append(button46)
    btn_list.append(button47)
    btn_list.append(button48)
    btn_list.append(button49)

    btn_list.append(button50)
    btn_list.append(button51)
    btn_list.append(button52)
    btn_list.append(button53)
    btn_list.append(button54)
    btn_list.append(button55)
    btn_list.append(button56)
    btn_list.append(button57)
    btn_list.append(button58)
    btn_list.append(button59)

    btn_list.append(button60)
    btn_list.append(button61)
    btn_list.append(button62)
    btn_list.append(button63)
    btn_list.append(button64)
    btn_list.append(button65)
    btn_list.append(button66)
    btn_list.append(button67)
    btn_list.append(button68)
    btn_list.append(button69)

    btn_list.append(button70)
    btn_list.append(button71)
    btn_list.append(button72)
    btn_list.append(button73)
    btn_list.append(button74)
    btn_list.append(button75)
    btn_list.append(button76)
    btn_list.append(button77)
    btn_list.append(button78)
    btn_list.append(button79)

    btn_list.append(button80)
    btn_list.append(button81)
    btn_list.append(button82)
    btn_list.append(button83)
    btn_list.append(button84)
    btn_list.append(button85)
    btn_list.append(button86)
    btn_list.append(button87)
    btn_list.append(button88)
    btn_list.append(button89)

    btn_list.append(button90)
    btn_list.append(button91)
    btn_list.append(button92)
    btn_list.append(button93)
    btn_list.append(button94)
    btn_list.append(button95)
    btn_list.append(button96)
    btn_list.append(button97)
    btn_list.append(button98)
    btn_list.append(button99)

    if(choice == False ):
        btn_list[55].config(text='o')


    root.mainloop()

def set_first_move_var(choice):
    first_human = choice
    print(first_human)
    option_gui.destroy()
    create_board(choice)
   


def get_move_choice():

    human_go = Button(choice_frame, height='2', width='8',font="Verdana 10 bold",fg = 'red', text='Human',command = lambda: set_first_move_var(True))
    computer_go = Button(choice_frame, height='2', width='8',font="Verdana 10 bold",fg = 'red',text='Computer',command = lambda: set_first_move_var(False))
    human_go.grid(row = 1,column=0, columnspan=2,sticky=W+E)
    computer_go.grid(row = 1,column=8, columnspan=2,sticky=W+E)
    option_gui.mainloop()




def main():
    #print(len(btn_text)*len(btn_text[0]))
    get_move_choice()



if __name__ == '__main__':
    main()
