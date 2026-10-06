# Cognitive Assistant System (CAS)

> A personal AI assistant built with Python, designed to evolve into a modular agent capable of maintaining context, using tools, accessing knowledge and assisting with everyday tasks.

CAS — **Cognitive Assistant System** — is a personal project focused on exploring Artificial Intelligence, Large Language Models and software engineering through the development of an AI assistant from the ground up.

Rather than being only a chatbot interface, the long-term goal is to progressively build an assistant capable of maintaining context, integrating external tools and APIs, accessing persistent knowledge and assisting with different tasks through a modular architecture.

The project is being developed incrementally as part of my Computer Science studies and my exploration of AI engineering.

---

## ✨ Current Features

- Interactive command-line interface (CLI)
- Integration with Google Gemini through the `google-genai` SDK
- Conversational interaction with an LLM
- Conversation context maintained during the current session
- Interaction continuity using the Gemini Interactions API
- Custom system instructions for assistant behavior
- Basic command handling (`help`, `exit`, `quit`)
- Environment variable management for API credentials
- Modular separation between application logic, LLM integration and prompts
- Basic error handling for API communication

---

## 🧠 How It Works

CAS currently operates through a command-line interface.

The application receives the user's input and sends it to the language model through the Gemini API. Conversation continuity is maintained during the session, allowing the assistant to respond based on previous interactions rather than treating every message independently.

A simplified flow looks like this:

```text
User
  ↓
CLI Interface
  ↓
CAS Application
  ↓
LLM Integration
  ↓
Gemini API
  ↓
Response
  ↓
Conversation continues with context
```

The project is intentionally being built step by step so that new capabilities can be introduced without coupling every feature directly to the main application.

---

## 🛠️ Tech Stack

### Core

- Python
- Google Gemini API
- `google-genai`

### Development

- Git
- GitHub
- Python Virtual Environment (`venv`)
- Environment Variables (`.env`)
- `python-dotenv`

### Concepts

- Large Language Models (LLMs)
- Conversational AI
- Context management
- Prompt Engineering
- API Integration
- Modular Software Design

---

## 📁 Project Structure

CAS follows a modular project structure designed to keep the application
organized as new capabilities are introduced.

```text
CAS-CognitiveAiSystem/
│
├── docs/                  # Project documentation
├── experiments/           # AI and API experiments
├── src/
│   ├── llm.py             # LLM/API integration
│   ├── main.py            # CLI and application entry point
│   └── prompts.py         # System prompts and assistant behavior
│
├── tests/                 # Automated and integration tests
│
├── .env.example           # Environment variable template
├── .gitignore
├── README.md
└── requirements.txt       # Python dependencies
```

### Main components

**`main.py`**  
Handles the CLI interaction, user input and application flow.

**`llm.py`**  
Handles communication between CAS and the language model API.

**`prompts.py`**  
Stores the system instructions that define the assistant's behavior.

> `.env` is used locally for sensitive environment variables and is not committed to the repository.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/bruniibs/CAS-Cognitive-AI-System.git
cd CAS-CognitiveAiSystem
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and add the required API credential.

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your real API key to the repository.

### 6. Run CAS

```bash
python src/main.py
```

---

## 💬 Current Commands

| Command | Description |
|---|---|
| `help` | Displays the available commands |
| `exit` | Closes CAS |
| `quit` | Closes CAS |

Any other input is processed as a conversation with the assistant.

---

## 🗺️ Roadmap

CAS is an ongoing project. Future iterations are planned to progressively transform the current conversational assistant into a more capable AI system.

### Phase 1 — Conversational Core

- [x] CLI interface
- [x] LLM integration
- [x] System instructions
- [x] Session conversation context
- [x] Basic command system
- [ ] Improve error handling and application structure

### Phase 2 — Tools & Agents

- [ ] Tool / Function Calling
- [ ] Web search capabilities
- [ ] External API integrations
- [ ] Agent-based task execution
- [ ] Confirmation system for sensitive actions

### Phase 3 — Knowledge & Memory

- [ ] Persistent memory
- [ ] Database integration
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Embeddings
- [ ] Vector database integration
- [ ] Personal knowledge base

### Phase 4 — Assistant Capabilities

- [ ] Task management
- [ ] Notes and personal information retrieval
- [ ] Calendar integrations
- [ ] Automated workflows
- [ ] Additional specialized tools

### Phase 5 — Interface & Deployment

- [ ] Graphical or web interface
- [ ] Authentication
- [ ] Containerization
- [ ] Cloud deployment
- [ ] Multi-device access

---

## 🎯 Project Goals

CAS is both a personal assistant project and a practical environment for studying and experimenting with AI engineering.

Through its development, the project explores topics such as:

- Software architecture
- Python development
- API integration
- LLM application development
- AI agents
- Context and memory systems
- Retrieval-Augmented Generation
- Databases
- Tool integration
- Cloud deployment

Each capability is implemented progressively rather than abstracted behind pre-built solutions, allowing the project to serve as a hands-on learning environment.

---

## 🔒 Security

Sensitive information such as API keys must be stored in environment variables.

The `.env` file should always remain ignored by Git.

Example:

```gitignore
.env
.venv/
```

If an API key is accidentally committed, it should be revoked and replaced immediately.

---

## 📌 Project Status

🚧 **In active development**

CAS currently provides the conversational foundation of the assistant. The next stages will focus on expanding the architecture with tools, persistent memory and agent capabilities.

---

## 👩‍💻 Author

**Bruna Sant'Ana**

Computer Science • Artificial Intelligence • Software Development

GitHub: `@bruniibs`

---

*CAS is an evolving personal project built to explore how modern AI assistants can be designed from the ground up.*