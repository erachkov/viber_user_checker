# viber_user_checker

# Setup

1. setup python 3.8 on windows 10 (https://www.python.org/downloads/release/python-387/) and check in CMD #python --version
2. clone project from GitHub  git clone git@github.com:erachkov/viber_user_checker.git or download
    e.g.
    C:\>mkdir Project  
    C:\>cd Project  
    C:\Project>git clone git@github.com:erachkov/viber_user_checker.git
    Cloning into 'viber_user_checker'...

3. CD to viber_user_checker
4. run in CMD

C:\Project\viber_user_checker>virtualenv venv
C:\Project\viber_user_checker>.\env\Scripts\activate
pip install -r requirements.txt

5. update src/config/param.yml - add your list
6. run program
   C:\Project\viber_user_checker\src>cd src
   C:\Project\viber_user_checker\src>python src/bot.py

