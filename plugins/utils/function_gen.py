import asyncio
import re
import ast       
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters

from image.edit_1 import (  # pylint:disable=import-error
    bright,
    mix,
    black_white,
    g_blur,
    normal_blur,
    box_blur,
)
from image.edit_2 import (  # pylint:disable=import-error
    circle_with_bg,
    circle_without_bg,
    sticker,
    edge_curved,
    contrast,
    sepia_mode,
    pencil,
    cartoon,
)
from image.edit_3 import (  # pylint:disable=import-error
    green_border,
    blue_border,
    black_border,
    red_border,
)
from image.edit_4 import (  # pylint:disable=import-error
    rotate_90,
    rotate_180,
    rotate_270,
    inverted,
    round_sticker,
    removebg_white,
    removebg_plain,
    removebg_sticker,
)
from image.edit_5 import (  # pylint:disable=import-error
    normalglitch_1,
    normalglitch_2,
    normalglitch_3,
    normalglitch_4,
    normalglitch_5,
    scanlineglitch_1,
    scanlineglitch_2,
    scanlineglitch_3,
    scanlineglitch_4,
    scanlineglitch_5,
)



@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "removebg":
        await query.message.edit_text(
            "**Select required mode**γ€γ€γ€γ€",
            reply_markup=InlineKeyboardMarkup(
                [[
                InlineKeyboardButton(text="πΆπππ πΆππππΎ π‘π¦", callback_data="rmbgwhite"),
                InlineKeyboardButton(text="πΆππππππ π‘π¦", callback_data="rmbgplain"),
                ],[
                InlineKeyboardButton(text="π²πππΌππΎπ", callback_data="rmbgsticker"),
                ],[
                InlineKeyboardButton('π±π°π²πΊ', callback_data='photo')
             ]]
        ),)
    elif query.data == "stick":
        await query.message.edit(
            "**Select a Type**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="π­ππππΊπ", callback_data="stkr"),
                        InlineKeyboardButton(
                            text="π€π½ππΎ π’ππππΎπ½", callback_data="cur_ved"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="π’πππΌππΎ", callback_data="circle_sticker"
                        )
                    ],
                    [
                        InlineKeyboardButton('π±π°π²πΊ', callback_data='photo')
                    ],
                ]
            ),
        )
    elif query.data == "rotate":
        await query.message.edit_text(
            "**Select the Degree**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="180", callback_data="180"),
                        InlineKeyboardButton(text="90", callback_data="90"),
                    ],
                    [InlineKeyboardButton(text="270", callback_data="270")],
                    ],
                    [
                        InlineKeyboardButton('π±π°π²πΊ', callback_data='photo')
                ]
            ),
        )
    elif query.data == "glitch":
        await query.message.edit_text(
            "**Select required mode**γ€γ€γ€γ€",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="π­ππππΊπ", callback_data="normalglitch"
                        ),
                        InlineKeyboardButton(
                            text="π²πΌπΊπ π«πΊπππ", callback_data="scanlineglitch"
                        ),
                    ],
                    [
                        InlineKeyboardButton('π±π°π²πΊ', callback_data='photo')
                    ]
                ]
            ),
        )
    elif query.data == "normalglitch":
        await query.message.edit_text(
            "**Select Glitch power level**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="1", callback_data="normalglitch1"),
                        InlineKeyboardButton(text="2", callback_data="normalglitch2"),
                        InlineKeyboardButton(text="3", callback_data="normalglitch3"),
                    ],
                    [
                        InlineKeyboardButton(text="4", callback_data="normalglitch4"),
                        InlineKeyboardButton(text="5", callback_data="normalglitch5"),
                    ],
                    [
                        InlineKeyboardButton('π±π°π²πΊ', callback_data='glitch')
                    ],
                ]
            ),
        )
    elif query.data == "scanlineglitch":
        await query.message.edit_text(
            "**Select Glitch power level**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="1", callback_data="scanlineglitch1"),
                        InlineKeyboardButton(text="2", callback_data="scanlineglitch2"),
                        InlineKeyboardButton(text="3", callback_data="scanlineglitch3"),
                    ],
                    [
                        InlineKeyboardButton(text="4", callback_data="scanlineglitch4"),
                        InlineKeyboardButton(text="5", callback_data="scanlineglitch5"),
                    ],
                    [
                        InlineKeyboardButton('π±π°π²πΊ', callback_data='glitch')
                    ],
                ]
            ),
        )
    elif query.data == "blur":
        await query.message.edit(
            "**Select a Type**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="π‘ππ", callback_data="box"),
                        InlineKeyboardButton(text="π­ππππΊπ", callback_data="normal"),
                    ],
                    [InlineKeyboardButton(text="π¦πΊπππππΊπ", callback_data="gas")],
                    ],
                    [
                        InlineKeyboardButton('π±π°π²πΊ', callback_data='photo')
                ]
            ),
        )
    elif query.data == "circle":
        await query.message.edit_text(
            "**Select required mode**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="πΆπππ π‘π¦", callback_data="circlewithbg"),
                        InlineKeyboardButton(text="πΆππππππ π‘π¦", callback_data="circlewithoutbg"),
                    ],
                    [
                        InlineKeyboardButton('π±π°π²πΊ', callback_data='photo')
                    ]
                ]
            ),
        )
    elif query.data == "border":
        await query.message.edit(
            "**Select Border**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="π±πΎπ½", callback_data="red"),
                        InlineKeyboardButton(text="π¦ππΎπΎπ", callback_data="green"),
                    ],
                    [
                        InlineKeyboardButton(text="π‘ππΊπΌπ", callback_data="black"),
                        InlineKeyboardButton(text="π‘πππΎ", callback_data="blue"),
                    ],
                    [
                        InlineKeyboardButton('π±π°π²πΊ', callback_data='photo')   
                    ],
                ]
            ),
        )
    elif query.data == "bright":
        await bright(client, query.message)
    elif query.data == "mix":
        await mix(client, query.message)
    elif query.data == "b|w":
        await black_white(client, query.message)
    elif query.data == "circlewithbg":
        await circle_with_bg(client, query.message)
    elif query.data == "circlewithoutbg":
        await circle_without_bg(client, query.message)
    elif query.data == "green":
        await green_border(client, query.message)
    elif query.data == "blue":
        await blue_border(client, query.message)
    elif query.data == "red":
        await red_border(client, query.message)
    elif query.data == "black":
        await black_border(client, query.message)
    elif query.data == "circle_sticker":
        await round_sticker(client, query.message)
    elif query.data == "inverted":
        await inverted(client, query.message)
    elif query.data == "stkr":
        await sticker(client, query.message)
    elif query.data == "cur_ved":
        await edge_curved(client, query.message)
    elif query.data == "90":
        await rotate_90(client, query.message)
    elif query.data == "180":
        await rotate_180(client, query.message)
    elif query.data == "270":
        await rotate_270(client, query.message)
    elif query.data == "contrast":
        await contrast(client, query.message)
    elif query.data == "box":
        await box_blur(client, query.message)
    elif query.data == "gas":
        await g_blur(client, query.message)
    elif query.data == "normal":
        await normal_blur(client, query.message)
    elif query.data == "sepia":
        await sepia_mode(client, query.message)
    elif query.data == "pencil":
        await pencil(client, query.message)
    elif query.data == "cartoon":
        await cartoon(client, query.message)
    elif query.data == "normalglitch1":
        await normalglitch_1(client, query.message)
    elif query.data == "normalglitch2":
        await normalglitch_2(client, query.message)
    elif query.data == "normalglitch3":
        await normalglitch_3(client, query.message)
    elif query.data == "normalglitch4":
        await normalglitch_4(client, query.message)
    elif query.data == "normalglitch5":
        await normalglitch_5(client, query.message)
    elif query.data == "scanlineglitch1":
        await scanlineglitch_1(client, query.message)
    elif query.data == "scanlineglitch2":
        await scanlineglitch_2(client, query.message)
    elif query.data == "scanlineglitch3":
        await scanlineglitch_3(client, query.message)
    elif query.data == "scanlineglitch4":
        await scanlineglitch_4(client, query.message)
    elif query.data == "scanlineglitch5":
        await scanlineglitch_5(client, query.message)
    elif query.data == "rmbgwhite":
        await removebg_white(client, query.message)
    elif query.data == "rmbgplain":
        await removebg_plain(client, query.message)
    elif query.data == "rmbgsticker":
        await removebg_sticker(client, query.message)
    elif query.data == "photo":
        buttons = [[
            InlineKeyboardButton(text="π‘πππππ", callback_data="bright"),
            InlineKeyboardButton(text="π¬πππΎπ½", callback_data="mix"),
            InlineKeyboardButton(text="π‘ & πΆ", callback_data="b|w"),
            ],[
            InlineKeyboardButton(text="π’πππΌππΎ", callback_data="circle"),
            InlineKeyboardButton(text="π‘πππ", callback_data="blur"),
            InlineKeyboardButton(text="π‘πππ½πΎπ", callback_data="border"),
            ],[
            InlineKeyboardButton(text="π²πππΌππΎπ", callback_data="stick"),
            InlineKeyboardButton(text="π±πππΊππΎ", callback_data="rotate"),
            InlineKeyboardButton(text="π’πππππΊππ", callback_data="contrast"),
            ],[
            InlineKeyboardButton(text="π²πΎπππΊ", callback_data="sepia"),
            InlineKeyboardButton(text="π―πΎππΌππ", callback_data="pencil"),
            InlineKeyboardButton(text="π’πΊπππππ", callback_data="cartoon"),
            ],[
            InlineKeyboardButton(text="π¨πππΎππ", callback_data="inverted"),
            InlineKeyboardButton(text="π¦ππππΌπ", callback_data="glitch"),
            InlineKeyboardButton(text="π±πΎππππΎ π‘π¦", callback_data="removebg")
            ],[
            InlineKeyboardButton(text="π’ππππΎ", callback_data="close_data")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)        
        await query.message.edit_text(        
            text="Select your required mode from below!",
            reply_markup=reply_markup,
            parse_mode='html'
        )








