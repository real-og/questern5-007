from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable


@dp.message_handler(state=State.ended_task_2)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.mission3_btn:
        await aiotable.change_level(str(message.from_user.id), '3')
        await message.answer(texts.task_3_1)
        await State.task_3_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.mission3_kb)



@dp.message_handler(state=State.task_3_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_3_1_ans:
        await message.answer(texts.right_answer)
        await message.answer(texts.task_3_2)
        await State.task_3_2.set()
    else:
        await message.answer(texts.wrong_answer)



@dp.message_handler(state=State.task_3_2)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_3_2_ans:
        await message.answer(texts.task_3_2_right)
        await message.answer(texts.get_number)
        await message.answer(texts.num_9)
        await message.answer(texts.mission_completed, reply_markup=kb.mission4_kb)
        await State.ended_task_3.set()
    elif input.upper() in texts.task_3_2_ans_wrong:
        await message.answer(texts.task_3_1_correction)
    else:
        await message.answer(texts.wrong_answer)


