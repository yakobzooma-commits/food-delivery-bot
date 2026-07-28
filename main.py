import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.effective_user.first_name
    welcome_text = (
        f"ሰላም {user_first_name}! 👋\n\n"
        "ወደ ምግብ ማዘዣ ቦታችን እንኳን በደህና መጡ! 🍔🍕\n"
        "ምን ማዘዝ ይፈልጋሉ?"
    )
    await update.message.reply_text(welcome_text)

def main():
    # Get bot token from environment variables
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN not found!")
        return

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
