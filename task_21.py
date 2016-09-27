#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right(n=1)
    move_down(n=1)
    fill_cell()
    n=14
    for i in range (12):
        for i in range(2,n,1):
            move_down(n=1)
            if cell_is_filled()==False:
                fill_cell()
        move_right(n=1)
        for i in range(2,n-1,1):
            move_up(n=1)
            if cell_is_filled()==False:
                fill_cell()
        n=n-1
    fill_cell()
    move_down(n=1)
    move_left(n=12)

    pass


if __name__ == '__main__':
    run_tasks()
