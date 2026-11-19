
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Page Configuration
st.set_page_config(
    page_title="AI Python Code Generator",
    page_icon="🐍",
    layout="wide"
)

# Application Title
st.title("🐍 AI Python Code Generator")
st.write("Generate Python code automatically using AI!")

# API Key
api_key = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password"
)

# User Input
st.subheader("Enter Your Coding Requirement")

requirement = st.text_area(
    "What code do you want?",
    placeholder="Example: Create a Python calculator"
)

# Generate Code
if st.button("Generate Code"):

    if not api_key:
        st.warning("Please enter your Gemini API key.")

    elif not requirement.strip():
        st.warning("Please enter your requirement.")

    else:
        try:
            with st.spinner("AI is generating your code..."):

                # Initialize Gemini
                llm = ChatGoogleGenerativeAI(
                    model="gemini-3.8-flash",
                    google_api_key=api_key,
                    temperature=0.2
                )

                # Create Prompt Template
                prompt = PromptTemplate(
                    input_variables=["requirement"],
                    template="""
                    You are an expert Python developer.

                    Generate complete Python code
                    based on this requirement:

                    {requirement}

                    Include:
                    1. Complete Python code
                    2. Explanation
                    3. Required libraries
                    4. Execution steps
                    """
                )

                # LangChain Chain
                chain = prompt | llm | StrOutputParser()

                # Generate Response
                response = chain.invoke({
                    "requirement": requirement
                })

            st.success("Code generated successfully!")

            st.markdown("## AI Generated Output")
            st.markdown(response)

            # Download Output
            st.download_button(
                "Download Generated Code",
                data=response,
                file_name="generated_code.md",
                mime="text/markdown"
            )

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Built with Python | LangChain | Streamlit | Gemini")
