from discord.ext import commands
from discord import Embed
import datetime as dt

class OnUnfront(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot 
        
    @commands.Cog.listener("on_unfront")
    async def on_unfront(self, member, color, live):
        embed=self.create_front_embed(f"{member} saiu do front...", color, self.bot.get_guild(self.bot.SYSTEM_SERVER).get_member(self.bot.members[member]["dcid"]).avatar.url)
        await self.bot.get_channel(self.bot.FRONT_CHANNEL).send(f"{self.bot.get_channel(self.bot.FRONT_CHANNEL).guild.get_role(1296284550111957092).mention}", embed=embed)
    
    def create_front_embed(self, tittle, color, url):
        embed=Embed(title=tittle, color=color, timestamp=dt.datetime.now())
        embed.set_image(url=url)
        return embed
async def setup(bot):
    await bot.add_cog(OnUnfront(bot))
