Since you are using NotebookLM with your study guide, you have a powerful "Engine" for your project. You can use it to extract the data for your CLI and to tutor you on the logic behind the exam.

Here are the specific prompts you should use to build your tool and master the material.

---

### Phase 1: Data Extraction (Populating your CLI "Database")

Copy and paste these into NotebookLM to get the raw data for your GitHub repo.

**1. The "Ports & Protocols" JSON:**

> "Based on the study guide, create a raw JSON array of the common ports for the 220-1101 exam. For each entry, include: 'port_number', 'protocol_name', 'default_transport' (TCP/UDP), and a short 'description' of its function. Make sure it is formatted as valid code so I can use it in a Python script."

**2. The "Command Line" JSON (Core 2 Focus):**

> "Find every Windows and Linux command line tool mentioned in the 220-1102 section. Create a JSON list where each object contains the 'command', its 'utility' (e.g., Network Troubleshooting, Disk Management), a 'common_switch' (like /release or -l), and a 'scenario' where it would be used."

**3. The "Acronym Flashcard" Generator:**

> "Identify the 50 most important acronyms from the Core 1 and Core 2 objectives in this guide. Provide them in a list with the acronym and its full definition. Then, create a 'Hint' for each one that describes what it does without using the words in the acronym."

---

### Phase 2: Building the CLI (The "Logic" Prompts)

Use these to help you write the code for your GitHub repo.

**1. Designing the "Scoring Engine":**

> "In the study guide, look at how CompTIA weights the different domains (e.g., Networking is 20%). Based on those weights, suggest a scoring algorithm for my CLI tool that would give a user a 'Predicted Exam Score' out of 900."

**2. Creating "Simulated Troubleshooting" Logic:**

> "Explain the CompTIA 6-step troubleshooting methodology in detail based on the text. Now, write a 'pseudocode' logic flow for a CLI game where a user is presented with a problem and must select the correct 'Step' in the methodology before moving to the next."

---

### Phase 3: Teaching You (The "Tutor" Prompts)

Use these when you are actually studying the content yourself.

**1. The Socratic Troubleshooting Method (High Level):**

> "I want to practice troubleshooting. Find a scenario in the guide regarding a 'Black Screen of Death' or a 'Mobile device overheating.' Present the symptoms to me and ask me what my **FIRST** step should be according to the CompTIA methodology. Don't give me the answer; wait for my response."

**2. The "Real-World" Translator:**

> "I'm having trouble understanding the difference between a 'Managed Switch' and an 'Unmanaged Switch.' Based on the guide, give me a real-world analogy involving a traffic cop and a four-way stop sign."

**3. The "Performance-Based Question" (PBQ) Practice:**

> "Describe a visual PBQ from the 1101 exam involving a Motherboard. Ask me to identify 5 specific components (like CMOS battery, PCIe slot, etc.) by describing their location or appearance. I will type my answers, and you tell me if I'm right."

---

### Your GitHub Project Blueprint

Since you asked for help creating the CLI, here is a "Minimum Viable Product" (MVP) structure you should aim for:

1. **`data.json`**: Use the JSON prompts above to fill this.
2. **`main.py`**: A simple loop that:
* Loads the JSON.
* Uses a library like `Rich` or `Inquirer` to display questions.
* Checks the user's input against the `correct_answer` field in your JSON.


3. **`README.md`**: This is crucial for GitHub.
* Explain that this is an **Active Recall** tool.
* Include a "How to Contribute" section where others can add more questions to the JSON.



**Would you like me to write a 30-line Python script that imports that JSON and runs a basic "Port Quiz" in your terminal?**