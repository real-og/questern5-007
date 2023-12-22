from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable


@dp.message_handler(state=State.ended_task_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.mission2_btn:
        await aiotable.change_level(str(message.from_user.id), '2')
        await message.answer(texts.task_2_1)
        await State.task_2_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.mission2_kb)



@dp.message_handler(state=State.task_2_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_2_1_ans:
        await message.answer(texts.right_answer)
        await message.answer(texts.task_2_2, reply_markup=kb.hint_kb)
        await State.task_2_2.set()
    else:
        await message.answer(texts.wrong_answer)



@dp.message_handler(state=State.task_2_2)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_2_2_ans:
        await message.answer(texts.task_2_2_rigth)
        await message.answer(texts.get_number)
        await message.answer(texts.num_7)
        await message.answer(texts.mission_completed, reply_markup=kb.mission3_kb)
        await State.ended_task_2.set()

    elif input == texts.get_hint:
        await message.answer(texts.task_2_1_hint, reply_markup=kb.hint_double_kb)
    elif input == texts.get_more_hint:
        await message.answer(texts.task_2_2_hint, reply_markup=kb.hint_kb)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)


