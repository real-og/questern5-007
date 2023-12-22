from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable
import logic


@dp.message_handler(state=State.entering_name)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.generate_confirmation_msg(message.text), reply_markup=kb.yes_no_kb)
    await state.update_data(team_name=message.text)
    await State.confirmation_name.set()

@dp.message_handler(state=State.confirmation_name)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.yes_btn:
        data = await state.get_data()
        await aiotable.change_name(str(message.from_user.id), data.get('team_name'))
        await message.answer(texts.ask_for_beginning, reply_markup=kb.begin_quest_kb)
        await State.greeting_screen.set()
    else:
        await message.answer(texts.enter_another_name)
        await State.entering_name.set()

# @dp.message_handler(state=State.entering_email)
# async def send_welcome(message: types.Message, state: FSMContext):
#     input = message.text.strip()
#     if not logic.is_valid_email(input):
#         await message.answer(texts.bad_email)
#         return
#     await aiotable.change_email(str(message.from_user.id), input)
#     # table.sheet.change_email(str(message.from_user.id), input)
#     await message.answer(texts.ask_for_beginning, reply_markup=kb.begin_quest_kb)
#     await State.greeting_screen.set()