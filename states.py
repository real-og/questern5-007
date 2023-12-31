from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    greeting_screen = State()
    entering_name = State()
    entering_email = State()
    ended_task_1 = State()
    ended_task_2 = State()
    ended_task_3 = State()
    ended_task_4 = State()
    ended_task_5 = State()
    ended_task_6 = State()
    ended_task_7 = State()
    ended_task_8 = State()
    ended_task_9 = State()
    ended_task_10 = State()
    task_1_1 = State()
    task_2_1 = State()
    task_3_1 = State()
    task_4_1 = State()
    task_5_1 = State()
    task_5_2 = State()
    task_6_1 = State()
    task_7_1 = State()
    task_8_1 = State()
    task_9_1 = State()
    task_10_1 = State()
    task_10_2 = State()
    task_10_3 = State()
    ended = State()

    confirmation_name = State()
    task_1_2 = State()
    task_2_2 = State()
    task_3_2 = State()
    task_4_2 = State()
    task_4_3 = State()
    task_5_2 = State()
    task_6_2 = State()
    task_5_3 = State()

    end = State()
    
