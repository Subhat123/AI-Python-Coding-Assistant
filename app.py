
import streamlit as st
from langchain_groq import ChatGroq

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="NEURACODE | AI Coding Studio",
    page_icon="⚡",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #080D1C, #11152C, #17112D);
    color: #F4F5FF;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #FFFFFF !important;
}

p, label, li {
    color: #CBD2ED;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #10172D, #211638);
    border-right: 1px solid #34365F;
}

section[data-testid="stSidebar"] * {
    color: #EEEEFF;
}

.stButton > button {
    background: linear-gradient(90deg, #7547FF, #00B8D9);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.65rem 1rem;
    font-weight: 700;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 7px 22px #7547FF66;
    border: 1px solid #8EEEFF;
}

div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
    background: #151C35;
    color: white;
    border: 1px solid #55518B;
    border-radius: 10px;
}

.feature-card {
    background: linear-gradient(145deg, #1A2340, #211A3D);
    border: 1px solid #484477;
    border-radius: 18px;
    padding: 22px;
    min-height: 155px;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px #00000033;
    margin-bottom: 12px;
}

.feature-card:hover {
    transform: translateY(-6px);
    border-color: #00D5FF;
    box-shadow: 0 10px 28px #7547FF44;
}

.feature-icon {
    font-size: 34px;
}

.feature-title {
    font-size: 20px;
    font-weight: 800;
    color: #FFFFFF;
    margin-top: 10px;
}

.feature-description {
    font-size: 14px;
    color: #BFC9E8;
    margin-top: 8px;
}

.brand-banner {
    background: linear-gradient(110deg, #30205B, #123B59);
    border: 1px solid #55518B;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 25px;
}

.followup-card {
    background: #171F3B;
    border: 1px solid #3D5684;
    border-radius: 12px;
    padding: 13px;
    margin: 7px 0;
}

hr {
    border-color: #34365F;
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# SESSION STATE
# ==================================================

if "navigation" not in st.session_state:
    st.session_state.navigation = "Home"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_response" not in st.session_state:
    st.session_state.last_response = ""

if "last_input" not in st.session_state:
    st.session_state.last_input = ""

if "last_type" not in st.session_state:
    st.session_state.last_type = ""

if "followup_prompt" not in st.session_state:
    st.session_state.followup_prompt = ""


def navigate_to(target):
    st.session_state.navigation = target


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
    st.markdown("### ✨ Continue Your Journey")
    st.caption("Explore more with these AI-powered follow-up actions.")

    suggestions = [
        "Explain this in a beginner-friendly way",
        "Show a practical example",
        "Improve and optimize this solution"
    ]

    for i, suggestion in enumerate(suggestions):

        if st.button(
            f"💡 {suggestion}",
            key=f"followup_{st.session_state.last_type}_{i}",
            use_container_width=True
        ):

            with st.spinner("NEURACODE AI is working..."):

                result = generate_response(
                    f"""Previous task:
{st.session_state.last_input}

Previous AI response:
{st.session_state.last_response}

Follow-up request:
{suggestion}

Give a helpful, clear answer."""
                )

            save_result(
                st.session_state.last_type,
                suggestion,
                result
            )

            st.rerun()


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center;padding:15px 2px;">
        <div style="
            font-size:29px;
            font-weight:900;
            letter-spacing:2px;
            background:linear-gradient(90deg,#A78BFA,#22D3EE,#F0ABFC);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;">
            ✦ NEURACODE ✦
        </div>
        <div style="
            color:#67E8F9;
            font-size:10px;
            letter-spacing:2px;
            margin-top:8px;">
            INTELLIGENT CODING STUDIO
        </div>
        <div style="
            color:#B8C3E8;
            font-size:11px;
            margin-top:8px;">
            Think • Build • Innovate
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "WORKSPACE NAVIGATION",
        [
            "Home",
            "Code Generator",
            "Code Debugger",
            "Code Explainer",
            "Chat Assistant",
            "Chat History"
        ],
        key="navigation"
    )

    st.divider()

    st.markdown("### ⚡ POWERED BY")
    st.markdown("🐍 Python")
    st.markdown("🔗 LangChain")
    st.markdown("🤖 Groq AI")
    st.markdown("🎨 Streamlit")

    st.divider()

    st.caption("NEURACODE • Version 1.0")


# ==================================================
# HOME PAGE
# ==================================================

if page == "Home":

    st.markdown("""
    <div class="brand-banner">
        <h1>⚡ Welcome to NEURACODE</h1>
        <h3 style="color:#67E8F9 !important;">
            Think Smart. Code Smarter.
        </h3>
        <p>
            Your intelligent AI-powered Python development studio.
            Generate smarter code, debug errors and understand
            programming with your personal AI assistant.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Explore Your Workspace")

    st.write("Choose a tool and start building smarter Python solutions.")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💻</div>
            <div class="feature-title">Code Generator</div>
            <div class="feature-description">
                Transform your ideas into clean Python code with AI.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Open Code Generator", key="home_gen", use_container_width=True):
            navigate_to("Code Generator")
            st.rerun()

    with col2:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🐞</div>
            <div class="feature-title">Code Debugger</div>
            <div class="feature-description">
                Detect errors, understand issues and fix your code.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔧 Open Code Debugger", key="home_debug", use_container_width=True):
            navigate_to("Code Debugger")
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📖</div>
            <div class="feature-title">Code Explainer</div>
            <div class="feature-description">
                Understand complex Python code step by step.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📚 Open Code Explainer", key="home_explain", use_container_width=True):
            navigate_to("Code Explainer")
            st.rerun()

    with col4:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI Chat Assistant</div>
            <div class="feature-description">
                Ask questions and explore programming concepts.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("💬 Open AI Assistant", key="home_chat", use_container_width=True):
            navigate_to("Chat Assistant")
            st.rerun()

    st.divider()

    st.markdown("### ✨ Your Ideas. Our Intelligence.")
    st.caption("Start creating something amazing with NEURACODE.")


# ==================================================
# CODE GENERATOR
# ==================================================

elif page == "Code Generator":

    st.title("💻 Code Generator")
    st.caption("Turn your ideas into Python programs.")

    requirement = st.text_area(
        "What do you want to build?",
        placeholder="Example: Create a Python calculator using functions...",
        height=150
    )

    if st.button("⚡ Generate Python Code", use_container_width=True):

        if requirement.strip():

            with st.spinner("NEURACODE is generating your solution..."):

                result = generate_response(
                    f"""You are an expert Python developer.

Generate clean and working Python code for this requirement:
{requirement}

Include comments and a short explanation.
Present the code in a Python code block."""
                )

            save_result("Code Generator", requirement, result)

        else:
            st.warning("Please enter your requirement.")

    if st.session_state.last_type == "Code Generator" and st.session_state.last_response:

        st.markdown("### ✨ Generated Solution")
        st.markdown(st.session_state.last_response)

        st.download_button(
            "📥 Download Generated Code",
            st.session_state.last_response,
            file_name="generated_code.py"
        )

        show_followups()


# ==================================================
# CODE DEBUGGER
# ==================================================

elif page == "Code Debugger":

    st.title("🐞 Code Debugger")
    st.caption("Find errors and improve your Python code.")

    code = st.text_area(
        "Paste your Python code",
        placeholder="Paste your code here...",
        height=220
    )

    if st.button("🔍 Debug My Code", use_container_width=True):

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

    if st.session_state.last_type == "Code Debugger" and st.session_state.last_response:

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
        height=200
    )

    if st.button("🧠 Explain My Code", use_container_width=True):

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

    if st.session_state.last_type == "Code Explainer" and st.session_state.last_response:

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
        height=120
    )

    if st.button("💬 Ask NEURACODE", use_container_width=True):

        if question.strip():

            with st.spinner("NEURACODE is thinking..."):

                result = generate_response(
                    f"""You are a friendly Python programming tutor.
Answer this question clearly with practical examples:

{question}"""
                )

            save_result("Chat Assistant", question, result)

        else:
            st.warning("Please enter a question.")

    if st.session_state.last_type == "Chat Assistant" and st.session_state.last_response:

        st.markdown("### 🤖 AI Response")
        st.markdown(st.session_state.last_response)

        show_followups()


# ==================================================
# CHAT HISTORY
# ==================================================

elif page == "Chat History":

    st.title("📚 Chat History")
    st.caption("Review your previous AI interactions.")

    if st.session_state.chat_history:

        for index, item in enumerate(reversed(st.session_state.chat_history)):

            with st.expander(
                f"✨ {item['type']} — {item['input'][:60]}"
            ):

                st.markdown("**Your Input**")
                st.code(item["input"])

                st.markdown("**AI Response**")
                st.markdown(item["output"])

        if st.button("🗑️ Clear Chat History"):

            st.session_state.chat_history = []
            st.session_state.last_response = ""
            st.session_state.last_type = ""
            st.rerun()

    else:
        st.info("Your chat history will appear here after your first interaction.")


# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown("""
<div style="text-align:center;padding:15px;">
    <h2 style="
        background:linear-gradient(90deg,#A78BFA,#22D3EE);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;">
        ✦ NEURACODE ✦
    </h2>
    <p style="color:#A5B4FC;">
        Think Smart. Code Smarter.
    </p>
    <p style="color:#8993B5;font-size:12px;">
        Powered by Python • LangChain • Groq AI • Streamlit
    </p>
</div>
""", unsafe_allow_html=True)
