"""
This application contains the code related to the
new electric car application.
"""

__author__ = 'Surendra Reddy'
__version__ = '1.0'
__maintainer__ = 'Surendra Reddy'
__email__ = 'surendraelectronics@gmail.com'
__status__ = 'Prototype'

print('# ' + '=' * 78)
print('Author: ' + __author__)
print('Version: ' + __version__)
print('Maintainer: ' + __maintainer__)
print('Email: ' + __email__)
print('Status: ' + __status__)
print('# ' + '=' * 78)

# Required packages importing
import streamlit as st

# Header template
html_temp = """
    <body style="background-color:red;">
    <div style="background-color:tomato;padding:10px">
    <h3 style="color:white;text-align:center;"> Azure Resource Naming tool</h3>
    </div>
    </body>
"""
# Hide Styles
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
# Page Config details
st.set_page_config(
        page_title = 'azureresourcenaming',
        page_icon = "🌩️",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

def main():
    """
    This function contains the streamlit code details
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write('\n')

    st.header("Azure Resource Namer")
    st.write("A simple tool to help you name your Azure resources, based on the [Cloud Adoption Framework naming convention](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)")

    st.write('---')


# main function call
if __name__ == '__main__':
    main()