# Checker viber user status  

# NOTE! 
The current version of the script just work under windows 10 where installed official viber

# Prerequisites
1. Change viber lang to English - other lang the script does not support

# Setup and Run

1. setup python 3.8 on windows 10 (https://www.python.org/downloads/release/python-387/) and check in CMD #python --version
2. clone project from GitHub  git clone git@github.com:erachkov/viber_user_checker.git or download
    
    C:\>mkdir Project  
    
    C:\>cd Project  
    
    C:\Project>git clone git@github.com:erachkov/viber_user_checker.git 
    
    C:\Project>cd viber_user_checker 


3. run in CMD

C:\Project\viber_user_checker>virtualenv venv

C:\Project\viber_user_checker>.\env\Scripts\activate

pip install -r requirements.txt

4. update src/config/param.yml - add your list

5. run program
   C:\Project\viber_user_checker\src>cd src
   C:\Project\viber_user_checker\src>python src/bot.py

