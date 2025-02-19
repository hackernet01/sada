from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler
import sqlite3

# 🔑 Bot Token from BotFather
BOT_TOKEN = '7679342786:AAGk43ImLwVT-0JTrWnw7wzMAMO38acfIsQ'

# ✅ Function to Verify Key
def check_key(user_key):
    conn = sqlite3.connect("keys.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM premium_keys WHERE key = ? AND status = 'unused'", (user_key,))
    key_data = cursor.fetchone()

    if key_data:
        cursor.execute("UPDATE premium_keys SET status = 'used' WHERE key = ?", (user_key,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

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
        await update.message.reply_text("⚠️ Usage: `/key YOUR_24_DIGIT_KEY`")
        return

    user_key = user_text[1]
    
    if check_key(user_key):
        await update.message.reply_text("✅ Your key is verified! Unlimited access activated. 🔥")
    else:
        await update.message.reply_text("❌ Invalid or already used key!")

# 🚀 Main Function
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("key", verify_key))

    application.run_polling()

if __name__ == "__main__":
    main()
