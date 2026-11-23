# NEURACODE – AI Python Coding Assistant

## Project Overview

NEURACODE is an AI-powered coding assistant developed to simplify programming activities and improve developer productivity. The application brings multiple coding support capabilities into a single platform, helping users generate, debug, understand, review, and optimize code through AI-driven interactions.

The solution integrates Large Language Models (LLMs) through Groq API and LangChain, with Streamlit providing an interactive user interface.

The primary goal of this project is to reduce the time and effort involved in routine programming tasks while making coding assistance more accessible to students, beginners, and developers.

## Live Application

**Application:** https://ai-python-coding-assistant.streamlit.app/

## Business Problem

Developers and programming learners frequently spend considerable time performing repetitive coding activities, identifying errors, understanding unfamiliar code, and validating program logic.

Using separate tools for these activities can interrupt development workflows and increase the time required to complete programming tasks.

NEURACODE addresses this challenge by providing multiple AI-powered coding capabilities through a unified application.

## Business Objectives

- Improve developer productivity by simplifying common programming activities.
- Reduce manual effort involved in identifying and resolving coding errors.
- Support faster understanding of programming concepts and existing code.
- Encourage better code quality through AI-powered reviews and optimization suggestions.
- Provide an accessible coding support platform for beginners and experienced developers.

## Key Functional Capabilities

| Module | Business Value |
|---|---|
| Home | Provides centralized access to coding assistance features. |
| Code Generator | Accelerates initial code development based on user requirements. |
| Code Debugger | Helps identify programming errors and suggests possible solutions. |
| Code Explainer | Improves code understanding and supports technical learning. |
| Chat Assistant | Enables interactive, natural-language programming support. |
| Chat History | Allows users to revisit previous coding conversations. |
| AI Code Reviewer | Provides feedback on code quality and potential improvements. |
| Code Optimizer | Suggests ways to improve code structure and efficiency. |
| Test Case Generator | Helps create test scenarios for validating program behaviour. |

## Technology Stack

| Technology | Implementation |
|---|---|
| Python | Application development and core logic |
| Streamlit | Interactive web application interface |
| LangChain | Integration and interaction with language models |
| Groq API | LLM-powered response generation |
| Git & GitHub | Source code management and version control |

## Application Workflow

1. The user selects a required coding functionality.
2. The user provides source code, programming requirements, or a question.
3. The application processes the input and sends the relevant request to the AI model through the integration layer.
4. The AI model generates a context-aware response.
5. The application displays the generated code, explanations, debugging suggestions, or other relevant results.
6. Users can continue interacting with the application based on their requirements.

## Expected Business Impact

**Improved Productivity:** Reduces the effort required for common programming activities by bringing multiple assistance features into one workspace.

**Faster Problem Resolution:** Helps developers understand errors and explore potential solutions more efficiently.

**Better Code Understanding:** Supports learning and knowledge sharing through simplified code explanations.

**Code Quality Improvement:** Encourages structured, readable, and maintainable programming practices through review and optimization suggestions.

**Workflow Consolidation:** Provides a centralized environment for several common coding support activities.

*Note: These are intended business benefits. Quantitative productivity improvements have not been benchmarked.*

## Installation and Execution

### Prerequisites

- Python 3.9 or above
- pip package manager
- Groq API key

### Setup Instructions

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd YOUR_PROJECT_FOLDER
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure API credentials**

Create a `.streamlit/secrets.toml` file:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Keep API credentials secure and never commit secret files to a public repository.

**5. Start the application**

```bash
streamlit run app.py
```

## Future Scope

- Expand support for additional programming languages.
- Introduce advanced code analysis capabilities.
- Improve code validation and testing workflows.
- Enhance conversation management and chat history.
- Explore additional LLM integrations for improved flexibility.

## Conclusion

NEURACODE demonstrates how Generative AI can be applied to practical software development challenges. By combining code generation, debugging, explanation, review, optimization, and test case generation in one application, the project provides a unified environment for AI-assisted programming.

This project also provided practical experience in integrating LLMs, developing interactive applications, and building AI-powered solutions using Python.

## Developer

**SUBHA T**

Developed as a practical project focused on Generative AI, Python application development, and intelligent coding assistance.
