#! /data/data/com.termux/files/usr/bin/python3
#garpozir@gmail.com

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.tl.functions.channels import InviteToChannelRequest
import sys

def main():
    chat_id=sys.argv[1]
    phone='+989020329144'
    api_id=6172884
    api_hash='1e7640728474bebc2ae5a131a49a2f9b'
    client = TelegramClient(phone, api_id, api_hash)
    async def mai():
        await client.send_message('me', 'garpozir@gmail.com')
    with client:
        client.loop.run_until_complete(mai())
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('40779'))
    try:
        target_group_entity = InputPeerChannel(1295195476, -128284830127589494)
        user_to_add = client.get_input_entity(int(chat_id))
        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
    except:pass

if __name__ == '__main__':
    main()
