from VILLAIN_MUSIC.misc import SUDOERS
from VILLAIN_MUSIC.utils.database import get_lang, is_maintenance
from strings import get_string

def language(mystic):
    async def wrapper(_, message, **kwargs):
        # Maintenance check
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} is under maintenance, visit <a href={SUPPORT_CHAT}>support chat</a> for more info.",
                    disable_web_page_preview=True,
                )

        # Try to delete the message if possible
        try:
            await message.delete()
        except:
            pass

        # Load language safely
        try:
            lang_code = await get_lang(message.chat.id)
            language_strings = get_string(lang_code)
        except:
            language_strings = get_string("en")  # fallback to English

        return await mystic(_, message, language_strings)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        # Maintenance check
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"{app.mention} is under maintenance, visit support chat for more info.",
                    show_alert=True,
                )

        # Load language safely
        try:
            lang_code = await get_lang(CallbackQuery.message.chat.id)
            language_strings = get_string(lang_code)
        except:
            language_strings = get_string("en")  # fallback to English

        return await mystic(_, CallbackQuery, language_strings)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            lang_code = await get_lang(message.chat.id)
            language_strings = get_string(lang_code)
        except:
            language_strings = get_string("en")  # fallback to English

        return await mystic(_, message, language_strings)

    return wrapper
