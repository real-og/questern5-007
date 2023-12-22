from loader import dp, bot, MAIN_CODE
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable

@dp.message_handler(state=State.ended_task_6)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.enter_code_btn:
        await message.answer(texts.task_7_1, reply_markup=kb.get_code_keyboard([]))
        await state.update_data(selected_digits=[]) 
        await aiotable.change_level(str(message.from_user.id), '7')
        await State.task_7_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.enter_code_kb)




@dp.callback_query_handler(state=State.task_7_1)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    tapped_num = int(callback.data)
    print(tapped_num)
    data = await state.get_data()
    selected = data.get('selected_digits')
    code = MAIN_CODE
    
    
    position = len(selected)

    if code[position] == str(tapped_num):
        selected.append(tapped_num)
    else:
        selected = []
    print(selected)
    try:
        await bot.edit_message_reply_markup(callback.message.chat.id,
                            callback.message.message_id,
                            reply_markup=kb.get_code_keyboard(selected))
    except:
        pass
    if len(selected) == 6:
        selected = []
        await State.end.set()
        await callback.message.answer(texts.end_code)
        await callback.message.answer(texts.end_finish)

    await state.update_data(selected_digits=selected) 
    await bot.answer_callback_query(callback.id)

