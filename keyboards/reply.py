from distutils.command.build import build

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    KeyboardButtonRequestChat
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import reply_buttons, inline_buttons


def start_admin()->ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=reply_buttons['market']),
                KeyboardButton(text=reply_buttons['admin_panel'])
            ],
        ]
    )
    return buttons

def product_panel()->ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=reply_buttons['show_products']),
                KeyboardButton(text=reply_buttons['add_product'])
            ],
            [
                KeyboardButton(text=reply_buttons['delete_product'])
            ],
            [
                KeyboardButton(text=reply_buttons['back'])
            ]
        ]
    )
    return buttons

def admin_panel()->ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=reply_buttons['admins']),
                KeyboardButton(text=reply_buttons['channels'])
            ],
            [
                KeyboardButton(text=reply_buttons['menu_products']),
                KeyboardButton(text=reply_buttons['users'])
            ],
            [
                KeyboardButton(text=reply_buttons['back_to_menu'])
            ]
        ]
    )
    return buttons

def button_admins()->ReplyKeyboardMarkup:

    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=reply_buttons['show_admins']),
                KeyboardButton(text=reply_buttons['add_admin']),
                KeyboardButton(text=reply_buttons['delete_admin'])

            ],
            [
                KeyboardButton(text=reply_buttons['back'])
            ]
        ]
    )

    return buttons

def button_channels()->ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=reply_buttons['show_channels']),
                KeyboardButton(text=reply_buttons['add_channel']),
                KeyboardButton(text=reply_buttons['delete_channel'])
            ],
            [
                KeyboardButton(text=reply_buttons['back'])
            ]
        ]
    )
    return buttons

def button_menu_products()->ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=reply_buttons['categories']),
                KeyboardButton(text=reply_buttons['sub_categories']),
                KeyboardButton(text=reply_buttons['products'])
            ],
            [
                KeyboardButton(text=reply_buttons['back'])
            ]
        ]
    )
    return buttons

def show_menu_categories()->ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=reply_buttons['get_categories']),
                KeyboardButton(text=reply_buttons['add_category'])
            ],
            [
                KeyboardButton(text=reply_buttons['edit_category']),
                KeyboardButton(text=reply_buttons['delete_category'])
            ],
            [
                KeyboardButton(text=reply_buttons['back'])
            ]
        ]
    )
    return buttons

def show_menu_sub_categories()->ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=reply_buttons['get_sub_categories']),
                KeyboardButton(text=reply_buttons['add_sub_category'])
            ],
            [
                KeyboardButton(text=reply_buttons['edit_sub_category']),
                KeyboardButton(text=reply_buttons['delete_sub_category'])
            ],
            [
                KeyboardButton(text=reply_buttons['back'])
            ]
        ]
    )
    return buttons

def show_categories_inline(categories:tuple)->InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.max_width = 3
    button_cancel = InlineKeyboardButton(text=inline_buttons['delete_button'],
                                         callback_data='delete_message')
    for category in categories:
        builder.add(InlineKeyboardButton(text=f'{category[0].capitalize()}',
                                         callback_data=f'{category[0]}:show_category'))
    builder.row(button_cancel)
    return builder.as_markup()

def show_products_in_admin_panel(products:list)->InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.max_width = 3
    for product in products:
        builder.add(InlineKeyboardButton(text=f'{product[5].capitalize()}', callback_data=f'show_product_admin:{product[0]}'))
    builder.row(InlineKeyboardButton(text=inline_buttons['delete_button'],
                                         callback_data='delete_message'))
    return builder.as_markup()

def get_sex_of_product()->InlineKeyboardMarkup:
    button_male = InlineKeyboardButton(text='Male', callback_data='sex_product_admin:male')
    button_female = InlineKeyboardButton(text='Female', callback_data='sex_product_admin:female')
    button_default = InlineKeyboardButton(text='Default', callback_data='sex_product_admin:none')
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                button_male,
                button_female
            ],
            [
                button_default
            ]
        ]
    )
    return buttons


def show_sub_categories_inline(sub_categories:tuple)->InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.max_width = 3
    button_cancel = InlineKeyboardButton(text=inline_buttons['delete_button'],
                                         callback_data='delete_message')
    for sub_cat in sub_categories:
        builder.add(InlineKeyboardButton(text=f'{sub_cat[0].capitalize()}', callback_data=f'{sub_cat[0].capitalize()}:show_sub_category'))

    builder.row(button_cancel)
    return builder.as_markup()

def generate_subs_buttons(button_list:list)->InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.max_width=3
    button_check = InlineKeyboardButton(text='Check✅', callback_data='check_sub')
    for button in button_list:
        builder.add(InlineKeyboardButton(text="Subscribe", url=button))
    builder.row(button_check)
    return builder.as_markup()

def get_channel()->ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text='Choose group', request_chat=KeyboardButtonRequestChat(
                    request_id=1,
                    chat_is_channel=False
                )),
                KeyboardButton(text='Choose channel', request_chat=KeyboardButtonRequestChat(
                    request_id=2,
                    chat_is_channel=True
                ))
            ]
        ]
    )
    return buttons
