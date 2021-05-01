import discord, logging, json
from discord.ext import commands
from discord.utils import get
import os

# Define all variables to be used around the script
description = '''PebbleHost Multicraft Bot'''
bot = commands.Bot(command_prefix='-', description=description)
client = discord.Client()
bot.remove_command("help") # Remove the normal help command
# Setup basic logging for the bot
logging.basicConfig(level=logging.WARNING)
# OGather details for the bots auth, stored 1 directory above in details.txt
f = open("./details.txt","r")
f = f.read()
details=(f.splitlines()[2])
botkey = (details.split("Bot Token: ",1)[1])
details=(f.splitlines()[1])
username = (details.split("Username: ",1)[1])
details=(f.splitlines()[0])
apikey = (details.split("API Key: ",1)[1])
def clear():
	print ("\n\n\n\n\n\n\n")
# Check the supplied API details work with mc.pebblehost.com
result = (os.popen(("php public-php/verifydetails.php ") + (str(username)) + (" ") + (str(apikey))).read())
uname = result.splitlines()
try:
	uname = uname[12]
	uname = (uname.split("[name] => ",1)[1])
except IndexError:
	clear()
	print ("Account details invalid")
	clear()
	quit()
if uname == username:
	print ("Account valid")
else:
	clear()
	print ("Account details invalid")
	clear()
	quit()
# Get the users account ID 
result = (os.popen(("php public-php/verifydetails.php ") + (str(username)) + (" ") + (str(apikey))).read())
uid = result.splitlines()
uid = uid[11]
uid = (uid.split("[id] => ",1)[1])
print (uid)


@bot.event
async def on_ready():
	print ("Ready")
	
	
	print ("Bot booted")
@bot.command(pass_context=True)
async def servers(ctx):
	channel = bot.get_channel(ctx.message.channel.id)
	print ("Servers")
	listofservers = (os.popen(("php public-php/getservers.php ") + (str(username)) + (" ") + (str(apikey)) + (" ") + (str(uid))).read())
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	listofservers = listofservers.splitlines()
	count = 0
	servers = []
	listofservers = listofservers[11:]
	for item in listofservers:
		servers.append(listofservers[(count)])
		count = ((count) + (1))
		if ")" in (listofservers[(count)]):
			break
	server = ""
	noservers = "false"
	serverslist = ""
	for item in servers:
		try:
			serverid = (item[21:])
			serverid = (serverid.split("]",1)[0])
			servername = (item[21:])
			servername = (servername.split("=> ",1)[1])
			servernameid = ((serverid) + (" | ") + (servername))
			print (servernameid)
			serverslist = ((serverslist) + (servernameid) + ("\n"))
		except IndexError:
			await channel.send(":x: You have no active servers.")
			noservers = "true"
			break
	if noservers == "false":
		await channel.send (("__**Server ID | Server Name**__\n") + (serverslist) + ("\nUse `-server {name}` for details on a specific server"))
		
@bot.command(pass_context=True)
async def server(ctx):
	channel = bot.get_channel(ctx.message.channel.id)
	try:
		checkerblank = ctx.message.content[8]
	except IndexError:
		await channel.send(":x: Usage: -server {serverid}")
		return
	requestedsrv = (ctx.message.content[8:])
	print (requestedsrv)
	listofservers = (os.popen(("php public-php/getservers.php ") + (str(username)) + (" ") + (str(apikey)) + (" ") + (str(uid))).read())
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	listofservers = listofservers.splitlines()
	count = 0
	servers = []
	listofservers = listofservers[11:]
	for item in listofservers:
		servers.append(listofservers[(count)])
		count = ((count) + (1))
		if ")" in (listofservers[(count)]):
			break
	serverslist = []
	for item in servers:
		try:
			serverid = (item[21:])
			serverid = (serverid.split("]",1)[0])
			serverslist.append(serverid)
		except IndexError:
			print ("No active servers")
	print (serverslist)
	if requestedsrv in serverslist:
		print ("Server is owned by the correct user and is valid")
	else:
		print ("Server is invalid, Exiting now")
		await channel.send(":x: This server appears to be invalid")
		return
	result = (os.popen(("php public-php/resources.php ") + (str(username)) + (" ") + (str(apikey)) + (" ") + (str(requestedsrv))).read())
	stats = result.splitlines()
	count = 0
	cpumem = []
	stats = stats[9:]
	for item in stats:
		if "[quota]" in (stats[(count)]):
			break
		cpumem.append(stats[(count)])
		count = ((count) + (1))
	cpuusage = cpumem[0]
	cpuusage = (cpuusage.split("=> ",1)[1])
	ramusage = cpumem[1]
	ramusage = (ramusage.split("=> ",1)[1])
	cpuusage = round((float(cpuusage)), 2)
	ramusage = round((float(ramusage)), 2)
	result = (os.popen(("php public-php/getserverstatus.php ") + (str(username)) + (" ") + (str(apikey)) + (" ") + (str(requestedsrv))).read())
	status = result.splitlines()
	count = 0
	details = []
	status = status[9:]
	for item in status:
		if ")" in (status[(count)]):
			break
		details.append(status[(count)])
		count = ((count) + (1))
	onlineoffline = details[0]
	onlineoffline = (onlineoffline.split("=> ",1)[1])
	if onlineoffline == "online":
		onlineoffline = "Online"
	elif onlineoffline == "offline":
		onlineoffline = "Offline"
	onlineplayers = details[1]
	onlineplayers = (onlineplayers.split("=> ",1)[1])
	maxplayers = details[2]
	maxplayers = (maxplayers.split("=> ",1)[1])
	
	
	result = (os.popen(("php public-php/getserver.php ") + (str(username)) + (" ") + (str(apikey)) + (" ") + (str(requestedsrv))).read())
	maxram = result.splitlines()
	print (maxram)
	maxrama = maxram[15]
	daemonram = maxram[15]
	maxramaa = (maxrama.split("=> ",1)[1])
	maxramaa = (int(maxramaa) / 1024)
	maxramaa = (int(maxramaa))
	
	playerdetails = (("`\nMax RAM: `") + str(maxramaa) + ("GB`\nPlayers: `") + (onlineplayers) + ("/") + (maxplayers) + ("`"))
	
	await channel.send(("Server ID `")+(requestedsrv)+("`\nStatus: `")+str(onlineoffline)+("`\nCPU usage: `")+str(cpuusage)+("%`\nRAM usage: `")+str(ramusage)+("%") + (playerdetails))
		

if __name__ == '__main__':
	bot.run((str(botkey)))