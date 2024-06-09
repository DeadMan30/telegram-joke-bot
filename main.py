import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

app = Client("joke", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command(["start", "help"]))
async def start(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Owner", url="https://t.me/AliMehdiAbdi"),
                InlineKeyboardButton("Repo", url="https://t.me/")
            ]
        ]
    )
    
    await message.reply_text(
        "Hey There, 👋 It's Joke Teller\n\n"
        "◲ I am a Joke Teller Bot\n"
        "◲ I can Tell You a New Joke Everytime you Send /joke",
        reply_markup=keyboard
    )

@app.on_message(filters.command("joke"))
async def joke(client, message):
    try:
        api_url = "https://v2.jokeapi.dev/joke/Pun?format=txt"
        response = requests.get(api_url)
        if response.status_code == 200:
            joke = response.text
            await message.reply_text(joke)
    except Exception as e:
        await message.reply_text("Sorry, I couldn't fetch a joke right now.")

app.run()
