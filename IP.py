from pathlib import Path
import requests

if __name__ == "__main__":
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        ip_info = response.json()
        ip_address = ip_info["ip"]

        # Read existing content from README.md
        readme_path = Path("README.md")
        readme_content = readme_path.read_text(encoding="utf8")

        # Create a comment line with the IP address
        comment_line = f"Added IP: {ip_address}"

        # Append the comment line as a new line
        new_readme = f"{readme_content.strip()}\n{comment_line}\n"

        # Write updated content to README.md
        with open("README.md", "w+") as f:
            f.write(new_readme)
