import json
from datetime import datetime, timezone
from pathlib import Path

CONFIG = Path(__file__).with_name("config.json")
LOG = Path(__file__).with_name("activity.log")


def load_config():
    with CONFIG.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    config = load_config()

    now = datetime.now(timezone.utc).astimezone()
    timestamp = now.isoformat(timespec="seconds")

    message = (
        f"[{timestamp}] Promotion cycle prepared\n"
        f"Instagram post: {config['instagram_url']}\n"
        f"Promotion page: {config['promotion_page']}\n"
        f"Next cooldown: {config['cooldown_minutes']} minutes\n"
        "Action required: manually review and submit any promotion request."
    )

    print(message)

    with LOG.open("a", encoding="utf-8") as f:
        f.write(message + "\n\n")


if __name__ == "__main__":
    main()
