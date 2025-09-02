# telegram_bot.py

import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your BotFather token (generate a new one if leaked)
TOKEN = "8286212831:AAGWyH20h5wnHtuv-qcVBD1l9pBPCYKO15k"


# --- Command Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text("🤖 This is a test bot who can be optimized.")
    await update.message.reply_text("👋 Hi! I'm your bot. How can I help you?")
    await update.message.reply_text("Give me the /give now type it !!!!!!!!!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when the /help command is issued."""
    await update.message.reply_text(
        "Here are some commands you can use:\n"
        "/start - Welcome message\n"
        "/help - This help menu\n"
        "/give - Sends you a random photo"
    )

async def give_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random photo when /give is used."""
    photos = [
        "https://picsum.photos/400/300",   # random placeholder image
        "https://placekitten.com/400/300", # random kitten
        "https://placebear.com/400/300",   # random bear
        "https://loremflickr.com/400/300", # random flickr photo
    ]

    photo_url = random.choice(photos)
    await update.message.reply_photo(photo_url, caption="📸 Here’s a random photo for you!")


# --- Message Handler ---

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo any non-command text message."""
    await update.message.reply_text(update.message.text)


# --- Main Function ---

def main():
    # Create the bot application
    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("give", give_photo))  # <-- new command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until Ctrl+C is pressed
    print("✅ Bot is running... (test bot, can be optimized)")
    app.run_polling()


if __name__ == "__main__":
    main()
async def give_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random photo when /give is used."""
    photos = [
        "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?w=800",  # Unsplash landscape
        "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=800",  # Unsplash dog
        "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?w=800",  # Unsplash cat
        "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?w=800",  # Unsplash parrot
    ]

    photo_url = random.choice(photos)
    await update.message.reply_photo(photo_url, caption="📸 Here’s a random photo for you!")
