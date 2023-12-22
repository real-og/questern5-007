from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable


@dp.message_handler(state=State.ended_task_4)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.mission5_btn:
        await aiotable.change_level(str(message.from_user.id), '5')
        await message.answer(texts.task_5_1)
        await State.task_5_1.set()
        await state.update_data(task_5_ans=['0', '0', '0', '0', '0', '0', '0'])
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.mission5_kb)



@dp.message_handler(state=State.task_5_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_5_1_ans:
        await message.answer(texts.right_answer)
        await message.answer(texts.task_5_2)
        await State.task_5_2.set()
    else:
        await message.answer(texts.wrong_answer)




@dp.message_handler(state=State.task_5_2)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip().upper()
    data = await state.get_data()
    ar = data.get('task_5_ans')
    if input == 'ГЕРМАНИЯ':
        ar[0] = '1'
        if ar != ['1', '1', '1', '1', '1', '1', '1']:
            await message.answer('Верно ☑️ Продолжайте!')
    elif input == 'ИСПАНИЯ':
        ar[1] = '1'
        if ar != ['1', '1', '1', '1', '1', '1', '1']:
            await message.answer('Верно ☑️ Продолжайте!')
    elif input == 'ИТАЛИЯ':
        ar[2] = '1'
        if ar != ['1', '1', '1', '1', '1', '1', '1']:
            await message.answer('Верно ☑️ Продолжайте!')
    elif input == 'ПОРТУГАЛИЯ':
        ar[3] = '1'
        if ar != ['1', '1', '1', '1', '1', '1', '1']:
            await message.answer('Верно ☑️ Продолжайте!')
    elif input == 'КИТАЙ':
        ar[4] = '1'
        if ar != ['1', '1', '1', '1', '1', '1', '1']:
            await message.answer('Верно ☑️ Продолжайте!')
    elif input == 'ЧИЛИ':
        ar[5] = '1'
        if ar != ['1', '1', '1', '1', '1', '1', '1']:
            await message.answer('Верно ☑️ Продолжайте!')
    elif input == 'СУДАН':
        ar[6] = '1'
        if ar != ['1', '1', '1', '1', '1', '1', '1']:
            await message.answer('Верно ☑️ Продолжайте!')
    else:
        await message.answer('Неверно')

    await state.update_data(task_5_ans=ar)
    

    if ar == ['1', '1', '1', '1', '1', '1', '1']:
        await message.answer('С первой частью миссии вы успешно справились. Поздравляю!')
        await message.answer(texts.task_5_3, reply_markup=kb.hint_kb)
        await State.task_5_3.set()



@dp.message_handler(state=State.task_5_3)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_5_3_ans:
        await message.answer('Верно.')
        await message.answer(texts.get_number)
        await message.answer(texts.num_4)
        await message.answer(texts.mission_completed, reply_markup=kb.mission6_kb)
        await State.ended_task_5.set()
    elif input == texts.get_hint:
        await message.answer(texts.task_5_1_hint, reply_markup=kb.hint_double_kb)
    elif input == texts.get_more_hint:
        await message.answer(texts.task_5_2_hint, reply_markup=kb.hint_kb)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)
