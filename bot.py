import discord
from discord.ext import commands
from discord import app_commands
import os  # <-- ADDED to import os

OWNER_ID = 1348238462352097332

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"❌ Sync error: {e}")

@bot.tree.command(name="send", description="Send a message to any channel")
@app_commands.describe(channel="Select the channel", message="The message to send")
async def send(interaction: discord.Interaction, channel: discord.TextChannel, message: str):
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message("❌ You are not allowed to use this command.", ephemeral=True)
        return

    try:
        await channel.send(message)
        await interaction.response.send_message(f"✅ Sent your message to {channel.mention}", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"❌ Failed to send message: {e}", ephemeral=True)

# 🚀 Start the bot using token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
