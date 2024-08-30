import aiohttp


async def check_spelling(text: str):
    """
    Функция для поиска ошибок в тексте заметки.

    :param text: Текст заметки.
    :return: Список ошибок.
    """
    api_url = "https://speller.yandex.net/services/spellservice.json/checkText"
    params = {
        "text": text,
        "option": 526,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url, params=params) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Ошибка проверки орфографии: {response.status}")
