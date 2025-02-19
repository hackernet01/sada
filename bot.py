from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

# 🔑 Fixed Premium Key
PREMIUM_KEY = "H123acker!!N#t!2wTreHHok"

# 🔹 Telegram Bot Token (Replace with your bot's token)
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

# 📌 Start Command
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("🐍 WORM GPT 🐍", callback_data="worm_gpt"),
         InlineKeyboardButton("💰 CREDIT 💰", callback_data="credit")],
        [InlineKeyboardButton("🔑 BUY PREMIUM KEY 🔑", url="https://t.me/HackerNet0101")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("👋 Welcome to Hackernet Bot!", reply_markup=reply_markup)

# 🔑 Key Activation
async def verify_key(update: Update, context):
    user_text = update.message.text.split()

    if len(user_text) < 2:
        await update.message.reply_text("⚠️ Usage: `/key YOUR_KEY`")
        return

    user_key = user_text[1]
    
    if user_key == PREMIUM_KEY:
        await update.message.reply_text("✅ Key Verified! Unlimited Access Activated. 🔥")
    else:
        await update.message.reply_text("❌ Invalid Key! Buy from @HackerNet0101")

# 🚀 Main Function
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("key", verify_key))

    application.run_polling()

if __name__ == "__main__":
    main()
