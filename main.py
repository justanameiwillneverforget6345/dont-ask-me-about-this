import discord
import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix='h!')

static void UpdatePresence()
{
    DiscordRichPresence discordPresence;
    memset(&discordPresence, 0, sizeof(discordPresence));
    discordPresence.state = "Playing Solo";
    discordPresence.details = "Competitive";
    discordPresence.startTimestamp = 1507665886;
    discordPresence.endTimestamp = 1507665886;
    discordPresence.largeImageText = "Numbani";
    discordPresence.smallImageText = "Rogue - Level 100";
    discordPresence.partyId = "ae488379-351d-4a4f-ad32-2b9b01c91657";
    discordPresence.partySize = 1;
    discordPresence.partyMax = 5;
    discordPresence.joinSecret = "MTI4NzM0OjFpMmhuZToxMjMxMjM= ";
    Discord_UpdatePresence(&discordPresence);
}

@bot.event
async def on_ready():
	#await bot.change_presence(game=discord.Game(name="Making a    bot"))
	guild_count = 0
	for guild in bot.guilds:
		print(f"Server ID: - {guild.id} Name: - {guild.name}")
		
		guild_count = guild_count + 1
	print("Hirotu is in " + str(guild_count) + " guilds.")
	print(f'Bot connected as {bot.user}')
	
@bot.event
async def on_message(message):
	if message.content == "test":
		await message.channel.send("Testing 1 2 3")
bot.run("NjU1NDc1ODY0OTQ3MTMwMzk5.XfUpeA.-NiRbATkrhrPP8w4Ju2fqOib6dQ")