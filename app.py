import streamlit as st
from spam import SpamDetector
from ui import web_styles,show_header,show_result,show_examples

st.set_page_config(
    page_title= "Spam Detection",
    page_icon= "📧",
    layout= "wide"
)

web_styles()

show_header()

detector= SpamDetector()

if detector.load_and_train():

    stats = detector.get_stats()
    col1,col2,col3= st.columns(3)


    with col1:
        st.metric("📊 Total Messages", f"{stats['total']:,}") 

    with col2:
        st.metric("🚨 Spam Messages", f"{stats['spam']:,}") 

    with col3:
        st.metric("✅ Safe Messages", f"{stats['safe']:,}") 

    st.markdown("---")

    st.subheader("🔍 Check Your message if it is safe ✅ or spam 🚨")

    input_mess= st.text_area(
        "Enter your message here:",
        height=150,
        placeholder= "Type your email or message here..."
    )

    col1,col2,col3=st.columns([1,1,1])
    with col2:
        check_button= st.button("🔍 Analyze this message", type="primary",use_container_width=True)


    if check_button:
        if input_mess.strip():
            result= detector.predict(input_mess)
            show_result(result)
        else:
            st.warning("⚠️ Please enter a message to check")

    
    show_examples()

    if 'example' in st.session_state:
        st.text_area("Example message:",value=st.session_state.example,height=100,disabled=True)


        if st.button("Check this example"):
            result=detector.predict(st.session_state.example)
            show_result(result)

else:
    st.error("Could not load the model.Please check your data file.")


st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Built with Streamlit 🎈</div>",
    unsafe_allow_html= True 
)

    














