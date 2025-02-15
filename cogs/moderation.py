import discord
from discord.ext import commands
from utils.database import Database

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await self.log_action(ctx.guild.id, f"Пользователь {member} был кикнут. Причина: {reason}")
        await ctx.send(f"{member.mention} был кикнут!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await self.log_action(ctx.guild.id, f"Пользователь {member} был забанен. Причина: {reason}")
        await ctx.send(f"{member.mention} был забанен!")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
        await self.log_action(ctx.guild.id, f"Очищено {amount} сообщений в канале {ctx.channel.name}")

    async def log_action(self, guild_id, message):
        channel_id = self.db.get_log_channel(guild_id)
        if channel_id:
            channel = self.bot.get_channel(channel_id)
            if channel:
                await channel.send(f"[ЛОГ] {message}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
