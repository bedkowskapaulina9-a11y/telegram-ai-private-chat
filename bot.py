from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "TU_WKLEJ_TOKEN_Z_BOTFATHERA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💋 Witaj w prywatnym czacie Paulina AI 24/7.\n\n"
        "Napisz do mnie… jestem tylko dla Ciebie 😈"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "cześć" in text or "hej" in text:
        reply = "Hej kotku 😘 co dziś robimy?"
    elif "co robisz" in text:
        reply = "Myślę o Tobie… i czekam na Twoją wiadomość 💋"
    else:
        reply = "Mmm… napisz mi więcej 😈"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
