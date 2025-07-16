import streamlit as st

def web_styles():
    st.markdown("""
    <style>
     .main-title{
            text-align: center;
            background: linear-gradient(90deg, #e74c3c, #3498db);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .result-spam {
            background-color: #ffebee;
            border: 2px solid #f44336;
            color: #d32f2f;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin: 20px 0;
        }
        
        .result-safe {
            background-color: #e8f5e8;
            border: 2px solid #4caf50;
            color: #2e7d32;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin: 20px 0;
        }
        
        .example-box {
            background-color: #f0f8ff;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #2196F3;
            margin: 20px 0;
        }
        
        .info-text {
            text-align: center;
            color: #666;
            font-size: 14px;
            margin: 10px 0;
        }
    </style>
    """, unsafe_allow_html=True)

    

def show_header():
    st.markdown("""
    <div class="main-title">
        <h1>📧 Email Spam Detection</h1>
        <p>Check if your message is spam or not 🚨 </p>
    </div>
    """,unsafe_allow_html=True)

def show_result(result):
    if result== 'Spam':
        st.markdown("""
        <div class="result-spam">
            🚨 Spam Detected!!<br>
            This message looks spam.Be careful!!
        </div>
        """,unsafe_allow_html=True)

    else:
         st.markdown("""
        <div class="result-safe">
            ✅ Safe Message!!<br>
            This message looks Safe.Check now!!
        </div>
        """,unsafe_allow_html=True)

def show_examples():
    st.markdown("---")
    st.subheader("📝 Want to try examples?")


    col1,col2= st.columns(2)

    with col1:
        st.markdown("""
        <div class="example-box">
            <h4>✅ Safe message example</h4>
            <p>Normal Conversation message</p>
        </div>
        """,unsafe_allow_html=True)

        if st.button("Try Safe Message",use_container_width=True):
            st.session_state.example= "Hi, I hope you're doing well. I wanted to follow up on our meeting yesterday and discuss the project details."

    with col2:
        st.markdown("""
        <div class="example-box">
            <h4>🚨 Spam message example</h4>
            <p>A spam message</p>
        </div>
        """,unsafe_allow_html=True)

        if st.button("Try Spam Message",use_container_width=True):
            st.session_state.example= "Congratulations! You won a lottery! Please click on this link to claim the lottery prize."


def show_info_box(title,content):
    st.markdown(f"""
        <div class="example-box">
            <h4>{title} </h4>
            <p>{content}</p>
        </div>
        """,unsafe_allow_html=True)




    
        
        

