from aiogram import F, Router, Bot
from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER, ChatMemberUpdatedFilter
from aiogram.types import Message, CallbackQuery, ChatMemberUpdated

from const.photo_id import get_random_photo_id

router = Router()

@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def new_member(event: ChatMemberUpdated, bot: Bot):
        random_id = get_random_photo_id()
        await event.answer(f"<b>Helo brother  {event.new_chat_member.user.first_name}."
                           f"Wear a face of yuor leder and be a pert of KEM.ARMY.</b>",
                    parse_mode="HTML")
        await event.answer_photo(random_id)

# @router.message(F.photo)
# async def get_photo_id(message: Message):
#     await message.answer(f'ID фото: {message.photo[-1].file_id}')