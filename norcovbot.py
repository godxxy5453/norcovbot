# -*- coding:utf-8 -*-

import discord, asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("야끼런"))
    print("준비됐다이기") #준비
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    #맵

    if message.content == "!맵이름":
        await message.channel.send("ex) ```!커스텀 !인터체인지 처럼 맵 이름을 입력해라 이기```")

    if message.content == "!커스텀":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683360890376159282/custom.jpg")

    if message.content == "!우드":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683360854057549843/1582904309.jpg")

    if message.content == "!인터체인지":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683360878137311297/1582995805.jpg")

    if message.content == "!리저브":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683360866787524618/1582995782.jpg")

    if message.content == "!해안선":
        await message.channel.send("https://cdn.discordapp.com/attachments/682958432675823708/682974731884167230/20200228_012656.png")

    if message.content == "!팩토리":
        await message.channel.send("https://forum.escapefromtarkov.com/uploads/monthly_2017_08/Tarkin_v4_+tunels_Factory.jpg.686b65ccd9f64f83144e0ed3fe6ab98a.jpg")

    #eng

    if message.content == "!custom":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683360890376159282/custom.jpg")

    if message.content == "!wood":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683360854057549843/1582904309.jpg")

    if message.content == "!interchange":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683360878137311297/1582995805.jpg")

    if message.content == "!reserve":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683360866787524618/1582995782.jpg")

    if message.content == "!shoreline":
        await message.channel.send("https://cdn.discordapp.com/attachments/682958432675823708/682974731884167230/20200228_012656.png")

    if message.content == "!factory":
        await message.channel.send("https://forum.escapefromtarkov.com/uploads/monthly_2017_08/Tarkin_v4_+tunels_Factory.jpg.686b65ccd9f64f83144e0ed3fe6ab98a.jpg")

    #일반1

    if message.content == "!치료":
        await message.channel.send("https://cdn.discordapp.com/attachments/682230933600206959/682669173704491018/viewimage.png")

    if message.content == "!회복":
        await message.channel.send("https://cdn.discordapp.com/attachments/682230933600206959/682669173704491018/viewimage.png")

    if message.content == "!가성비":
        await message.channel.send("https://cdn.discordapp.com/attachments/682956969614639270/682957887563235410/1582820723.png")

    if message.content == "!매크로":
        await message.channel.send("http://m.dcinside.com/board/eft/77389")

    if message.content == "!보스":
        await message.channel.send("https://gall.dcinside.com/m/eft/33381")
    
    if message.content == "!방어구":
        await message.channel.send("https://gall.dcinside.com/m/eft/115289")
    
    if message.content == "!시세":
        await message.channel.send("https://tarkov-market.com/")

    if message.content == "!파밍":
        await message.channel.send("https://gall.dcinside.com/m/eft/5033")

    if message.content == "!그래픽":
        await message.channel.send("https://gall.dcinside.com/m/eft/627")

    if message.content == "!피라미드":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/683371493115166777/pramid.png")

    if message.content == "!케이스":
        await message.channel.send("https://gall.dcinside.com/mgallery/board/view/?id=eft&no=15835")

    if message.content == "!스킬":
        await message.channel.send("https://namu.wiki/w/Escape%20from%20Tarkov/%EC%8B%9C%EC%8A%A4%ED%85%9C#s-5")

    if message.content == "!스킬작":
        await message.channel.send("https://gall.dcinside.com/m/eft/34405")

    if message.content == "!시스템":
        await message.channel.send("https://namu.wiki/w/Escape%20from%20Tarkov/%EC%8B%9C%EC%8A%A4%ED%85%9C")

    if message.content == "!은신처":
        await message.channel.send("https://namu.wiki/w/Escape%20from%20Tarkov/%EC%8B%9C%EC%8A%A4%ED%85%9C#s-3")

    if message.content == "!퀘스트":
        await message.channel.send("https://escapefromtarkov.gamepedia.com/Quests")

    


    

    if message.content == "!북미":
        await message.channel.send("https://drive.google.com/file/d/1eo70IxUzy4mcKJBdCaK060ihwdLBXsq_/view?usp=sharing ```구글 드라이브에서 html파일을 받고\nC:Battlestate Games/BsgLauncher/Content 폴더에 붙여넣기 (게임 설치한 폴더위치가 다르면 거기로)\n서버는 캘리보니아랑 워싱턴DC```")

    if message.content == "!서버":
        await message.channel.send("https://drive.google.com/file/d/1eo70IxUzy4mcKJBdCaK060ihwdLBXsq_/view?usp=sharing ```구글 드라이브에서 html파일을 받고\nC:Battlestate Games/BsgLauncher/Content 폴더에 붙여넣기 (게임 설치한 폴더위치가 다르면 거기로)\n서버는 캘리보니아랑 워싱턴DC```")

    if message.content == "!북미서버":
        await message.channel.send("https://drive.google.com/file/d/1eo70IxUzy4mcKJBdCaK060ihwdLBXsq_/view?usp=sharing ```구글 드라이브에서 html파일을 받고\nC:Battlestate Games/BsgLauncher/Content 폴더에 붙여넣기 (게임 설치한 폴더위치가 다르면 거기로)\n서버는 캘리보니아랑 워싱턴DC```")

    if message.content == "!탄약":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/686210996603453440/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211012428693524/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211031445667840/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211046196903936/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211059912015973/viewimage.png")
       
    if message.content == "!관통":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/686210996603453440/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211012428693524/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211031445667840/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211046196903936/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211059912015973/viewimage.png")
        
    if message.content == "!총알":
        await message.channel.send("https://cdn.discordapp.com/attachments/683360793215238307/686210996603453440/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211012428693524/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211031445667840/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211046196903936/viewimage.png\nhttps://cdn.discordapp.com/attachments/683360793215238307/686211059912015973/viewimage.png")    
     
    
    
    #일반2
    

    if message.content == "!갤러리":
        await message.channel.send("https://gall.dcinside.com/mgallery/board/lists?id=eft")

    if message.content == "!리버슨":
        await message.channel.send("https://cdn.discordapp.com/attachments/682958432675823708/682958951934984245/e281528289554a77.png")

    if message.content == "!커슨텀":
        await message.channel.send("https://cdn.discordapp.com/attachments/682958432675823708/682958887162347606/a2d4624767fb9359.png")

    if message.content == "!해안슨":
        await message.channel.send("https://cdn.discordapp.com/attachments/682958432675823708/682974731884167230/20200228_012656.png")

    if message.content == "@노무현":
        await message.channel.send("저는 살아있습니다")



    #ㅇㅂ

    if message.content == "!응디":
        await message.channel.send("흔드르라 이기야")

    if message.content == "!응디시티":
        await message.channel.send("https://www.youtube.com/watch?v=vYibVU6Wbas")

    if message.content == "하아":
        await message.channel.send("언조비카이~")

    if message.content == "하아~":
        await message.channel.send("언조비카이~")
    
    if message.content == "하아~!":
        await message.channel.send("언조비카이~")
    
    if message.content == "노무현":
        await message.channel.send("예아")
    
    if message.content == "7퍼센트 못해서":
        await message.channel.send("죄송합니다")
    
    if message.content == "7% 못해서":
        await message.channel.send("죄송합니다")

    if message.content == "우흥":
        await message.channel.send(":owl:")

    if message.content == "우흥~":
        await message.channel.send(":owl:")

    if message.content == "우흥우흥":
        await message.channel.send(":owl::owl:")

    if message.content == "노알라":
        await message.channel.send(":koala:")

    if message.content == "북딱슨":
        await message.channel.send(":koala:")

    if message.content == "예아":
        await message.channel.send("안될거 뭐있노?")

    if message.content == "북딱슨":
        await message.channel.send(":koala:")

    
    #디시콘(test)

    if message.content == "~글카":
        await message.channel.send("https://cdn.discordapp.com/attachments/684157019258748946/684158796947390620/icon_18.png")

    if message.content == "~서버":
        await message.channel.send("https://cdn.discordapp.com/attachments/684157019258748946/684158836029915165/icon_21.gif")

    if message.content == "~니키타":
        await message.channel.send("https://cdn.discordapp.com/attachments/684157019258748946/684158865163681883/icon_25.gif")
    


    #help

    if message.content == "양숙아":
        await message.channel.send("```!맵이름, !치료, !회복, !가성비, !매크로, !보스, !방어구, !시세, !파밍, !그래픽, !피라미드, !케이스, !북미, !서버, !스킬, !스킬작, !시스템, !은신처, !퀘스트```")

    if message.content == "무현아":
        await message.channel.send("```!맵이름, !치료, !회복, !가성비, !매크로, !보스, !방어구, !시세, !파밍, !그래픽, !피라미드, !케이스, !북미, !서버, !스킬, !스킬작, !시스템, !은신처, !퀘스트```")

    if message.content == "노무쿤":
        await message.channel.send("```!맵이름, !치료, !회복, !가성비, !매크로, !보스, !방어구, !시세, !파밍, !그래픽, !피라미드, !케이스, !북미, !서버, !스킬, !스킬작, !시스템, !은신처, !퀘스트```")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
