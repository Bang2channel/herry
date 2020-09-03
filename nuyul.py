# Bangtwo Channel

import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 1169057
api_hash = '91b887d78631c352f9ea2083569f8703'

# WELCOME BLOCK
print(Fore.MAGENTA + '  #####      ##     ##    #  #####   #######')
print(Fore.MAGENTA + '  ##   #    ## #    ## #  # ##             ##')
print(Fore.MAGENTA + '  #####    ######   ##  # # ## ###   ########')
print(Fore.MAGENTA + '  ##   #  ##     #  ##   ## ##   #   ##')
print(Fore.MAGENTA + '  #####  ###    ### ##   ##  ##### # ########')
print(Fore.YELLOW  + ' ================================================')
print(Fore.CYAN    + '      YouTube     	: Bangtwo Channel')
print(Fore.CYAN    + '      Group Tele   	: BangTwo')
print(Fore.YELLOW  + ' ================================================\n' + Fore.RESET)
print(Fore.CYAN +'-                   Click Bot Script v4                             -' + Fore.RESET)
# DESCRIPTION BLOCK
print('\n	 Hasilkan uang menggunakan bot telegram.\n')
# Bot options
print(' Daftar Menu: \n')
option = ["Dogecoin_click_bot", "Litecoin_click_bot", "BCH_clickbot", "Zcash_click_bot", "Bitcoinclick_bot"] #Bot option list
# Print bot options list with numberings
for number, letter in enumerate(option):
    print(	"	", number, letter)
# Ask user to select bot
ask = int(input ("	\n	Pilih BOT yang ingin Anda jalankan?" + Fore.CYAN + " (Masuk Nombor BOT)" + Fore.CYAN + ":" ))
answer = (option[ask])
url_channel = answer

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=15)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]

async def main():
	print(Fore.GREEN + url_channel + Fore.RESET + " selected.\n")
	print('		DogeClick Bot Channel Actions Menu.\n')
	# Bot options
	print(' Daftar Menu: \n')
	action = ["Visit", "Message", "Join"] #Bot option list
	# Print bot options list with numberings
	for number, letter in enumerate(action):
		print(	"	", number, letter)
	# Ask user to select bot
	ask_action = int(input ("	\n	Pilih BOT yang ingin Anda jalankan?" + Fore.CYAN + " (Masukan Nombor)" + Fore.RESET + ":" ))
	answer = (action[ask_action])
	bot_action = answer
	if answer == action[0]:
		print(action[0] + " performed")
				# Check if phone number is not specified
		if len(sys.argv) < 2:
			print('Usage: python start.py phone_number')
			print('-> Input number in international format (example: +639162995600)\n')
			e = input('Tekan sembarang tombol untuk keluar...')
			exit(1)

		phone_number = sys.argv[1]

		if not os.path.exists("session"):
			os.mkdir("session")

		# Connect to client
		client = TelegramClient('session/' + phone_number, api_id, api_hash)
		await client.start(phone_number)
		me = await client.get_me()
		ads_channel = "DogeCoin"
		await client(JoinChannelRequest(ads_channel))
		ads_group = "DogeCoin"
		await client(JoinChannelRequest(ads_group))
		print('Current account:' + Fore.CYAN + f'{me.first_name}({me.username})\n' + Fore.RESET)
		print_msg_time(Fore.YELLOW + 'Mengirim/Mengunjungi Perintah' + Fore.RESET)

		# Start command /visit
		await client.send_message(url_channel, '/visit')

		# Start visiting the ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def visit_ads(event):


			original_update = event.original_update
			if type(original_update)is not UpdateShortMessage:
				if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
					url = event.original_update.message.reply_markup.rows[0].buttons[0].url
					#url = event.message.reply_markup.rows[0].buttons[0].url

					if url is not None:
						print_msg_time('Mengunjungi situs web...')

						# Parse the html of url
						(status_code, text_response) = get_response(url)
						parse_data = BeautifulSoup(text_response, 'html.parser')
						captcha = parse_data.find('div', {'class':'g-recaptcha'})

						# Captcha detected
						if captcha is not None:
							print_msg_time(Fore.CYAN + 'Captcha detected!'+ Fore.CYAN +' Skipping ads...\n')

							# Clicks the skip
							await client(GetBotCallbackAnswerRequest(
								peer=url_channel,
								msg_id=event.message.id,
								data=event.message.reply_markup.rows[1].buttons[1].data
							))

		# Print earned money
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def wait_hours(event):
			message = event.raw_text
			if 'You earned' in message:
				print_msg_time(Fore.GREEN + f'{message}' + Fore.RESET)
		# Balance Check
			#======== Start print balance
		#@client.on(events.NewMessage(chats=url_channel, incoming=True))
		#async def account_balance(event):
			#message = event.raw_text
			#if 'Available balance' in message:
				#print_msg_time(Fore.YELLOW + f'{message}\n' + Fore.RESET)
			# Print earned money
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def manual_skip(event):
			message = event.raw_text
			if 'Skipping task...' in message:
				print_msg_time(Fore.YELLOW + f'{message}' + Fore.RESET)
		# No longer valid
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_valid(event):
			message = event.raw_text
			if 'Maaf, tugas itu sudah tidak valid' in message:
				print_msg_time(Fore.CYAN + 'Maaf, tugas itu sudah tidak valid.' + Fore.RESET)
				print_msg_time(Fore.YELLOW + 'Mengirim / mengunjungi perintah' + Fore.RESET)
				await client.send_message(url_channel, '/visit')
		# No more ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_ads(event):
			message = event.raw_text
			if 'no new ads available' in message:
				print_msg_time(Fore.CYAN + 'Maaf, tidak ada iklan baru yang tersedia\n' + Fore.RESET)
				e = input('Tekan sembarang tombol untuk keluar...ENTER')
				exit(1)
	elif answer == action[1]:
		print(action[1] + " performed")
				# Check if phone number is not specified
		if len(sys.argv) < 2:
			print('Usage: python start.py phone_number')
			print('-> Input number in international format (example: +639162995600)\n')
			e = input('Tekan sembarang tombol untuk keluar...ENTER')
			exit(1)

		phone_number = sys.argv[1]

		if not os.path.exists("session"):
			os.mkdir("session")

		# Connect to client
		client = TelegramClient('session/' + phone_number, api_id, api_hash)
		await client.start(phone_number)
		me = await client.get_me()
		ads_channel = "DogeBot"
		await client(JoinChannelRequest(ads_channel))
		ads_group = "DogeBot"
		await client(JoinChannelRequest(ads_group))
		print('Current account:' + Fore.CYAN + f'{me.first_name}({me.username})\n' + Fore.RESET)
		print_msg_time('Mengirim/Perintah Bot')

		# Start command /bots
		await client.send_message(url_channel, '/bots')

		# Message the bot
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def join_start(event):
			message = event.raw_text
			if 'Forward a message to' in message:
				channel_msg = event.original_update.message.reply_markup.rows[0].buttons[0].url
				print_msg_time(f'URL @{channel_msg}')

				if '?' in channel_msg:
					channel_name = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
				elif '?' not in channel_msg:
					channel_name = re.search(r't.me\/(.*?)', channel_msg).group(1)

				print_msg_time(f'Messaging @{channel_name}...')
				await client.send_message(channel_name, '/start')

				# Forward the bot message
				@client.on(events.NewMessage(chats=channel_name, incoming=True))
				async def earned_amount(event):
					msg_id = event.message.id,
					await client.forward_messages(url_channel, msg_id, channel_name)

		# Print earned amount
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def earned_amount(event):
			message = event.raw_text
			if 'You earned' in message:
				print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)

		# No more ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_ads(event):
			message = event.raw_text
			if 'no new ads available' in message:
				print_msg_time(Fore.CYAN + 'Mengirim/Perintah Bot\n' + Fore.RESET)
				e = input('Tekan sembarang tombol untuk keluar...ENTER')
				exit(1)
	elif answer == action[2]:
		print(action[2] + " performed")
				# Check if phone number is not specified
		if len(sys.argv) < 2:
			print('Usage: python start.py phone_number')
			print('-> Input number in international format (example: +639162995600)\n')
			e = input('Tekan sembarang tombol untuk keluar...ENTER')
			exit(1)

		phone_number = sys.argv[1]

		if not os.path.exists("session"):
			os.mkdir("session")

		# Connect to client
		client = TelegramClient('session/' + phone_number, api_id, api_hash)
		await client.start(phone_number)
		me = await client.get_me()
		ads_channel = "DogeCoin"
		await client(JoinChannelRequest(ads_channel))
		ads_group = "DogeCoin"
		await client(JoinChannelRequest(ads_group))
		print('Current account:' + Fore.CYAN + f'{me.first_name}({me.username})\n' + Fore.RESET)
		print_msg_time('Mengirim/Perintah Bot')

		# Start command /join
		await client.send_message(url_channel, '/join')

		# Join the channel
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def join_start(event):
			message = event.raw_text
			if 'You must join' in message:
				channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
				print_msg_time(f'Joining @{channel_name}...')

				# Join the channel
				await client(JoinChannelRequest(channel_name))
				print_msg_time(f'Verifying...')

				# Clicks the joined
				await client(GetBotCallbackAnswerRequest(
					peer=url_channel,
					msg_id=event.message.id,
					data=event.message.reply_markup.rows[0].buttons[1].data
				))

		# Print waiting hours
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def wait_hours(event):
			message = event.raw_text
			if 'You must stay' in message:
				waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
				print_msg_time(Fore.GREEN + f'Success! Please wait {waiting_hours} to earn reward\n' + Fore.RESET)

		# No more ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_ads(event):
			message = event.raw_text
			if 'no new ads available' in message:
				print_msg_time(Fore.CYAN + 'Maaf, tidak ada iklan baru yang tersedia\n' + Fore.RESET)
				e = input('Tekan sembarang tombol untuk keluar..ENTER')
				exit(1)
	else:
		print("Anda tidak memasukkan apa pun yang saya tidak ada tindakan. Keluar..EXSIT")
		exit


	await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())
