#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right(n=1)
    fill_cell()
    for i in range (11):
        for i in range(2,28,1):
            move_right(n=1)
            if cell_is_filled()==False:
                fill_cell()
        move_down(n=1)
        fill_cell()
        for i in range(2,28,1):
            move_left(n=1)
            if cell_is_filled()==False:
                    fill_cell()
    move_down(n=1)





if __name__ == '__main__':
    run_tasks()
