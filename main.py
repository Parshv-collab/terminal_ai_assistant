
from g4f.client import Client
from datetime import datetime
from rich.console import Console
from rich.markdown import Markdown
import json
import time

# ==========================================
# SETUP
# ==========================================

console = Console()
client = Client()

SYSTEM_PROMPT = """
Format all responses with proper paragraphs.
Use line breaks between sections.
Use bullet points when listing items.
Never return one giant paragraph.
Add emoji to make responses more engaging.
Adapt to the user's mood , tone and emotions.
"""

FILE_NAME = "chats.json"

# ==========================================
# FILE FUNCTIONS
# ==========================================

def load_data():

    try:

        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)

    except:

        data = {
            "active_chat": None,
            "chats": {}
        }

        save_data(data)

        return data


def save_data(data):

    with open(FILE_NAME, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

# ==========================================
# CHAT FUNCTIONS
# ==========================================

def create_chat(data):

    name = input("\nChat Name > ").strip()

    if not name:
        print("Invalid name.")
        return

    if name in data["chats"]:
        print("Chat already exists.")
        return

    data["chats"][name] = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    data["active_chat"] = name

    save_data(data)

    print(f"Created chat: {name}")


def open_chat(data):

    chats = list(data["chats"].keys())

    if not chats:
        print("No chats found.")
        return

    print("\nAvailable Chats\n")

    for i, chat in enumerate(chats, start=1):
        print(f"{i}. {chat}")

    try:

        choice = int(input("\nSelect > "))

        selected = chats[choice - 1]

        data["active_chat"] = selected

        save_data(data)

        print(f"Opened: {selected}")

    except:

        print("Invalid selection.")


def delete_chat(data):

    chats = list(data["chats"].keys())

    if not chats:
        print("No chats found.")
        return

    print("\nChats\n")

    for i, chat in enumerate(chats, start=1):
        print(f"{i}. {chat}")

    try:

        choice = int(input("\nDelete > "))

        selected = chats[choice - 1]

        del data["chats"][selected]

        if data["active_chat"] == selected:
            data["active_chat"] = None

        save_data(data)

        print("Chat deleted.")

    except:

        print("Invalid selection.")


def show_chats(data):

    chats = list(data["chats"].keys())

    if not chats:
        print("\nNo chats available.")
        return

    print("\nStored Chats\n")

    for i, chat in enumerate(chats, start=1):

        marker = ""

        if chat == data["active_chat"]:
            marker = " <-- ACTIVE"

        print(f"{i}. {chat}{marker}")

# ==========================================
# AI
# ==========================================

def ask_ai(messages):

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    return response.choices[0].message.content

# ==========================================
# CHAT LOOP
# ==========================================

def chat_loop(data):

    current_chat = data["active_chat"]

    if current_chat is None:

        print("Open or create a chat first.")
        return

    start_time = time.time()

    print("\n" + "=" * 60)
    print(f"Current Chat: {current_chat}")
    print("=" * 60)

    print("Commands:")
    print("exit")
    print("history")
    print("clear")
    print("=" * 60)

    while True:

        user_text = input("\nYou > ")

        if not user_text.strip():
            continue

        if user_text.lower() == "exit":

            duration = int(
                time.time() - start_time
            )

            print(
                f"\nSession Time: {duration} sec"
            )

            break

        if user_text.lower() == "history":

            count = len(
                data["chats"][current_chat]
            )

            print(f"Stored messages: {count}")

            continue

        if user_text.lower() == "clear":

            data["chats"][current_chat] = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                }
            ]

            save_data(data)

            print("Chat cleared.")

            continue

        data["chats"][current_chat].append(
            {
                "role": "user",
                "content": user_text
            }
        )

        save_data(data)

        try:

            print("\nAI is thinking...")

            ai_answer = ask_ai(
                data["chats"][current_chat]
            )

            timestamp = datetime.now().strftime(
                "%H:%M:%S"
            )

            print("\n" + "-" * 60)
            print(f"AI [{timestamp}]")
            print("-" * 60)

            console.print(
                Markdown(ai_answer)
            )

            print("-" * 60)

            data["chats"][current_chat].append(
                {
                    "role": "assistant",
                    "content": ai_answer
                }
            )

            save_data(data)

        except Exception as e:

            data["chats"][current_chat].pop()

            print("\nERROR")
            print(e)

# ==========================================
# MENU
# ==========================================

def main():

    data = load_data()

    while True:

        print("\n" + "=" * 60)
        print("AI CHAT ASSISTANT")
        print("=" * 60)

        print("1. Create Chat")
        print("2. Open Chat")
        print("3. Delete Chat")
        print("4. Show Chats")
        print("5. Chat")
        print("6. Exit")

        if data["active_chat"]:
            print(
                f"\nCurrent Chat: "
                f"{data['active_chat']}"
            )

        choice = input("\nSelect > ")

        if choice == "1":

            create_chat(data)

        elif choice == "2":

            open_chat(data)

        elif choice == "3":

            delete_chat(data)

        elif choice == "4":

            show_chats(data)

        elif choice == "5":

            chat_loop(data)

        elif choice == "6":

            print("Goodbye.")
            break

        else:

            print("Invalid option.")

# ==========================================
# START
# ==========================================

if __name__ == "__main__":
    main()

