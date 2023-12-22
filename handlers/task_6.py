from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable


@dp.message_handler(state=State.ended_task_5)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.mission6_btn:
        await aiotable.change_level(str(message.from_user.id), '6')
        await message.answer(texts.task_6_1)
        await State.task_6_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.mission6_kb)



@dp.message_handler(state=State.task_6_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_6_1_ans:
        await message.answer(texts.right_answer)
        await message.answer(texts.task_6_2)
        await State.task_6_2.set()
    else:
        await message.answer(texts.wrong_answer)



@dp.message_handler(state=State.task_6_2)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_6_2_ans:
        await message.answer(texts.task_6_2_right)
        await message.answer(texts.get_number)
        await message.answer(texts.num_8)
        await message.answer('Миссия пройдена!')
        await message.answer(texts.code_task, reply_markup=kb.enter_code_kb)
        await State.ended_task_6.set()
    elif input.upper() in texts.task_6_2_ans_wrong:
        await message.answer(texts.task_6_1_correction)
    else:
        await message.answer(texts.wrong_answer)