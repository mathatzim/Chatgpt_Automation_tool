import os
import argparse
from pathlib import Path

from handler.chatgpt_selenium_automation import ChatGPTAutomation


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Send a prompt to ChatGPT via Selenium automation (manual login)."
    )
    parser.add_argument("--prompt", required=True, help="Prompt to send")
    parser.add_argument(
        "--chrome-path",
        default=os.getenv("CHROME_PATH"),
        help="Path to Chrome binary (e.g., chrome.exe). Can also set CHROME_PATH.",
    )
    parser.add_argument(
        "--driver-path",
        default=os.getenv("CHROMEDRIVER_PATH"),
        help="Path to chromedriver. Can also set CHROMEDRIVER_PATH.",
    )
    parser.add_argument(
        "--save",
        default="conversation.txt",
        help="Filename to save conversation text (saved under conversations/).",
    )
    args = parser.parse_args()

    if not args.chrome_path:
        raise ValueError("Missing Chrome path. Provide --chrome-path or set CHROME_PATH.")
    if not args.driver_path:
        raise ValueError("Missing ChromeDriver path. Provide --driver-path or set CHROMEDRIVER_PATH.")

    chrome_path = Path(args.chrome_path).expanduser()
    driver_path = Path(args.driver_path).expanduser()

    chatgpt = ChatGPTAutomation(
        chrome_path=str(chrome_path),
        chrome_driver_path=str(driver_path),
    )

    try:
        chatgpt.send_prompt_to_chatgpt(args.prompt)
        response = chatgpt.return_last_response()
        print("\n=== Model response ===\n")
        print(response)

        if args.save:
            # Ensure output folder exists (your handler may already do this;
            # this is a safe extra guard).
            out_dir = Path("conversations")
            out_dir.mkdir(parents=True, exist_ok=True)
            chatgpt.save_conversation(str(out_dir / args.save))
    finally:
        chatgpt.quit()


if __name__ == "__main__":
    main()

