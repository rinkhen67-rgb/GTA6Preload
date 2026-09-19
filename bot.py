"""
GTA 6 Download Bot — Traffic driver bot.
Sends fake download teasers with inline buttons to redirect users to website.
"""

import asyncio
import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)
from config import (
    BOT_TOKEN,
    WEBSITE_URL,
    FOOTER_TEXT,
    TEASERS,
    FAKE_PROGRESS_STEPS,
)

# ─── Logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ─── Keyboards ─────────────────────────────────────────────────────────────────

def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📥 DOWNLOAD GTA 6 NOW", url=WEBSITE_URL)],
        [
            InlineKeyboardButton("⚡ Fast Mirror", callback_data="mirror"),
            InlineKeyboardButton("🔑 Get Key", callback_data="key"),
        ],
        [
            InlineKeyboardButton("📋 Requirements", callback_data="specs"),
            InlineKeyboardButton("❓ Help", callback_data="help_cb"),
        ],
    ])

def download_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 START DOWNLOAD", url=WEBSITE_URL)],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data="back")],
    ])


# ─── Handlers ──────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Welcome + teaser."""
    user = update.effective_user
    name = user.first_name or "Gamer"

    text = (
        f"🎮 *Welcome, {name}!*\n\n"
        f"You've found the *#1 GTA 6 Download Bot* on Telegram!\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"✅ *Full Game — PC/PS5/Xbox*\n"
        f"✅ *Pre-cracked & Ready to Play*\n"
        f"✅ *All DLC Included*\n"
        f"✅ *Free Forever*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{random.choice(TEASERS)}\n\n"
        f"⬇️ *Tap the button to start your download!*\n"
        f"_{FOOTER_TEXT}_"
    )
    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_keyboard(),
    )
    logger.info("New user: %s (id=%s)", user.username, user.id)


async def cmd_download(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/download — show a teaser + download button."""
    teaser = random.choice(TEASERS)
    text = (
        f"📥 *GTA 6 — DOWNLOAD READY*\n\n"
        f"{teaser}\n\n"
        f"_{FOOTER_TEXT}_"
    )
    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_keyboard(),
    )


async def cmd_progress(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/getlink — animated fake progress then redirect."""
    msg = await update.message.reply_text("⏳ *Preparing your download...*", parse_mode="Markdown")

    for step in FAKE_PROGRESS_STEPS[:-1]:
        await asyncio.sleep(1.2)
        await msg.edit_text(
            f"⏳ *Preparing your download...*\n\n{step}",
            parse_mode="Markdown",
        )

    await asyncio.sleep(1.2)
    await msg.edit_text(
        f"✅ *Download Ready!*\n\n"
        + "\n".join(FAKE_PROGRESS_STEPS)
        + f"\n\n⬇️ *Tap below to start!*\n_{FOOTER_TEXT}_",
        parse_mode="Markdown",
        reply_markup=download_keyboard(),
    )


async def cmd_specs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/specs — show fake system requirements."""
    text = (
        "🖥️ *GTA 6 — PC System Requirements*\n\n"
        "*Minimum:*\n"
        "• OS: Windows 10 64-bit\n"
        "• CPU: Intel i5-9600K / Ryzen 5 3600\n"
        "• RAM: 16 GB\n"
        "• GPU: GTX 1070 / RX 5700\n"
        "• Storage: 95 GB SSD\n\n"
        "*Recommended:*\n"
        "• OS: Windows 11 64-bit\n"
        "• CPU: Intel i9-13900K / Ryzen 9 7900X\n"
        "• RAM: 32 GB\n"
        "• GPU: RTX 4080 / RX 7900 XT\n"
        "• Storage: 95 GB NVMe SSD\n\n"
        f"_{FOOTER_TEXT}_"
    )
    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📥 Download Now", url=WEBSITE_URL)],
        ]),
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/help — command list."""
    text = (
        "📋 *Commands*\n\n"
        "/start — Welcome & first download link\n"
        "/download — Get latest download link\n"
        "/getlink — Auto-generate your download\n"
        "/specs — PC system requirements\n"
        "/help — Show this menu\n\n"
        f"🌐 Direct: {WEBSITE_URL}"
    )
    await update.message.reply_text(text, parse_mode="Markdown")


# ─── Callback Handlers ─────────────────────────────────────────────────────────

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "mirror":
        # Animated progress then link
        await query.edit_message_text("⏳ *Connecting to fast mirror...*", parse_mode="Markdown")
        for step in FAKE_PROGRESS_STEPS[:-1]:
            await asyncio.sleep(1.0)
            await query.edit_message_text(
                f"⏳ *Connecting to fast mirror...*\n\n{step}",
                parse_mode="Markdown",
            )
        await asyncio.sleep(1.0)
        await query.edit_message_text(
            f"🟢 *Mirror Server Connected!*\n\n"
            + "\n".join(FAKE_PROGRESS_STEPS)
            + f"\n\n⬇️ Tap below — link expires in *10 minutes!*\n_{FOOTER_TEXT}_",
            parse_mode="Markdown",
            reply_markup=download_keyboard(),
        )

    elif query.data == "key":
        fake_key = "-".join([
            f"{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5))}"
            for _ in range(5)
        ])
        text = (
            f"🔑 *Your GTA 6 Serial Key:*\n\n"
            f"`{fake_key}`\n\n"
            f"⚠️ *This key is valid for 1 use only!*\n"
            f"Use it during installation on our site.\n\n"
            f"⬇️ Download the game first 👇\n"
            f"_{FOOTER_TEXT}_"
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=download_keyboard(),
        )

    elif query.data == "specs":
        text = (
            "🖥️ *GTA 6 — PC System Requirements*\n\n"
            "*Minimum:*\n"
            "• CPU: Intel i5-9600K / Ryzen 5 3600\n"
            "• RAM: 16 GB\n"
            "• GPU: GTX 1070 / RX 5700\n"
            "• Storage: 95 GB SSD\n\n"
            "*Recommended:*\n"
            "• CPU: Intel i9-13900K / Ryzen 9 7900X\n"
            "• RAM: 32 GB\n"
            "• GPU: RTX 4080 / RX 7900 XT\n"
            "• Storage: 95 GB NVMe\n\n"
            f"_{FOOTER_TEXT}_"
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📥 Download Now", url=WEBSITE_URL)],
                [InlineKeyboardButton("🔙 Back", callback_data="back")],
            ]),
        )

    elif query.data == "help_cb":
        text = (
            "❓ *Need Help?*\n\n"
            "1️⃣ Tap *Download GTA 6 NOW*\n"
            "2️⃣ Complete the verification on our site\n"
            "3️⃣ Download starts automatically!\n\n"
            "📌 *Having issues?*\n"
            f"Visit: {WEBSITE_URL}\n\n"
            f"_{FOOTER_TEXT}_"
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🌐 Visit Website", url=WEBSITE_URL)],
                [InlineKeyboardButton("🔙 Back", callback_data="back")],
            ]),
        )

    elif query.data == "back":
        teaser = random.choice(TEASERS)
        text = (
            f"🎮 *GTA 6 Download — Ready for You!*\n\n"
            f"{teaser}\n\n"
            f"_{FOOTER_TEXT}_"
        )
        await query.edit_message_text(
            text,
            parse_mode="Markdown",
            reply_markup=main_keyboard(),
        )


async def catch_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Any text → teaser + button."""
    teaser = random.choice(TEASERS)
    text = (
        f"🎮 *GTA 6 is waiting for you!*\n\n"
        f"{teaser}\n\n"
        f"⬇️ *Tap below to download now!*\n"
        f"_{FOOTER_TEXT}_"
    )
    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=main_keyboard(),
    )


# ─── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("download", cmd_download))
    app.add_handler(CommandHandler("getlink", cmd_progress))
    app.add_handler(CommandHandler("specs", cmd_specs))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, catch_all))

    logger.info("GTA6 Bot is running... Press Ctrl+C to stop.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    main()
