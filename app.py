
import streamlit as st
from langchain_groq import ChatGroq

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="NEURACODE | AI Python Lab",
    page_icon=" ",
    layout="wide"
)

SIDEBAR_OPTIONS = {
    " Home": "Home",
    " Code Generator": "Code Generator",
    " Code Debugger": "Code Debugger",
    " Code Explainer": "Code Explainer",
    " Chat Assistant": "Chat Assistant",
    " Chat History": "Chat History",
    " AI Code Reviewer": "AI Code Reviewer",
    " Code Optimizer": "Code Optimizer",
    " Test Case Generator": "Test Case Generator"
}

# ==================================================
# SESSION STATE
# ==================================================

defaults = {
    "current_page": "Home",
    "chat_history": [],
    "last_response": "",
    "last_input": "",
    "last_type": "",
    "followup_count": 0,
    "sidebar_navigation": "Home"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def navigate_to(target):
    st.session_state.current_page = target

    matching_label = next(
        label for label, page_name in SIDEBAR_OPTIONS.items()
        if page_name == target
    )

    st.session_state.sidebar_navigation = matching_label


def sync_sidebar_page():
    selected = st.session_state.sidebar_navigation
    st.session_state.current_page = SIDEBAR_OPTIONS[selected]


# ==================================================
# CUSTOM CSS
# ==================================================

st.html("""
<style>

.stApp {
    background:
        radial-gradient(ellipse at 10% 10%, #29205B 0%, transparent 38%),
        radial-gradient(ellipse at 90% 80%, #103B54 0%, transparent 35%),
        linear-gradient(135deg, #080D1C, #11152C 55%, #17112D);
    color: #F4F5FF;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

h1, h2, h3 {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

p, label, li {
    color: #CBD2ED;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #10172D, #211638);
    border-right: 1px solid #484477;
}

/* BUTTONS */

.stButton > button {
    background: linear-gradient(100deg, #7547FF, #00AFCB);
    color: white;
    border: 1px solid transparent;
    border-radius: 12px;
    font-weight: 700;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    border: 1px solid #8EEEFF;
    box-shadow: 0 7px 22px #7547FF66;
    color: white;
}

/* FEATURE CARDS */

.st-key-feature_generator button,
.st-key-feature_debugger button,
.st-key-feature_explainer button,
.st-key-feature_assistant button {
    min-height: 165px;
    width: 100%;
    white-space: pre-wrap;
    text-align: left;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding: 22px;
    line-height: 1.8;
    font-size: 15px;
    border-radius: 18px;
    border: 1px solid #514B85;
    background: linear-gradient(145deg, #20294A, #2A1E49);
    box-shadow: 0 5px 22px #00000040;
}

.st-key-feature_generator button:hover,
.st-key-feature_debugger button:hover,
.st-key-feature_explainer button:hover,
.st-key-feature_assistant button:hover {
    background: linear-gradient(135deg, #34245F, #123E58);
    border: 1px solid #22D3EE;
    box-shadow: 0 10px 30px #7547FF55;
    transform: translateY(-5px);
}

/* INPUTS */

div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
    background: #151C35;
    color: white;
    border: 1px solid #55518B;
    border-radius: 10px;
}

div[data-testid="stTextArea"] textarea:focus {
    border: 1px solid #22D3EE;
    box-shadow: 0 0 10px #22D3EE44;
}

/* SIDEBAR RADIO */

div[role="radiogroup"] label {
    background: #1A2340;
    border: 1px solid #484477;
    border-radius: 10px;
    padding: 9px 12px;
    margin-bottom: 7px;
}

div[role="radiogroup"] label:hover {
    border-color: #22D3EE;
    background: #29234A;
}

/* DIVIDERS */

hr {
    border-color: #34365F;
}

/* HERO */

.hero-section {
    background:
        radial-gradient(circle at 90% 10%, #5540A855, transparent 35%),
        linear-gradient(115deg, #211844, #142D4C 65%, #153E55);
    border: 1px solid #6658A2;
    border-radius: 24px;
    padding: 38px 35px;
    margin-bottom: 28px;
    box-shadow: 0 12px 40px #00000055;
}

.hero-label {
    color: #67E8F9;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
}

.hero-title {
    font-size: clamp(34px, 5vw, 52px);
    line-height: 1.15;
    font-weight: 900;
    margin-top: 16px;
    background: linear-gradient(90deg, #FFFFFF, #A78BFA, #67E8F9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-tagline {
    font-size: 20px;
    font-weight: 700;
    color: #67E8F9;
    margin-top: 14px;
}

.hero-description {
    font-size: 15px;
    line-height: 1.8;
    color: #D3D9F2;
    max-width: 700px;
    margin-top: 15px;
}

.section-label {
    color: #A78BFA;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

/* FOOTER */

.footer {
    text-align: center;
    padding: 25px 10px;
    margin-top: 30px;
    border-top: 1px solid #34365F;
}

.footer-brand {
    font-size: 22px;
    font-weight: 900;
    letter-spacing: 3px;
    color: #A78BFA;
}

.footer-tagline {
    font-size: 10px;
    letter-spacing: 3px;
    color: #67E8F9;
    margin-top: 7px;
}

</style>
""")

# ==================================================
# GROQ AI MODEL
# ==================================================

try:
    api_key = st.secrets.get("GROQ_API_KEY", "")
except Exception:
    api_key = ""

llm = None

if api_key:
    try:
        llm = ChatGroq(
            model="openai/gpt-oss-120b",
            api_key=api_key,
            temperature=0.3
        )
    except Exception as e:
        st.error(f"Model initialization error: {e}")
else:
    st.sidebar.warning(
        "Add GROQ_API_KEY in Streamlit Secrets to enable AI."
    )


def generate_response(prompt):

    if not llm:
        return "Please configure GROQ_API_KEY in Streamlit Secrets."

    try:
        response = llm.invoke(prompt)
        return response.content

    except Exception as e:
        return f"AI Error: {str(e)}"


def save_result(tool_name, user_input, response):

    st.session_state.last_response = response
    st.session_state.last_input = user_input
    st.session_state.last_type = tool_name
    st.session_state.followup_count = 0

    st.session_state.chat_history.append({
        "type": tool_name,
        "input": user_input,
        "output": response
    })


# ==================================================
# FOLLOW-UP SUGGESTIONS
# ==================================================

def show_followups():

    st.markdown("---")
    st.markdown("### ✨ What's Next?")
    st.caption("Keep exploring with NEURACODE AI.")

    suggestions = [
        "Explain this in a beginner-friendly way",
        "Show a practical example",
        "Improve and optimize this solution"
    ]

    for i, suggestion in enumerate(suggestions):

        if st.button(
            f"💡 {suggestion}",
            key=f"followup_{st.session_state.last_type}_{st.session_state.followup_count}_{i}",
            use_container_width=True
        ):

            prompt = f"""
Previous task:
{st.session_state.last_input}

Previous AI response:
{st.session_state.last_response}

Follow-up request:
{suggestion}

Give a helpful, clear answer with examples where useful.
"""

            with st.spinner("NEURACODE AI is working..."):
                result = generate_response(prompt)

            save_result(
                st.session_state.last_type,
                suggestion,
                result
            )

            st.session_state.followup_count += 1
            st.rerun()


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.html("""
    <div style="text-align:center;padding:15px 2px;">

        <h2 style="
            font-size:27px;
            font-weight:900;
            letter-spacing:2px;
            background:linear-gradient(90deg,#A78BFA,#22D3EE,#F0ABFC);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;">
            ✦ NEURACODE ✦
        </h2>

        <p style="color:#67E8F9;font-size:10px;letter-spacing:2px;">
            INTELLIGENT CODING STUDIO
        </p>

        <p style="color:#B8C3E8;font-size:11px;">
            Think • Build • Innovate
        </p>

    </div>
    """)

    st.divider()

    st.markdown("### 🚀 WORKSPACE")

    st.radio(
        "Choose your workspace",
        list(SIDEBAR_OPTIONS.keys()),
        key="sidebar_navigation",
        on_change=sync_sidebar_page
    )

    st.divider()

    st.markdown("### ⚡ POWERED BY")
    st.markdown("🐍 Python")
    st.markdown("🔗 LangChain")
    st.markdown("🤖 Groq AI")
    st.markdown("🎨 Streamlit")

    st.divider()
    st.caption("NEURACODE • Version 2.0")


page = st.session_state.current_page


# ==================================================
# HOME PAGE
# ==================================================

if page == "Home":

    st.html("""
    <div class="hero-section">

        <div class="hero-label">
            ✦ INTELLIGENT CODING STUDIO
        </div>

        <div class="hero-title">
            NEURACODE
        </div>

        <div class="hero-tagline">
            Build. Debug. Understand. Create.
        </div>

        <div class="hero-description">
            Your ideas deserve intelligent code.
            Generate programs, debug errors,
            understand complex logic and explore programming
            with your AI-powered coding companion.
        </div>

    </div>
    """)

    st.html("""
    <div class="section-label">
        YOUR DEVELOPMENT WORKSPACE
    </div>
    """)

    st.markdown("## 🚀 Explore Your Tools")
    st.write("Select a workspace to start creating with NEURACODE.")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(key="feature_generator"):
            st.button(
                "💻  CODE GENERATOR\n\n"
                "Transform your ideas into programs in multiple languages.\n\n"
                "START GENERATING  →",
                key="card_gen",
                use_container_width=True,
                on_click=navigate_to,
                args=("Code Generator",)
            )

    with col2:
        with st.container(key="feature_debugger"):
            st.button(
                "🐞  CODE DEBUGGER\n\n"
                "Detect errors, understand issues and fix your code.\n\n"
                "START DEBUGGING  →",
                key="card_debug",
                use_container_width=True,
                on_click=navigate_to,
                args=("Code Debugger",)
            )

    col3, col4 = st.columns(2, gap="large")

    with col3:
        with st.container(key="feature_explainer"):
            st.button(
                "📖  CODE EXPLAINER\n\n"
                "Understand Python code step by step with AI.\n\n"
                "EXPLORE CODE  →",
                key="card_explain",
                use_container_width=True,
                on_click=navigate_to,
                args=("Code Explainer",)
            )

    with col4:
        with st.container(key="feature_assistant"):
            st.button(
                "🤖  AI CHAT ASSISTANT\n\n"
                "Ask questions, learn concepts and get coding help.\n\n"
                "START CHATTING  →",
                key="card_chat",
                use_container_width=True,
                on_click=navigate_to,
                args=("Chat Assistant",)
            )

    st.markdown("---")

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("### ⚡ Smart Coding")
        st.caption("Generate programming solutions faster.")

    with col_b:
        st.markdown("### 🧠 Learn Better")
        st.caption("Understand code with AI guidance.")

    with col_c:
        st.markdown("### 🚀 Build More")
        st.caption("Turn your ideas into working programs.")


# ==================================================
# CODE GENERATOR
# ==================================================

elif page == "Code Generator":

    st.title("💻 AI Code Generator")
    st.caption("Generate programs in multiple programming languages.")

    language = st.selectbox(
        "Choose Programming Language",
        ["Python", "Java", "C", "C++", "JavaScript"],
        key="generator_language"
    )

    requirement = st.text_area(
        "What do you want to build?",
        placeholder="Example: Create a calculator using functions...",
        height=150,
        key="generator_input"
    )

    if st.button(
        f"⚡ Generate {language} Code",
        key="generate_button",
        use_container_width=True
    ):

        if requirement.strip():

            with st.spinner(f"NEURACODE is generating {language} code..."):

                result = generate_response(
                    f"""You are an expert {language} developer.

Generate clean and working {language} code
for this requirement:

{requirement}

Requirements:
1. Use only {language}.
2. Include meaningful comments.
3. Follow proper coding standards.
4. Provide complete executable code.
5. Include a beginner-friendly explanation.
6. Put the code inside a correctly labelled
   {language} code block.
7. Do not mix other programming languages.
"""
                )

            save_result("Code Generator", requirement, result)

        else:
            st.warning("Please enter your requirement.")

    if (
        st.session_state.last_type == "Code Generator"
        and st.session_state.last_response
    ):

        st.markdown("### ✨ Generated Solution")
        st.markdown(st.session_state.last_response)

        extensions = {
            "Python": "py",
            "Java": "java",
            "C": "c",
            "C++": "cpp",
            "JavaScript": "js"
        }

        st.download_button(
            "📥 Download Generated Code",
            st.session_state.last_response,
            file_name=f"generated_code.{extensions[language]}",
            key="download_generated"
        )

        show_followups()


# ==================================================
# CODE DEBUGGER
# ==================================================

elif page == "Code Debugger":

    st.title("🐞 Code Debugger")
    st.caption("Find errors and improve your Python code.")

    code = st.text_area(
        "Paste your code",
        placeholder="Paste your code here...",
        height=220,
        key="debugger_input"
    )

    if st.button(
        "🔍 Debug My Code",
        key="debug_button",
        use_container_width=True
    ):

        if code.strip():

            with st.spinner("NEURACODE is analyzing your code..."):

                result = generate_response(
                    f"""You are an expert Python debugging assistant.

Analyze this code:
{code}

Identify errors, explain why they occur,
and provide corrected code."""
                )

            save_result("Code Debugger", code, result)

        else:
            st.warning("Please paste your Python code.")

    if (
        st.session_state.last_type == "Code Debugger"
        and st.session_state.last_response
    ):

        st.markdown("### 🛠️ Debugging Results")
        st.markdown(st.session_state.last_response)

        show_followups()


# ==================================================
# CODE EXPLAINER
# ==================================================

elif page == "Code Explainer":

    st.title("📖 Code Explainer")
    st.caption("Understand Python code in simple language.")

    code = st.text_area(
        "Enter Python code to explain",
        placeholder="Paste Python code here...",
        height=200,
        key="explainer_input"
    )

    if st.button(
        "🧠 Explain My Code",
        key="explain_button",
        use_container_width=True
    ):

        if code.strip():

            with st.spinner("NEURACODE is explaining your code..."):

                result = generate_response(
                    f"""Explain this Python code in beginner-friendly language.
Explain the important lines and provide a practical example.

{code}"""
                )

            save_result("Code Explainer", code, result)

        else:
            st.warning("Please enter code.")

    if (
        st.session_state.last_type == "Code Explainer"
        and st.session_state.last_response
    ):

        st.markdown("### 📚 Code Explanation")
        st.markdown(st.session_state.last_response)

        show_followups()


# ==================================================
# CHAT ASSISTANT
# ==================================================

elif page == "Chat Assistant":

    st.title("🤖 AI Chat Assistant")
    st.caption("Your personal programming assistant.")

    question = st.text_area(
        "Ask your question",
        placeholder="Example: What is a Python function?",
        height=120,
        key="chat_input"
    )

    if st.button(
        "💬 Ask NEURACODE",
        key="ask_button",
        use_container_width=True
    ):

        if question.strip():

            with st.spinner("NEURACODE is thinking..."):

                result = generate_response(
                    f"""You are a friendly programming tutor.
Answer this question clearly with practical examples:

{question}"""
                )

            save_result("Chat Assistant", question, result)

        else:
            st.warning("Please enter a question.")

    if (
        st.session_state.last_type == "Chat Assistant"
        and st.session_state.last_response
    ):

        st.markdown("### 🤖 AI Response")
        st.markdown(st.session_state.last_response)

        show_followups()


# ==================================================
# AI CODE REVIEWER
# ==================================================

elif page == "AI Code Reviewer":

    st.title("🧠 AI Code Reviewer")
    st.caption("Analyze your Python code and get improvement suggestions.")

    code_to_review = st.text_area(
        "Paste your Python code",
        placeholder="Paste your Python code here...",
        height=220,
        key="reviewer_input"
    )

    if st.button(
        "🔍 Review My Code",
        key="review_button",
        use_container_width=True
    ):

        if code_to_review.strip():

            with st.spinner("NEURACODE is reviewing your code..."):

                result = generate_response(
                    f"""You are a senior Python code reviewer.

Review the following Python code:

{code_to_review}

Provide your review using these sections:
1. Overall Code Quality
2. Errors or Potential Bugs
3. Code Readability and Best Practices
4. Performance Improvements
5. Improved Version of the Code
6. Explanation of Changes

Be accurate. Do not claim an error exists unless you can identify it.
"""
                )

            save_result("AI Code Reviewer", code_to_review, result)

        else:
            st.warning("Please paste your Python code.")

    if (
        st.session_state.last_type == "AI Code Reviewer"
        and st.session_state.last_response
    ):

        st.markdown("### ✨ Code Review Results")
        st.markdown(st.session_state.last_response)

        show_followups()


# ==================================================
# CODE OPTIMIZER
# ==================================================

elif page == "Code Optimizer":

    st.title("⚡ Code Optimizer")
    st.caption("Improve your Python code with AI-powered optimization.")

    code_to_optimize = st.text_area(
        "Paste your Python code",
        placeholder="Paste your Python code here...",
        height=220,
        key="optimizer_input"
    )

    if st.button(
        "⚡ Optimize My Code",
        key="optimizer_button",
        use_container_width=True
    ):

        if code_to_optimize.strip():

            with st.spinner("NEURACODE is optimizing your code..."):

                result = generate_response(
                    f"""You are an expert Python code optimization engineer.

Analyze and optimize the following Python code:

{code_to_optimize}

Provide your response using these sections:

1. Original Code Analysis
2. Performance Issues
3. Optimization Opportunities
4. Optimized Python Code
5. Before vs After Comparison
6. Explanation of Improvements

Requirements:
- Preserve the original functionality.
- Improve readability and efficiency.
- Use Python best practices.
- Return the optimized code in a properly formatted Python code block.
- Do not invent performance improvements.
"""
                )

            save_result("Code Optimizer", code_to_optimize, result)

        else:
            st.warning("Please paste your Python code.")

    if (
        st.session_state.last_type == "Code Optimizer"
        and st.session_state.last_response
    ):

        st.markdown("### ✨ Optimization Results")
        st.markdown(st.session_state.last_response)

        show_followups()


# ==================================================
# TEST CASE GENERATOR
# ==================================================

elif page == "Test Case Generator":

    st.title("🧪 Automatic Test Case Generator")
    st.caption("Generate test cases and pytest scripts using AI.")

    code_to_test = st.text_area(
        "Paste your Python code",
        placeholder="Paste your Python function here...",
        height=220,
        key="test_generator_input"
    )

    if st.button(
        "🧪 Generate Test Cases",
        key="test_generator_button",
        use_container_width=True
    ):

        if code_to_test.strip():

            with st.spinner("NEURACODE is generating test cases..."):

                result = generate_response(
                    f"""You are an expert Python software testing engineer.

Analyze the following Python code:

{code_to_test}

Generate a detailed testing report with these sections:

1. Code Understanding
2. Normal Test Cases
3. Edge Test Cases
4. Expected Outputs
5. Python pytest Test Script
6. Explanation of Test Cases

Requirements:
- Cover normal, boundary and invalid inputs.
- Provide accurate expected outputs.
- Generate executable pytest code.
- Do not claim tests were executed.
- Identify assumptions clearly.
"""
                )

            save_result(
                "Test Case Generator",
                code_to_test,
                result
            )

        else:
            st.warning("Please paste your Python code.")

    if (
        st.session_state.last_type == "Test Case Generator"
        and st.session_state.last_response
    ):

        st.markdown("### ✨ Test Case Results")
        st.markdown(st.session_state.last_response)

        show_followups()


# ==================================================
# CHAT HISTORY
# ==================================================

elif page == "Chat History":

    st.title("📚 Chat History")
    st.caption("Review your previous AI interactions.")

    if st.session_state.chat_history:

        for item in reversed(st.session_state.chat_history):

            with st.expander(
                f"✨ {item['type']} — {item['input'][:60]}"
            ):

                st.markdown("**Your Input**")
                st.code(item["input"])

                st.markdown("**AI Response**")
                st.markdown(item["output"])

        if st.button(
            "🗑️ Clear Chat History",
            key="clear_history"
        ):

            st.session_state.chat_history = []
            st.session_state.last_response = ""
            st.session_state.last_type = ""
            st.session_state.last_input = ""
            st.rerun()

    else:
        st.info(
            "Your chat history will appear here after your first interaction."
        )


# ==================================================
# FOOTER
# ==================================================

st.html("""
<div class="footer">

    <div class="footer-brand">
        ✦ NEURACODE ✦
    </div>

    <div class="footer-tagline">
        INTELLIGENT CODING STUDIO
    </div>

    <p style="color:#B8C3E8;font-size:12px;margin-top:12px;">
        Think • Build • Innovate
    </p>

    <p style="color:#747D9F;font-size:10px;">
        Think Smart. Code Smarter.
    </p>

</div>
""")
