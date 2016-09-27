#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    p=0
    while wall_is_on_the_right()==False:
        p+=1
        if wall_is_above()==False:
            k=0
            while wall_is_above()==False:
                move_up()
                fill_cell()
                k+=1
            move_down(k)
        move_right()
    if wall_is_on_the_right()==True and wall_is_above()==False:
        k=0
        while wall_is_above()==False:
            move_up()
            fill_cell()
            k+=1
        move_down(k)
    move_left(p+1)

if __name__ == '__main__':
    run_tasks()
