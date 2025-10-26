import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# ЗАМЕНИТЕ НА ВАШ ТОКЕН ОТ @BotFather
BOT_TOKEN = "8274677913:AAGNvXs-yVqSvJQ7IGhEZJxkQg-BJ_jcBco"

async def start(update: Update, context):
    await update.message.reply_text("🔍 Бот запущен! Напиши что найти.")

async def search(update: Update, context):
    query = update.message.text
    await update.message.reply_text(f"🔍 Ищу: {query}...")
    await update.message.reply_text("✅ Бот работает! Реальный поиск добавлю позже.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))
    print("✅ Бот запущен в Render!")
    app.run_polling()

if __name__ == "__main__":
    main()
