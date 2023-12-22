from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts
from typing import List

begin_quest_kb = ReplyKeyboardMarkup([[texts.start_travel]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

mission2_kb = ReplyKeyboardMarkup([[texts.mission2_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
mission3_kb = ReplyKeyboardMarkup([[texts.mission3_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
mission4_kb = ReplyKeyboardMarkup([[texts.mission4_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
mission5_kb = ReplyKeyboardMarkup([[texts.mission5_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
mission6_kb = ReplyKeyboardMarkup([[texts.mission6_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

enter_code_kb = ReplyKeyboardMarkup([[texts.enter_code_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

hint_kb = ReplyKeyboardMarkup([[texts.get_hint]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

hint_double_kb = ReplyKeyboardMarkup([[texts.get_more_hint]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)



continue_kb = ReplyKeyboardMarkup([[texts.continue_quest]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)


hint_extended_kb = ReplyKeyboardMarkup([[texts.get_hint], [texts.hint_find_code_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

hint_location_kb = ReplyKeyboardMarkup([[texts.hint_find_code_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)


yes_no_kb = ReplyKeyboardMarkup([[texts.yes_btn, texts.no_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)


def get_code_keyboard(selected: List[int]):
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='☑️' if 1 in selected else '3️⃣', callback_data='1')
    button_2 = InlineKeyboardButton(text='☑️' if 2 in selected else '7️⃣', callback_data='2')
    button_3 = InlineKeyboardButton(text='☑️' if 3 in selected else '9️⃣', callback_data='3')
    button_4 = InlineKeyboardButton(text='☑️' if 4 in selected else '8️⃣', callback_data='4')
    button_5 = InlineKeyboardButton(text='☑️' if 5 in selected else '4️⃣', callback_data='5')
    button_6 = InlineKeyboardButton(text='☑️' if 6 in selected else '8️⃣', callback_data='6')

    kb.row(button_1, button_2, button_3, button_4, button_5, button_6)
    # kb.row(button_4, button_5, button_6)

    return kb
