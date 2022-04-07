import discord
import openai
from time import sleep


def gpt_3(text):
    your_api_key = ""  # Insert your api key here
    openai.api_key = your_api_key
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    return response.choices[0].text


class MyClient(discord.Client):
    async def on_ready(self):
        await client.get_channel(941322534467534880).send(
            "Hello guys 👋 , it's nice to see you again!" +
            "I'm ready to ""chat so hit me up. 🎉")

        sleep(2)

        await client.get_channel(941322534467534880).send(
            "Also if any one of you would like to have a" +
            "private conversation with me, "
            "just begin your message with $private and i will text you back "
            "in a private chat 🔒")

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("$info"):
            await message.channel.send(
                "Hi " + str(message.author) +
                " ,it's nice to finally meet you !" +
                "I've heard so much about you ! "
                "Please talk english with me,"
                "as I have yet to master any other laguage besides english " +
                "Thank you for understanding, you ARE awesome ❤️ !")
            return
        # uncomment this code if you want to enable private messages.
        # if message.content.startswith("$private"):
        # 	await message.author.send(
        # 		"Hey " + str(message.author) +
        # "what would you like to chat with me about ?
        # Is there anything on your mind ?")
        # 	sleep(3)
        # 	await message.author.send("I got told I'm a great listener 👂")
        # 	return

        message_user = str(message.content)
        message_user = message_user.strip()
        answer = gpt_3(message_user)

        await message.channel.send(str(message.author.mention) + str(answer))

    async def on_message_delete(self, message):
        await message.channel.send("Hey " + str(message.author) +
                                   ", there is no need for secrets.")
        sleep(2)
        await message.channel.send("This is the message " +
                                   str(message.author) +
                                   " tried to delete." + ": " +
                                   str(message.content))

    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '❤️':
            await reaction.message.channel.send(str(user.mention) +
                                                "Thanks for the love !")
        if reaction.emoji == '💩':
            await reaction.message.channel.send(str(user.mention) +
                                                "What's with the attitude ?")
        if reaction.emoji == '👍':
            await reaction.message.channel.send(str(user.mention) +
                                                "Thumbs up to you too 👍")


client = MyClient()
client.run(
    #add your client url here
)
