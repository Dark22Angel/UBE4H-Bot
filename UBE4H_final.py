#imports
import discord
from discord.ext import commands
import time 
import random
import recueil_de_poesie



#variables

intents = discord.Intents().all()

bot = commands.Bot(command_prefix="", intents = intents)

intents.message_content = True
intents.guilds = True
intents.members = True

#-------------------- on récupère le token
with open("token1.txt","r",encoding="utf-8") as fichier :
    token= fichier.readline()

client= discord.Client()

#variable
motinterdit= "darkangel","mathurus"

#quand le bot se connect au serveur
@bot.event
async def on_ready():
    channel = discord.utils.get(bot.get_all_channels(), name="général")
    await bot.get_channel(channel.id).send("Bonjour jeunes forgerons, je suis votre maître et vous allez faire tout ce que je vous dit de faire. 🙂 lol c'était une boutadeu ;)")
    await bot.get_channel(channel.id).send(f"Mot interdie:{motinterdit} sans de majuscule !!")

#En cas d'erreur
@bot.event
async def on_command_error(ctx,error):
    """Définit la réaction du bot en cas d'erreur"""
    if isinstance(error,commands.CommandNotFound):
        await ctx.reply("Mes Maitres, Sa Sainteté Lweem et Sa Sainteté Mathurus, ne m'ont pas encore programmé pour réagir à cela. Faut pas tout vouloir tout de suite, impatient va.")
    else :
        raise error

#En cas de mot interdit
@bot.command(name="salut")
async def salut(ctx):
    """Définit la réaction du bot si on dit 'salut'"""
    reponse=f"Tu te crois à la fête de l'huma, {ctx.message.author.name}? Ou chez mémé? T'as intérêt à montrer un peu plus de respect, ou je te vire."
    await ctx.reply(reponse)
    print(f"Réponse à message {ctx.message.id} : {reponse}")
@bot.command(name="mathurus")
async def mathurus(ctx):
    compteur=6
    reponse=f"Comment oses-tu! Pour la peine, espèce de gueux, tu retoures d'où tu viens!"
    while compteur>1:
        compteur -=1
    await ctx.channel.send(compteur)
    time.sleep(1)
    await ctx.author.kick(reason="Insulte")

@bot.command(name="hello")
async def salut(ctx):
    """Définit la réaction du bot si on dit 'salut'"""
    reponse=f"Arrête de dire ça {ctx.message.author.name} ou tu vas rejoindre la reine d'Angleterre!UwU"
    await ctx.reply(reponse)
    print(f"Réponse à message {ctx.message.id} : {reponse}")

@bot.command(name="salam")
async def salam(ctx):
    reponseasalam=f"Salam, bienvenue chez Air OQTF,, des avions pleins à l'aller, vides au retour. (Vols uniquement en direction du magrehb et de tchétchénie)"

#reponse au message envoyer
@bot.command(name="Bonjour")

async def Bonjour(ctx):
    # récupère le nom de celui qui vient d'envoyer le message, l'insère dans une phrase, et stocke ça dans la variable reponse.
    reponse= f"Sâle paysan on ta pas appris la pollitesse {ctx.message.author.name} ? Ici on dit: BONDOURAN !!!!!!"
    await ctx.reply(reponse)
    print(f"Réponse à message {ctx.message.id} : {reponse}")

@bot.command(name="darkangel")
async def darkangel(ctx):
    compteur=6 
    await ctx.channel.send(f"Comment peux tu oser pronnoncer ce nom sans majuscule {ctx.message.author.name} ? Tu mérite un kick !! ;)")
    await ctx.channel.send("Tu sera renvoyer dans ton pays dans:")
    while compteur>1:
        await ctx.channel.send(compteur)
        time.sleep(1)
    await ctx.author.kick(reson="Mot interdit ;)")

# déconnexion
@bot.command(name="exit")
async def exit(ctx):
    reponse="Le seigneur bot est déconnecter pour une indéterminé, adieu bande de sac à merde enflouie sous ton arrière grand mère qui est insinéré 😉 " 
    await ctx.reply(reponse)
    await bot.close()
    print(f"Reponse à message {ctx.message.id} : {reponse}")

@bot.command(name="coucou")
async def coucou(ctx):
    acceuil= recueil_de_poesie.creer_une_insulte()
    await ctx.reply(acceuil)
    print(f"Bonjour voici quelques formules de politesses: {acceuil}.")

@bot.command(name="BONDOURAN")
async def BONDOURAN(ctx):
    reponse= "Ici on ne dit pas BONDOURAN mais: salam"
    await ctx.reply(reponse)
    print(f"reponse à message {ctx.message.id} : {reponse}") 
    
       



bot.run("token1.txt")