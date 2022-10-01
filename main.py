from vkbottle.bot import Bot, Message

client = Bot("vk1.a.rlJ1EbcxLRTTPSAyP5L4mtW3czE94BJySNr7mVb3tNGcjKi_7sbFY7q8i3oxe1ZM_JCxqOKBDWbPCtTNhVD7LijxOlVFDum4wQEpwWwvb6aBi8zMlxfTOiPpR8cRHUe2m5d-Y7fW6ovWzC4sc8dfBDLF77d__D7Dyy880yihBYHRix-41IhPFStYNe5QmR_1")

@client.on.private_message(text="<msg>")
async def echo_answer(ans: Message, msg):
    await ans.answer("Ты написал: %s"%(msg))

# Проверка, если файл запущен, как основной, бот запустится. Иначе, ничего не произойдет.
if __name__ == "__main__":
    client.run_forever()