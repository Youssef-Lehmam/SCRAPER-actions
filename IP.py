from pathlib import Path
import datetime
import requests

if __name__ == "__main__":
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        ip_info = response.json()
        ip_address = ip_info["ip"]
        ip_address = "\n- " + datetime.datetime.now().strftime("%H:%M %d/%m/%y") + " " + ip_address
        readme = Path("README.md").read_text(encoding="utf8")
        readme_title = "# Latest IP"
        new_readme = readme[:readme.find(readme_title)] + f"{ip_address}\n\n"
        with open("README.md", "w+") as f:
            f.write(new_readme)
