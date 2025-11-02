import telebot
import openai
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def generate_image(message):
    try:
        prompt = message.text
        bot.send_message(message.chat.id, "🎨 Creating your image, please wait...")

        result = openai.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_url = result.data[0].url
        bot.send_photo(message.chat.id, image_url)

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")

bot.polling()
