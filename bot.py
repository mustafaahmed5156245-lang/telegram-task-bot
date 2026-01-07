from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

tasks = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "Use these commands:\n"
        "/add <task> - Add task\n"
        "/list - Show tasks\n"
        "/delete <number> - Delete task"
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task = " ".join(context.args)
    if task:
        tasks.append(task)
        await update.message.reply_text(f"✅ Task added: {task}")
    else:
        await update.message.reply_text("❌ Please write a task.")

async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not tasks:
        await update.message.reply_text("📭 No tasks found.")
        return

    message = "📝 Your Tasks:\n"
    for i, task in enumerate(tasks, start=1):
        message += f"{i}. {task}\n"

    await update.message.reply_text(message)

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        index = int(context.args[0]) - 1
        removed = tasks.pop(index)
        await update.message.reply_text(f"🗑️ Deleted: {removed}")
    except:
        await update.message.reply_text("❌ Use: /delete <task number>")

def main():
    app = ApplicationBuilder().token("PUT_YOUR_BOT_TOKEN_HERE").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("list", list_tasks))
    app.add_handler(CommandHandler("delete", delete))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
