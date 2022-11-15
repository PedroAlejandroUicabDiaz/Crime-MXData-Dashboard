import streamlit as st


def crime_bullets(warn:str, blt_1:str|float|int, blt_2:str|float|int):
    print(warn, blt_1, blt_2)
    st.markdown(
        """
        <style>
            .container {
                display:flex;
                justify-content: space-between;
                margin-left: 30px;
                margin-right: 30px;
                margin-bottom: 30px;
            }
            
            .bullet {
            }

            .bullet_title {
                text-align: center;
                font-size: 20;
                font-weight:bold;
            }

            .bullet_text {
                text-align: center;
            }
        </style>

        <div class='container'>
            <div class='bullet'>
                <div class='bullet_title'>Security</div>
                <div class='bullet_text'>"""+f"{warn}"+"""</div>
            </div>
            <div class='bullet'>
                <div class='bullet_title'>Homicides</div>
                <div class='bullet_text'>"""+f"{blt_1}"+"""</div>
            </div>
            <div class='bullet'>
                <div class='bullet_title'>Zones</div>
                <div class='bullet_text'>"""+f"{blt_2}"+"""</div>
            </div>
        </div>
        """
        , unsafe_allow_html=True)
