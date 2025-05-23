import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Read token from environment variable
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("No TOKEN found! Please set the TOKEN environment variable.")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton("💻 Programming in C"), KeyboardButton("☕ Programming in Java")],
        [KeyboardButton("🛡️ Bug Bounty Hacking"), KeyboardButton("🚀 Problem Solving with C++")],
        [KeyboardButton("🌐 Javascript Full Course"), KeyboardButton("📚 Free Books")],
        [KeyboardButton("🏅 Certificate Courses"), KeyboardButton("🐍 Download Python Course")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("👋 Welcome! Please choose a category:", reply_markup=reply_markup)

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()

    if "programming in c" in text:
        msg = "📘 **C Programming Course**\nLearn the basics of C programming language from scratch."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/DownloadUdemyCProgramming.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "programming in java" in text:
        msg = "☕ **Java Programming Course**\nMaster Java programming with this free Udemy course."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/udemy-java-programming-free-course.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "problem solving with c++" in text:
        msg = "🚀 **Problem Solving with C++**\nSharpen your logical thinking using C++."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/problem-solving-with-c-programming.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "python course" in text or "download python course" in text:
        msg = "🐍 **Python Programming Course**\nMaster your Python skills with this free course."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2025/05/master-your-skills-with-free-python.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "free books" in text:
        await update.message.reply_text("📚 Book uploads are coming soon! Stay tuned...")

    elif "certificate courses" in text:
        await update.message.reply_text("🏅 Get daily certificate courses!\nJoin our Telegram channel: https://t.me/OmegaOfTS")

    # Bug Bounty submenu
    elif "bug bounty hacking" in text:
        keyboard = [
            [KeyboardButton("📖 Complete Hacking Guide"), KeyboardButton("📍 Web Hacking")],
            [KeyboardButton("📱 Android Hacking"), KeyboardButton("💥 Offensive Bug Bounty")],
            [KeyboardButton("🧰 Burp Suite Guide"), KeyboardButton("🔙 Back to Main Menu")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("💥 Choose a Bug Bounty course:", reply_markup=reply_markup)

    elif "complete hacking guide" in text:
        msg = "📖 **Bug Bounty Hunting Guide**\nA complete guide to bug bounty hunting."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/free-download-bug-bounty-hunting-guide.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "web hacking" in text:
        msg = "📍 **Bug Bounty Web Hacking**\nBecome a pro at web hacking with this course."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/bug-bounty-web-hacking-become-web.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "android hacking" in text:
        msg = "📱 **Bug Bounty Android Hacking**\nMaster Android hacking for bug bounty."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/bug-bounty-android-hacking-master-art.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "offensive bug bounty" in text:
        msg = "💥 **Offensive Bug Bounty Approach**\nLearn offensive strategies in bug bounty."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/bug-bounty-hunting-offensive-approach.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "burp suite" in text:
        msg = "🧰 **Burp Suite Guide**\nA detailed guide on using Burp Suite for bug bounty."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/burp-suite-bug-bounty-web-hacking-from.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    # Javascript submenu
    elif "javascript full course" in text:
        keyboard = [
            [KeyboardButton("📘 JS Part 1"), KeyboardButton("📗 JS Part 2")],
            [KeyboardButton("📙 JS Part 3"), KeyboardButton("🔙 Back to Main Menu")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("📚 JavaScript Course Parts:", reply_markup=reply_markup)

    elif "js part 1" in text:
        msg = "📘 **JavaScript Part 1**\nBeginner to advanced JavaScript fundamentals."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/javascript-beginners-to-advance-course.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "js part 2" in text:
        msg = "📗 **JavaScript Part 2**\nAdvanced JavaScript concepts and techniques."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/part-2-javascript-beginners-to-advance.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "js part 3" in text:
        msg = "📙 **JavaScript Part 3**\nDeep dive into JavaScript best practices."
        button = InlineKeyboardMarkup.from_button(
            InlineKeyboardButton("📥 Click Here to Download", url="https://www.omegaofts.news/2024/11/javascript-beginners-to-advance-course_21.html")
        )
        await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=button)

    elif "back to main menu" in text:
        await start(update, context)

    else:
        await update.message.reply_text("❌ Please choose a valid option from the keyboard.")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
