import discord
from discord.ext import commands
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 1008022746212618330:
        channel = after.channel
        try:
            if before.channel.members == [] and not before.channel.id == 1012189739601899601:
                if before.channel.category_id == 1008022746770448437:
                    await before.channel.delete()
        except:
            pass
    
    if after.channel.id == 1012189739601899601:
        guild = after.channel.guild
        private_channels = discord.utils.get(guild.categories, id=1008022746770448437)
        voice_channel = await guild.create_voice_channel(member.name, category=private_channels)
        await member.move_to(voice_channel)
        await voice_channel.set_permissions(member, connect=True, speak=True, move_mamber=True, manage_roles=True, manage_channels=True, view_channel=True)

client.run("MTAxMjE4ODg0MDU4NjM4NzU5Ng.Gdug7e.Q8kuJpsxLGzM6JqfrZLMvRolxlPv5XzYL8Bm0U")