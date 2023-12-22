from loader import dp, CODES
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):

    if len(message.text.split()) == 2:
        code = message.text.split()[1]
        if code in CODES:
            await message.answer(texts.greeting)
            await message.answer(texts.ask_for_name)


            await State.entering_name.set()
            # await State.ended_task_6.set()


            await state.update_data(team_number=CODES.index(code) + 1)
 
            await aiotable.append_user(str(message.from_user.id), message.from_user.username, message.from_user.full_name)
            
        else:
            await message.answer(texts.wrong_code)
    else:
        await message.answer(texts.no_code_enter)


@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help_message)
