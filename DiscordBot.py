import discord
import requests
import random


def read_token():
    with open('token.txt', 'r') as read1:
        lines = read1.readlines()
        return lines[0].strip()


def read_key():
    with open('steam_key.txt', 'r') as read2:
        lines = read2.readlines()
        return lines[0].strip()


token = read_token()
key = read_key()
client = discord.Client()


async def on_message(message):
    user = f"{message.author.name}"



    if message.content.find("!csgostats") != -1:
        player_id = message.content[11:]

        url_id = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + key + "&vanityurl=" + str(player_id)
        id_get = requests.get(url_id)
        if id_get.status_code == 200:
            id = id_get.json()
            if id["response"]["success"] == 1:
                real_id = id["response"]["steamid"]

                url_name = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + key + "&steamids=" + real_id
                name_get = requests.get(url_name)
                name = name_get.json()

                url_data = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=" + key + "&steamid=" + real_id
                data_get = requests.get(url_data)

                if data_get.status_code == 200:
                    player_name = name["response"]["players"][0]["personaname"]
                    player_picture = name["response"]["players"][0]["avatarfull"]
                    data = data_get.json()
                    total_kills = data["playerstats"]['stats'][0]["value"]
                    total_deaths = data["playerstats"]['stats'][1]["value"]
                    kill_death_ratio = total_kills / total_deaths
                    total_time = data["playerstats"]['stats'][2]["value"]
                    total_time_hours = total_time / 60 / 60
                    total_bombs_planted = data["playerstats"]['stats'][3]["value"]
                    total_defused_bombs = data["playerstats"]['stats'][4]["value"]
                    total_wins = data["playerstats"]['stats'][5]["value"]
                    total_damage_done = data["playerstats"]['stats'][6]["value"]
                    total_money_earned = data['playerstats']['stats'][7]['value']
                    total_knife_kills = data['playerstats']['stats'][8]['value']
                    total_headshots = data['playerstats']['stats'][24]['value']
                    # Because there is a list inside the dictionary, use [0] and such to navigate which list and in turn which key & value

                    embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** stats:",
                                          color=discord.Colour.blue())
                    embed.set_thumbnail(url=player_picture)
                    embed.add_field(name="**Kills & Deaths**", value="Kills: " + str(total_kills) +
                                    "   Deaths: " + str(total_deaths) +
                                    "   K/D: " + str(kill_death_ratio),inline=False)
                    embed.add_field(name="**Bombs**", value="Bombs Planted: " + str(total_bombs_planted) +
                                                            "            Bombs Defused: " + str(total_defused_bombs),inline=False)
                    embed.add_field(name="**Wins**", value="Has " + str(total_wins) + " wins!", inline=False)
                    embed.add_field(name="**Other Stats**", value="Has played " + str(total_time_hours) + " hours!\n"
                                    "Has " + str(total_knife_kills) + " kills with the knife!\n"
                                    "Has done " + str(total_damage_done) + " damage.\n"
                                    "Has earned $" + str(total_money_earned) + "!\n"
                                    "Has a total of " + str(total_headshots) + " headshots!")

                    await message.channel.send(embed=embed)
                elif data_get.status_code == 500:
                    embed = discord.Embed(title="Sorry " + user + " - Player does not exist or profile is private so we can't access it. (╯°□°）╯︵ ┻━┻")
                    embed.set_thumbnail(url="https://www.publicdomainpictures.net/pictures/40000/nahled/question-mark.jpg")
                    await message.channel.send(embed=embed)
                    # Because steam changed their privacy settings, go into your profile settings and make everything public
            elif id["response"]["success"] == 42:
                url_name = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + key + "&steamids=" + player_id
                name_get = requests.get(url_name)
                name = name_get.json()

                url_data = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=" + key + "&steamid=" + player_id
                data_get = requests.get(url_data)

                if data_get.status_code == 200:
                    player_name = name["response"]["players"][0]["personaname"]
                    player_picture = name["response"]["players"][0]["avatarfull"]
                    data = data_get.json()
                    total_kills = data["playerstats"]['stats'][0]["value"]
                    total_deaths = data["playerstats"]['stats'][1]["value"]
                    kill_death_ratio = total_kills / total_deaths
                    total_time = data["playerstats"]['stats'][2]["value"]
                    total_time_hours = total_time / 60 / 60
                    total_bombs_planted = data["playerstats"]['stats'][3]["value"]
                    total_defused_bombs = data["playerstats"]['stats'][4]["value"]
                    total_wins = data["playerstats"]['stats'][5]["value"]
                    total_damage_done = data["playerstats"]['stats'][6]["value"]
                    total_money_earned = data['playerstats']['stats'][7]['value']
                    total_knife_kills = data['playerstats']['stats'][8]['value']
                    total_headshots = data['playerstats']['stats'][24]['value']
                    # Because there is a list inside the dictionary, use [0] and such to navigate which list and in turn which key & value
                    embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** stats:",
                                          color=discord.Colour.blue())
                    embed.set_thumbnail(url=player_picture)
                    embed.add_field(name="**Kills & Deaths**", value="Kills: " + str(total_kills) +
                                    "   Deaths: " + str(total_deaths) +
                                    "   K/D: " + str(kill_death_ratio), inline=False)
                    embed.add_field(name="**Bombs**", value="Bombs Planted: " + str(total_bombs_planted) +
                                    "            Bombs Defused: " + str(total_defused_bombs), inline=False)
                    embed.add_field(name="**Wins**", value="Has " + str(total_wins) + " wins!", inline=False)
                    embed.add_field(name="**Other Stats**", value="Has played " + str(total_time_hours) + " hours!\n"
                                    "Has " + str(total_knife_kills) + " kills with the knife!\n"
                                    "Has done" + str(total_damage_done) + " damage.\n"
                                    "Has earned $" + str(total_money_earned) + "!\n"
                                    "Has a total of " + str(total_headshots) + " headshots!")

                    await message.channel.send(embed=embed)



                elif data_get.status_code == 500:
                    embed = discord.Embed(title="Sorry" + user + " - Player does not exist or profile is private so we can't access it. (╯°□°）╯︵ ┻━┻")
                    embed.set_thumbnail(url="https://www.publicdomainpictures.net/pictures/40000/nahled/question-mark.jpg")
                    await message.channel.send(embed=embed)
                    # Because steam changed their privacy settings, go into your profile settings and make everything public
        elif id_get.status_code == 500:
            url_name = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + key + "&steamids=" + player_id
            name_get = requests.get(url_name)
            name = name_get.json()

            url_data = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=" + key + "&steamid=" + player_id
            data_get = requests.get(url_data)

            if data_get.status_code == 200:
                player_name = name["response"]["players"][0]["personaname"]
                player_picture = name["response"]["players"][0]["avatarfull"]
                data = data_get.json()
                total_kills = data["playerstats"]['stats'][0]["value"]
                total_deaths = data["playerstats"]['stats'][1]["value"]
                kill_death_ratio = total_kills / total_deaths
                total_time = data["playerstats"]['stats'][2]["value"]
                total_time_hours = total_time / 60 / 60
                total_bombs_planted = data["playerstats"]['stats'][3]["value"]
                total_defused_bombs = data["playerstats"]['stats'][4]["value"]
                total_wins = data["playerstats"]['stats'][5]["value"]
                total_damage_done = data["playerstats"]['stats'][6]["value"]
                total_money_earned = data['playerstats']['stats'][7]['value']
                total_knife_kills = data['playerstats']['stats'][8]['value']
                total_headshots = data['playerstats']['stats'][24]['value']
                # Because there is a list inside the dictionary, use [0] and such to navigate which list and in turn which key & value
                embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** stats:",
                                      color=discord.Colour.blue())
                embed.set_thumbnail(url=player_picture)
                embed.add_field(name="**Kills & Deaths**", value="Kills: " + str(total_kills) +
                                "   Deaths: " + str(total_deaths) +
                                "   K/D: " + str(kill_death_ratio), inline=False)
                embed.add_field(name="**Bombs**", value="Bombs Planted: " + str(total_bombs_planted) +
                                "            Bombs Defused: " + str(total_defused_bombs), inline=False)
                embed.add_field(name="**Wins**", value="Has " + str(total_wins) + " wins!", inline=False)
                embed.add_field(name="**Other Stats**", value="Has played " + str(total_time_hours) + " hours!\n"
                                "Has " + str(total_knife_kills) + " kills with the knife!\n"
                                "Has done" + str(total_damage_done) + " damage.\n"
                                "Has earned $" + str(total_money_earned) + "!\n"
                                "Has a total of " + str(total_headshots) + " headshots!")

                await message.channel.send(embed=embed)



            elif data_get.status_code == 500:
                embed = discord.Embed(title="Sorry" + user + "Uh oh - Player does not exist, server is down, or profile is private. (╯°□°）╯︵ ┻━┻")
                embed.set_thumbnail(url="https://www.publicdomainpictures.net/pictures/40000/nahled/question-mark.jpg")
                await message.channel.send(embed=embed)
                # Because steam changed their privacy settings, go into your profile settings and make everything public

        await message.channel.send("Hello " + user + ", I am online!")

    if message.content.find("!playerbans") != -1:
        vanity_id = message.content[12:]
        url_id = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + key + "&vanityurl=" + str(vanity_id)
        id_get = requests.get(url_id)

        if id_get.status_code == 200:
            id = id_get.json()

            if id["response"]["success"] == 1:
                real_id = id["response"]["steamid"]
                url_bans = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=" + key + "&steamids=" + real_id
                url_name = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + key + "&steamids=" + real_id

                name_get = requests.get(url_name)
                if name_get.status_code == 200:
                    name = name_get.json()

                    player_name = name["response"]["players"][0]["personaname"]
                    player_picture = name["response"]["players"][0]["avatarfull"]
                    bans_get = requests.get(url_bans)
                    if bans_get.status_code == 200:
                        bans = bans_get.json()

                        num_bans = bans["players"][0]["NumberOfGameBans"]
                        if num_bans == 1:
                            embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** Bans:",
                                                  description="Player has " + str(num_bans) + " ban!",
                                                  color=discord.Colour.blue())
                            embed.set_thumbnail(url=player_picture)
                            await message.channel.send(embed=embed)
                        else:
                            embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** Bans:",
                                                  description="Player has " + str(num_bans) + " bans!",
                                                  color=discord.Colour.blue())
                            embed.set_thumbnail(url=player_picture)
                            await message.channel.send(embed=embed)

                    elif bans_get.status_code == 500:
                        embed = discord.Embed(title="Sorry " + user + " - Player Not Found!** (╯°□°）╯︵ ┻━┻")
                        embed.set_thumbnail(url="https://www.publicdomainpictures.net/pictures/40000/nahled/question-mark.jpg")
                        await message.channel.send(embed=embed)
                else:
                    await message.channel.send("Servers are down")
            elif id["response"]["success"] == 42:
                if vanity_id == str(vanity_id):
                    embed = discord.Embed(title="Sorry " + user + "- Player Not Found!** (╯°□°）╯︵ ┻━┻")
                    embed.set_thumbnail(url="https://www.publicdomainpictures.net/pictures/40000/nahled/question-mark.jpg")
                    await message.channel.send(embed=embed)
#                   SteamID64 is only made up of integers so if the characters are letters, they are spelled wrong.
                elif vanity_id != str(vanity_id):
                    url_bans = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=" + key + "&steamids=" + vanity_id
                    url_name = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + key + "&steamids=" + vanity_id

                    name_get = requests.get(url_name)
                    if name_get.status_code == 200:
                        name = name_get.json()

                        if name["response"] == "2":
                            player_name = name["response"]["players"][0]["personaname"]
                            player_picture = name["response"]["players"][0]["avatarfull"]
                            bans_get = requests.get(url_bans)
                            if bans_get.status_code == 200:
                                bans = bans_get.json()

                                num_bans = bans["players"][0]["NumberOfGameBans"]
                                if num_bans == 1:
                                    embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** Bans:",
                                                          description="Player has " + str(num_bans) + " ban!",
                                                          color=discord.Colour.blue())
                                    embed.set_thumbnail(url=player_picture)
                                    await message.channel.send(embed=embed)
                                else:
                                    embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** Bans:",
                                                          description="Player has " + str(num_bans) + " bans!",
                                                          color=discord.Colour.blue())
                                    embed.set_thumbnail(url=player_picture)
                                    await message.channel.send(embed=embed)

                            elif bans_get.status_code == 500:
                                embed = discord.Embed(title="Sorry " + user + " - Player Not Found!** (╯°□°）╯︵ ┻━┻")
                                embed.set_thumbnail(url="https://www.publicdomainpictures.net/pictures/40000/nahled/question-mark.jpg")
                                await message.channel.send(embed=embed)
                else:
                    await message.channel.send("Steam API is Down!")
        elif id_get.status_code == 500:
            url_bans = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=" + key + "&steamids=" + vanity_id
            url_name = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + key + "&steamids=" + vanity_id

            name_get = requests.get(url_name)
            if name_get.status_code == 200:
                name = name_get.json()
                if name["response"]["players"] == "[]":
                    await message.channel.send("Player does not exist")
                else:
                    player_name = name["response"]["players"][0]["personaname"]
                    player_picture = name["response"]["players"][0]["avatarfull"]
                    bans_get = requests.get(url_bans)
                    if bans_get.status_code == 200:
                        bans = bans_get.json()

                        num_bans = bans["players"][0]["NumberOfGameBans"]
                        if num_bans == 1:
                            embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** Bans:",
                                                  description="Player has " + str(num_bans) + " ban!",
                                                  color=discord.Colour.blue())
                            embed.set_thumbnail(url=player_picture)
                            await message.channel.send(embed=embed)
                        else:
                            embed = discord.Embed(title=user + ", Here you go! \n\n**" + player_name + "'s** Bans:",
                                                  description="Player has " + str(num_bans) + " bans!",
                                                  color=discord.Colour.blue())
                            embed.set_thumbnail(url=player_picture)
                            await message.channel.send(embed=embed)

                    elif bans_get.status_code == 500:
                        embed = discord.Embed(title="Sorry " + user + " - Player Not Found!** (╯°□°）╯︵ ┻━┻")
                        embed.set_thumbnail(url="https://www.publicdomainpictures.net/pictures/40000/nahled/question-mark.jpg")
                        await message.channel.send(embed=embed)
            else:
                await message.channel.send("Servers are down!")

    if message.content.find("!csgopistol") != -1:
        team = message.content[12:]
        user_uses = user + ", you should use the "
        if team == "ct":
            randpistol = random.randint(1, 8)

            if randpistol == 1:
                await message.channel.send(user_uses + "**USP-S**!")
            if randpistol == 2:
                await message.channel.send(user_uses + "**P2000**!")
            if randpistol == 3:
                await message.channel.send(user_uses + "**Dual Berattas**!")
            if randpistol == 4:
                await message.channel.send(user_uses + "**P250**!")
            if randpistol == 5:
                await message.channel.send(user_uses + "**Five-SeveN**!")
            if randpistol == 6:
                await message.channel.send(user_uses + "**CZ75-Auto**!")
            if randpistol == 7:
                await message.channel.send(user_uses + "**Desert Eagle (Deagle)**!")
            if randpistol == 8:
                await message.channel.send(user_uses + "**Revolver**!")
        if team == "t":
            randpistol = random.randint(1, 7)
            if randpistol == 1:
                await message.channel.send(user_uses + "**Glock**!")
            if randpistol == 2:
                await message.channel.send(user_uses + "**Dual Berattas**!")
            if randpistol == 3:
                await message.channel.send(user_uses + "**P250**!")
            if randpistol == 4:
                await message.channel.send(user_uses + "**Tec-9**!")
            if randpistol == 5:
                await message.channel.send(user_uses + "**CZ75-Auto**!")
            if randpistol == 6:
                await message.channel.send(user_uses + "**Desert Eagle (Deagle)**!")
            if randpistol == 7:
                await message.channel.send(user_uses + "**Revolver**!")

        game = message.content[9:]
        if game == "tf2":
            players_url = "http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=440"
            players_get = requests.get(players_url)
            if players_get.status_code == 200:
                players = players_get.json()
                number_of_players = players["response"]["player_count"]
                embed = discord.Embed(title=user + ", " + str(number_of_players) + " players are playing TF2!",
                                      color=discord.Colour.blue())
                embed.set_thumbnail(url="https://res.cloudinary.com/teepublic/image/private/s--V4c75MLA--/t_Resized%20Artwork/c_fit,g_north_west,h_954,w_954/co_000000,e_outline:48/co_000000,e_outline:inner_fill:48/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_jpg,h_630,q_90,w_630/v1539296609/production/designs/3303784_0.jpg")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Sorry " + user + "** - Steam information servers are down so we can't access the data!** (╯°□°）╯︵ ┻━┻")
        elif game == "csgo":
            players_url = "http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=730"
            players_get = requests.get(players_url)
            if players_get.status_code == 200:
                players = players_get.json()
                number_of_players = players["response"]["player_count"]
                embed = discord.Embed(title=user + ", " + str(number_of_players) + " players are playing CS:GO!",
                                      color=discord.Colour.blue())
                embed.set_thumbnail(url="https://pngimg.com/uploads/counter_strike/counter_strike_PNG99.png")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Sorry " + user + "** - Steam information servers are down so we can't access the data!** (╯°□°）╯︵ ┻━┻")
        elif game == "dota2":
            players_url = "http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=570"
            players_get = requests.get(players_url)
            if players_get.status_code == 200:
                players = players_get.json()
                number_of_players = players["response"]["player_count"]
                embed = discord.Embed(title=user + ", " + str(number_of_players) + " players are playing Dota2!",
                                      color=discord.Colour.blue())
                embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/fe/DOTA-logo-wis.png")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("Sorry " + user + "** - Steam information servers are down so we can't access the data!** (╯°□°）╯︵ ┻━┻")
        else:
            await message.channel.send("Please enter the game (tf2, csgo, or dota2) after the command!")

    if message.content.find("!help") != -1:
        embed = discord.Embed(title=user + ", Here you go!\n\n**Help**",
                              color=discord.Colour.orange())
        embed.add_field(name="Here are my Commands! **--Don't Put Caps--**", value=""
                        "!**csgostats [steam id (custom or not)]** - views player's CS:GO stats\n"
                        "!**online** - sees if I am online\n"
                        "!**playerbans [steam id (custom or not)]** - views how many bans a player has\n"
                        "!**csgopistol [ct or t]** - tells you random pistol to use depending on which side you are on\n"
                        "!**players [tf2, csgo, or dota2]** - shows the amount of players playing the respective game", inline=False)
                        # Added 4 stars to start the bold characters and end it again. Specifically did this so the bot woud not think this was a command.
        await message.channel.send(embed=embed)


client.run(token)
read_token()
