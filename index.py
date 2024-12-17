import streamlit as st
from openai import OpenAI

# Set the GPT API Key securely
client = OpenAI(
    api_key=st.secrets["pass"],  # This is the default and can be omitted
)
# Streamlit app title
st.title("🔍 Scientific Text Summarizer with GPT-4")

# Text Input for Article
article_text = st.text_area("📝 Enter your scientific text to summarize:", height=200)

# Output size selection
output_size = st.radio(
    label="🔧 Choose the summary length:",
    options=["To-The-Point", "Concise", "Detailed"],
    horizontal=True
)

# Map output size to token limit
output_token_map = {"To-The-Point": 50, "Concise": 128, "Detailed": 516}
out_token = output_token_map[output_size]

# Generate Summary Button

if st.button("✨ Generate Summary", type="primary"):
    try:
        # Call GPT-4 ChatCompletion API
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant summarizing scientific articles."},
                {"role": "user", "content": f"Summarize this text in {output_size} style:\n\n{article_text}"}
            ],
            model="gpt-4o-mini",
        )
        # openai.ChatCompletion.create(
        #     model="gpt-4",  # Use the GPT-4 model
        #     messages=[
                
        #     ],
        #     max_tokens=out_token,
        #     temperature=0.5,
        # )
        # Extract the summary
        print('\n\n\n',response)
        res = response.choices[0].message.content

        # Display the result
        st.success("**Summary:**")
        st.write(res)

        # Download button for the summary
        st.download_button("💾 Download Summary", res, file_name="summary.txt", mime="text/plain")

    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")

# Appreciation Section
if st.checkbox("🎉 Show Appreciation"):
    st.success("You're doing a great job learning Streamlit and OpenAI! 🚀")
