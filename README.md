# Terminal AI Assistant

A simple terminal-based AI chat assistant built in Python.

The application allows users to create multiple chat sessions, save conversations, reopen previous chats, and interact with an AI model directly from the terminal.

---

## Features

* Create multiple chat sessions
* Open existing chats
* Delete chats
* Persistent chat storage using JSON
* Conversation memory
* Markdown formatted AI responses
* Session statistics
* Error handling
* Terminal-based user interface

---

## Technologies Used

* Python
* JSON
* Rich
* g4f

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Parshv-collab/terminal-ai-assistant.git
cd terminal-ai-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python main.py
```

Menu options:

1. Create Chat
2. Open Chat
3. Delete Chat
4. Show Chats
5. Chat
6. Exit

---

## Chat Commands

Inside a chat session:

* `history` → Show stored message count
* `clear` → Clear current chat memory
* `exit` → Exit current chat session

---

## Project Structure

```text
terminal-ai-assistant/
│
├── main.py
├── chats.json
├── requirements.txt
└── README.md
```

---

## Example Workflow

1. Create a new chat
2. Ask questions
3. Responses are saved automatically
4. Close the program
5. Reopen later and continue the conversation

---

## Future Improvements

* Export chat history
* Search chats
* Multiple AI model selection
* Chat renaming
* User authentication
* GUI version

---

## Author

Built by Parshv as a learning project while exploring:

* Python
* APIs
* JSON storage
* Terminal applications
* AI integration
