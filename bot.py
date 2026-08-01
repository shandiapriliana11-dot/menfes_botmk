from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, GROUP_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Kirim pesan apa saja, nanti akan diteruskan ke grup secara anonim."
    )


async def forward_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == GROUP_ID:
        return

    if update.message.text:
        await context.bot.send_message(
            chat_id=GROUP_ID,
            text=f"📩 MENFESS\n\n{update.message.text}"
        )

        await update.message.reply_text("✅ Menfess berhasil dikirim!")


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, forward_text)
)

app.run_polling()