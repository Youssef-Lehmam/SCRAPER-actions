from pathlib import Path
import requests

if __name__ == "__main__":
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        ip_info = response.json()
        ip_address = ip_info["ip"]
        readme = Path("README.md").read_text(encoding="utf8")
        readme_title = "# Latest IP scraped from https://api.ipify.org?format=json"
        new_readme = readme[:readme.find(readme_title)] + f"{ip_address}\n\n"
        with open("README.md", "w+") as f:
            f.write(new_readme)
