import streamlit as st
from transformers import pipeline

st.title("🧠 Next Sentence Predictor")
st.write("Type a sentence and I'll predict what comes next!")

user_input = st.text_input("Enter your sentence:", "The weather today is")
num_predictions = st.slider("How many predictions?", 1, 5, 3)

if st.button("Predict"):
    with st.spinner("Generating..."):
        generator = pipeline("text-generation", model="gpt2")
        results = generator(
            user_input,
            max_new_tokens=30,
            num_return_sequences=num_predictions
        )
    st.subheader("Predictions:")
    for i, result in enumerate(results, 1):
        full_text = result["generated_text"]
        new_text = full_text[len(user_input):]
        st.markdown(f"**{i}.** {user_input} *{new_text}*")
