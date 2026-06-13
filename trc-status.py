from bs4 import BeautifulSoup
import subprocess
import json

url = "https://www.cbc.ca/newsinteractives/beyond-94"

def fetch_html(url):
    result = subprocess.run(
        [
            "curl",
            "-L",
            "--silent",
            "--show-error",
            "--fail",
            "--max-time", "60",
            "-A",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 trcprogress.ca",
            url
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"curl failed: {result.stderr}")

    return result.stdout


html = fetch_html(url)

soup = BeautifulSoup(html, "html.parser")

counts = soup.select(".resolution-count")

parsed_counts = []
for c in counts:
    try:
        parsed_counts.append(int(c.get_text(strip=True)))
    except:
        pass

complete = parsed_counts[3] if len(parsed_counts) > 3 else None
total = 94

print(json.dumps({
    "complete": complete,
    "total": total
}))
