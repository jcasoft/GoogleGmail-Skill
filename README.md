GoogleGmail-Skill
===================

A skill to use with Mycroft which allow to get emails from your Gmail Inbox.

----------


Install Using MSM (Mycroft Skill Manager)
-------------------

    msm install https://github.com/jcasoft/GoogleGmail-Skill.git



Install Manualy
-------------------

    cd  /opt/mycroft/skills
    git clone  https://github.com/jcasoft/GoogleGmail-Skill.git
    workon mycroft
    pip install -r requirements.txt


Authorize Google GMail
-------------------

Authorize Google GMail Skill in distro with local web browser, wait web browse open and select "Allow"

    From your command line go to mycroft skills folder

    cd  /opt/mycroft/skills
    workon mycroft
    python GoogleGmail-Skill

	
Authorize GoogleGMailSkill in distro without local web browser

    From your command line go to mycroft skills folder

    cd  /opt/mycroft/skills
    workon mycroft
    python skill-gmail --noauth_local_webserver

Open the generated link in computer with browser and wait the verification code and paste

     Enter verification code: 4/oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   




Edit your ~/.mycroft/mycroft.conf

on "GoogleGmailSkill" section (added automatically)

Restart Mycroft

./stop-mycroft.sh

./start-mycroft.sh debug


----------


Features
--------------------

Currently this skill can do the following things to get information from your Gmail Inbox, un-read e-mails (with some variation):

- Check my gmail
- Get my last gmail
- Get my last gmail complete 
- Get my last gmail detailed
- Get my last gmail with detail 
- Get my last gmail with body   
- Get my last 5 gmail
- Get my last 6 gmail complete 
- Get my last 7 gmail detailed
- Get my last 8 gmail with detail 
- Get my last 9 gmail with body
- Get my gmail


> **Note:**

> - You can toggle key word with:
> - The words: complete, detailed, with detail, with body; offer the same results




**Enjoy !**
--------
