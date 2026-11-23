# NEURACODE – AI Python Coding Assistant

**An AI-powered development assistant designed to simplify coding, improve productivity, and support smarter programming workflows.**

## Live Application

**Live Demo:** https://ai-python-coding-assistant.streamlit.app/

---

## 1. Project Overview

NEURACODE is an AI-powered coding assistant developed using Python and Streamlit. It integrates Large Language Models (LLMs) to provide intelligent programming assistance through a single interactive platform.

The application combines multiple coding capabilities, including code generation, debugging, code explanation, code review, code optimization, and test case generation.

The main objective is to reduce repetitive programming effort, support faster problem-solving, and make coding assistance more accessible to students, beginners, and developers.

## 2. Business Problem

Developers and programming learners spend considerable time writing code, identifying errors, understanding unfamiliar logic, reviewing code quality, and preparing test cases.

Using separate tools for these activities can interrupt development workflows and increase the time required to complete programming tasks.

NEURACODE addresses this challenge by bringing multiple AI-powered coding capabilities into one centralized application.

## 3. Business Objectives

- Improve programming productivity through AI-assisted development.
- Reduce manual effort in identifying and resolving coding errors.
- Simplify the understanding of programming logic.
- Encourage readable and maintainable code.
- Support faster development through AI-powered assistance.
- Provide a centralized platform for common programming needs.

## 4. Application Screenshots

### 4.1 Home – Application Dashboard

<img width="1916" height="866" alt="Neuracode Home Page" src="https://github.com/user-attachments/assets/b311265c-484f-46b7-8d03-607cfb5f160c" />


**Description:** Centralized dashboard providing access to the application's coding functionalities.

### 4.2 AI Code Generator

<img width="932" height="830" alt="AI code generator" src="https://github.com/user-attachments/assets/af9a5bf7-06f6-4a11-ab86-5e9160631a78" />

<img width="897" height="837" alt="AI Code Generator- multiple tasks" src="https://github.com/user-attachments/assets/e62e3fac-cf89-466f-af4b-5ecdd10582cd" />


**Description:** Generates programming solutions based on user requirements and selected programming languages.

### 4.3 AI Code Debugger

<img width="802" height="821" alt="Code Debugger" src="https://github.com/user-attachments/assets/b262131c-506a-450f-8b74-62228962fd7c" />


**Description:** Analyzes submitted code, identifies potential errors, and provides debugging suggestions.

### 4.4 AI Code Explainer

<img width="771" height="822" alt="Code Explainer" src="https://github.com/user-attachments/assets/c2039c6d-bed8-4d15-b105-f4d71a4090df" />


**Description:** Explains programming logic and helps users understand how a program works.

### 4.5 AI Chat Assistant

<img width="747" height="826" alt="AI Chat Assistant" src="https://github.com/user-attachments/assets/58ee5756-5289-413a-bed8-a4f11792f9e5" />


**Description:** Provides interactive conversational support for programming questions and technical assistance.

### 4.6 AI Code Reviewer

<img width="746" height="827" alt="AI Code Reviewer" src="https://github.com/user-attachments/assets/a8debdc3-ff62-41c0-b9ed-f8342345d129" />


**Description:** Reviews Python code and provides suggestions related to quality, readability, and potential improvements.

### 4.7 Code Optimizer

<img width="780" height="832" alt="Code Optimizer" src="https://github.com/user-attachments/assets/3389e8f7-9c9f-4f8c-9ed5-4dc0ad4dfa40" />


**Description:** Analyzes existing code and suggests improvements to code structure and efficiency.

### 4.8 Test Case Generator

<img width="755" height="840" alt="Test Case Generator" src="https://github.com/user-attachments/assets/16a6e892-c665-42f4-bd43-9de2ccc117c6" />


**Description:** Generates test scenarios to help validate program behaviour under different input conditions.

## 5. Key Functional Capabilities

| Feature | Description |
|---|---|
| Code Generator | Generates code based on user requirements. |
| Code Debugger | Identifies errors and suggests possible solutions. |
| Code Explainer | Provides understandable code explanations. |
| Chat Assistant | Supports interactive programming conversations. |
| Chat History | Provides access to previous conversations. |
| AI Code Reviewer | Analyzes code quality and suggests improvements. |
| Code Optimizer | Recommends improvements to existing code. |
| Test Case Generator | Creates test scenarios for program validation. |

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive web application interface |
| LangChain | Language model integration |
| Groq API | AI-powered response generation |
| Git | Version control |
| GitHub | Source code hosting |

## 7. Application Workflow

1. **User Input:** The user selects a coding feature and provides the required input.
2. **Input Processing:** The application processes the submitted requirement or source code.
3. **LLM Integration:** The request is passed through LangChain to the configured Groq language model.
4. **AI Response Generation:** The language model generates a response based on the user's request.
5. **Output Presentation:** The generated code, explanations, debugging suggestions, or other results are displayed through the Streamlit interface.

## 8. Business Value

**Productivity Improvement:** Combines multiple programming assistance functionalities in one application.

**Faster Problem Resolution:** Helps users understand programming errors and explore possible solutions.

**Improved Code Understanding:** Supports programming knowledge development through code explanations.

**Code Quality Support:** Encourages better programming practices through code review and optimization suggestions.

**Centralized Development Support:** Provides a unified workspace for common coding activities.

*Note: These are expected business benefits. Actual productivity improvements have not been quantitatively measured.*

## 9. Installation and Setup

### Prerequisites

- Python 3.9 or above
- pip package manager
- Groq API key

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Directory

```bash
cd YOUR_PROJECT_FOLDER
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure API Credentials

Create a `.streamlit/secrets.toml` file:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Never upload API credentials or secret files to a public repository.

### Step 5: Run the Application

```bash
streamlit run app.py
```

## 10. Future Enhancements

- Extend support for additional programming languages.
- Introduce advanced code validation capabilities.
- Improve AI-powered code analysis.
- Enhance chat history management.
- Explore additional LLM integrations.
- Introduce downloadable code outputs.

## 11. Learning Outcomes

Through this project, I gained practical experience in:

- Developing AI-powered applications using Python.
- Integrating Large Language Models into web applications.
- Working with LangChain and Groq API.
- Building interactive interfaces using Streamlit.
- Designing AI-assisted programming workflows.
- Managing source code using Git and GitHub.
- Deploying applications for public access.

## 12. Conclusion

NEURACODE demonstrates the practical application of Generative AI in software development workflows. By integrating multiple coding assistance capabilities into a single platform, the application aims to simplify programming activities and support more efficient development practices.

This project represents my hands-on experience in combining Python application development with Generative AI technologies to build a practical, user-focused solution.

---

## Developer

**SUBHA T**

Interested in Python Development, Artificial Intelligence, Machine Learning, and Generative AI.

**Project:** NEURACODE – AI Python Coding Assistant

**Live Application:** https://ai-python-coding-assistant.streamlit.app/
