import time
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(
    page_title="AI Python Coding Assistant",
    page_icon="🐍",
    layout="wide"
)

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
# Sidebar
st.sidebar.title("🐍 AI Coding Assistant")
st.sidebar.write("Your personal AI developer")

page = st.sidebar.radio(
    "Navigation",
    [
        "Code Generator",
        "Code Debugger",
        "Code Explainer",
        "Chat Assistant",
        "Chat History"
    ]
)

# Main page
api_key = st.sidebar.text_input(
    "Gemini API Key",
    type="password"
)

def generate_code(requirement):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=api_key,
        temperature=0.2
    )

    prompt = PromptTemplate(
        input_variables=["requirement"],
        template="""
        You are an expert Python developer.

        Generate complete Python code for:
        {requirement}

        Return:
        1. Complete Python code
        2. Explanation
        3. Required libraries
        4. How to run the code
        """
    )

    chain = prompt | llm | StrOutputParser()

    for attempt in range(3):
        try:
            response = chain.invoke({
                "requirement": requirement
            })

            if not response:
                raise ValueError("AI returned an empty response")

            return response

        except Exception as e:
            error_message = str(e)

            if ("503" in error_message or "UNAVAILABLE" in error_message) and attempt < 2:
                time.sleep(2 ** (attempt + 1))
            else:
                raise
    
st.title("🐍 AI Python Coding Assistant")
st.write("Welcome! Build Python programs with the help of AI.")

st.divider()


if page == "Code Generator":

    st.header("💻 AI Code Generator")

    requirement = st.text_area(
        "Describe what code you want:",
        placeholder="Example: Create a Python calculator",
        height=150
    )

    if st.button("🚀 Generate Code"):

        if not api_key:
            st.warning("Enter your Gemini API key.")

        elif not requirement.strip():
            st.warning("Enter your requirement.")

        else:
            try:
                with st.spinner("AI is generating code..."):

                    response = generate_code(requirement)

                st.success("Code generated successfully!")
                st.markdown(response)
                
                st.session_state.chat_history.append({
                 "feature": "Code Generator",
                 "question": requirement,
                 "answer": response
        })

                st.download_button(
                    "Download Generated Code",
                    data=response,
                    file_name="generated_code.md"
                )

            except Exception as e:
                st.error(str(e))

elif page == "Code Debugger":

    st.header("🐛 AI Code Debugger")

    code = st.text_area("Paste your Python code:")
    error = st.text_area("Paste your error message:")

    if st.button("Fix My Code"):

        if not api_key:
            st.warning("Enter your Gemini API key.")

        elif not code.strip():
            st.warning("Paste your Python code.")

        else:
            try:
                with st.spinner("AI is debugging your code..."):

                    response = generate_code(
                        f"""
                        Debug this Python code.

                        Code:
                        {code}

                        Error:
                        {error}

                        Explain the error and provide corrected code.
                        """
                    )

                st.success("Debugging completed!")
                st.markdown(response)

                st.session_state.chat_history.append({
                    "feature": "Code Debugger",
                    "question": code,
                    "answer": response
                })

            except Exception as e:
                st.error(str(e))

elif page == "Code Explainer":

    st.header("📖 AI Code Explainer")

    code = st.text_area("Paste Python code to explain:")

    if st.button("Explain Code"):

        if not api_key:
            st.warning("Enter your Gemini API key.")

        elif not code.strip():
            st.warning("Paste Python code.")

        else:
            try:
                with st.spinner("AI is explaining your code..."):

                    response = generate_code(
                        f"""
                        Explain this Python code step by step
                        in simple language.

                        Code:
                        {code}
                        """
                    )

                st.success("Explanation completed!")
                st.markdown(response)

                st.session_state.chat_history.append({
                    "feature": "Code Explainer",
                    "question": code,
                    "answer": response
                })

            except Exception as e:
                st.error(str(e))

elif page == "Chat Assistant":

    st.header("💬 AI Chat Assistant")

    question = st.text_input("Ask your Python question:")

    if st.button("Send"):

        if not api_key:
            st.warning("Enter your Gemini API key.")

        elif not question.strip():
            st.warning("Enter your question.")

        else:
            try:
                with st.spinner("AI is thinking..."):

                    response = generate_code(
                        f"Answer this Python-related question in simple language: {question}"
                    )

                st.success("Response generated!")
                st.markdown(response)

                st.session_state.chat_history.append({
                    "feature": "Chat Assistant",
                    "question": question,
                    "answer": response
                })

            except Exception as e:
                st.error(str(e))

elif page == "Chat History":

    st.header("🕘 Chat History")
    
    if st.session_state.chat_history:

     if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

    if st.session_state.chat_history:

        for i, chat in enumerate(
            reversed(st.session_state.chat_history), 1
        ):
            st.subheader(f"Conversation {i}")
            st.write("Feature:", chat["feature"])
            st.write("Question:", chat["question"])

            with st.expander("View AI Response"):
                st.markdown(chat["answer"])

            st.divider()

    else:
        st.info("No conversation history available yet.")

st.divider()

st.caption("Built with Python | Streamlit | LangChain | Google Gemini")

