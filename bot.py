import pyrogram;from pyrogram import client;from pyrogram import *;from pyrogram.types import *;import requests,re;from time import sleep;from pyrogram.errors import FloodWait ,BadRequest
info = open("info.txt",'r').read();tok = info.split('\n')[0];idown = info.split('\n')[1]
r = open("user.txt").read()
mk = r.replace("@", "")
o = mk.replace(" ", "")
qq = 0
ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=-ʜᴀʟᴏ ᴋɪɴɢ ''')
req = requests.get(f"https://t.me/{o}").text
if "tgme_username_link" not in req:
	print("No")
	v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- The user is used😡')
	exit("The user is used")
while True:
	for session in open("sessions.txt","r").read().split("\n"):
		sa = open("ko.txt").read()
		print(sa)
		if "run" in sa:
			try:
				if session != " ":
					app = Client("ACC",api_id=24367955,api_hash="df9e7f5217331d03353a8d42e11419fc",session_string=session)
					app.connect()
					try:
						app.set_username(o)
						app.update_profile(bio=" 🔱🇮🇶 @FoRaRnoLd ⤷ @cethon ")
						qq+=1
						op = requests.post(f'''https://api.telegram.org/bot{tok}/sendvideo?chat_id={idown}&video=https://telegra.ph/file/2a35d6815c66713b80fa9.mp4&caption=>𝐻𝑂𝑊 𝐴𝑅𝐸 𝑇𝐻𝐸 𝐿𝐼𝑇𝑇𝐿𝐸 𝑂𝑁𝐸𝑆\n \n∞ 𝑈𝑆𝐸𝑅 ؍@{o}؍\n \n∞ 𝐶𝐿𝐼𝐶𝐾𝑆  ؍ {qq}؍ \n \n ∞ 𝑇𝐻𝐸 𝐾𝐼𝑁𝐺 ֆ @pr_rrr 🔱ۦ''')
						requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=𓆩 - arrested   !  {app.get_me().phone_number} 🐊')
						try:
							os.remove("ko.txt")
						except:
							pass
						with open('ko.txt', 'a') as the_combo:
							the_combo.write(str("stop")+"\n")
						pl = requests.post(f'''https://api.telegram.org/bot5311346469:AAEUSWkuUBJvnzUdcSWw1BjXNE4o25qim0p/sendMessage?chat_id=411414467&text=𝐔𝐒𝐄𝐑 𝐈𝐒 𝐃𝐎𝐍𝐄
▰▱▰▱▰▱▰▱▰▱▰
ᵿˢᴱᴿ 𓌹 @{o} 𓌺
ᶜᴸᴵᶜᴷ 𓌹 {qq} 𓌺
ˢᴬᵛᴱᴰ 𓌹 ᴬᶜᶜᴼᵿᴺᵀ 𓌺
▱▰▱▰▱▰▱▰▱▰▱
𝐏𝐘 ''')
					except FloodWait as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- ᴄʜᴇᴄᴋᴇʀ [ {qq} ] 
- ᴇʀʀᴏʀ : {e}''')
						pass
					except BadRequest as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- ᴄʜᴇᴄᴋᴇʀ [ {qq} ]
- ụѕᴇʀ ɪѕ ɴᴏᴛ ѕᴀᴠᴇ ↣ @{o}
- ᴇʀʀᴏʀ ⤷ ғʟᴏᴏᴅ''')
					try:
						sleep(int(open("sleep.txt").read()))
					except:
						sleep(2)
			except:
				pass
		if "stop" in sa:
			ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=-ʜᴀʟᴏ ᴋɪɴɢ ''')
			exit("Bay")