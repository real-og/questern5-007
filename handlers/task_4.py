from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import table
import aiotable


@dp.message_handler(state=State.ended_task_3)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input == texts.mission4_btn:
        await aiotable.change_level(str(message.from_user.id), '4')
        await message.answer(texts.task_4_1)
        await state.update_data(task_4_ans=['0', '0', '0', '0', '0', '0'])
        await State.task_4_1.set()
    else:
        await message.answer(texts.use_keyboards, reply_markup=kb.mission4_kb)



@dp.message_handler(state=State.task_4_1)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_4_1_ans:

        await message.answer(texts.right_answer)
        await message.answer(texts.task_4_2)
        await State.task_4_2.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.task_4_2)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip().upper()
    data = await state.get_data()
    ar = data.get('task_4_ans')
    if input == '10':
        ar[0] = '1'
        await message.answer('Н')
    elif input == '343':
        await message.answer('Да, это номер указан на танке. Напишите сумму этих 3 чисел.')
    elif input == 'CARLSON':
        ar[1] = '1'
        await message.answer('А')
    elif input in ['CARLSSON', 'KARLSSON', 'KARLSON',]:
        await message.answer('Проверьте правильность написания этого слова.')
    elif input in ['PARIS', 'ПАРИЖ']:
        ar[2] = '1'
        await message.answer('Л')
    elif input == 'VB':
        await message.answer('C')
        ar[3] = '1'
    elif input in ['ЖЕЛТЫЙ', 'ЖЕЛТОГО', 'ЖЕЛТЫЙ ЦВЕТ', 'ЖЕЛТОГО ЦВЕТА', 'ЖЁЛТЫЙ', 'ЖЁЛТОГО', 'ЖЁЛТЫЙ ЦВЕТ', 'ЖЁЛТОГО ЦВЕТА', ]:
        await message.answer('У')
        ar[4] = '1'
    elif input == 'ВЕЛИКОБРИТАНИЯ':
        await message.answer('Р')
        ar[5] = '1'
    elif input == 'АНГЛИЯ':
        await message.answer('Англия входит в состав этого государства. Как называется это государство?')
    elif '10' in input or 'CARLSON' in input or'PARIS'in input or 'ПАРИЖ'in input or 'VB'in input or'ЖЕЛТЫЙ'in input or 'ЖЁЛТОГО ЦВЕТА' in input or'ВЕЛИКОБРИТАНИЯ'in input:
        await message.answer('Вы меня запутали. Пришлите каждый ответ отдельным сообщением.')
    else:
        await message.answer('Неверно')

    
    if ar == ['1', '1', '1', '1', '1', '1']:
        await message.answer('Вы ответили правильно на все вопросы. Составьте из полученных букв слово.',reply_markup=kb.hint_kb)
        await State.task_4_3.set()

    await state.update_data(task_4_ans=ar)




@dp.message_handler(state=State.task_4_3)
async def send_welcome(message: types.Message, state: FSMContext):
    input = message.text.strip()
    if input.upper() in texts.task_4_2_ans:
        await message.answer(texts.task_4_2_right)
        await message.answer(texts.get_number)
        await message.answer(texts.num_8)
        await message.answer(texts.mission_completed, reply_markup=kb.mission5_kb)
        await State.ended_task_4.set()
    elif input == texts.get_hint:
        await message.answer(texts.task_4_1_hint, reply_markup=kb.hint_kb)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.hint_kb)