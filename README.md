GoogleGmail-Skill
===================

A skill to use with Mycroft which allow to get emails from your Gmail Inbox.

----------


Install Using MSM (Mycroft Skill Manager)  not for Mark1
-------------------

    msm install https://github.com/jcasoft/GoogleGmail-Skill.git


If it does not work with the MSM method try it with the manual method
For install in Mark1 use Manual Method on Mark1
of Manual Method not for Mark1

Manual Method not for Mark1
-------------------

    cd  /opt/mycroft/skills
    git clone https://github.com/jcasoft/GoogleGmail-Skill.git
    workon mycroft (Only if you have installed Mycroft on Virtualenv)
    cd GoogleGmail-Skill
    sudo pip install -r requirements.txt

Authorize Google GMail not for Mark1
-------------------

Authorize Google GMail Skill in distro with local web browser, wait web browse open and select "Allow"

    From your command line go to mycroft skills folder

    cd  /opt/mycroft/skills
    workon mycroft
    python GoogleGmail-Skill


Edit your mycroft.conf
on "GoogleGmailSkill"  edit your options

     cd ~/mycroft/.mycroft
     sudo nano mycroft.conf


Manual Method for Mark1
-------------------

    open SSH session

    cd  /opt/mycroft/skills
    git clone https://github.com/jcasoft/GoogleGmail-Skill.git
    cd GoogleGmail-Skill
    sudo pip install -r requirements.txt


Authorize Google GMail for Mark1
-------------------
	
Authorize GoogleGMailSkill in Mark1 without local web browser

    open SSH session

    From your command line go to mycroft skills folder

    cd  /opt/mycroft/skills
    python GoogleGmail-Skill --noauth_local_webserver

Open the generated link in computer with browser and wait the verification code and paste

     Enter verification code: 4/oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   


The installation process generates automatically the file ~/.mycroft/mycroft.conf and ~/.credentials/mycroft-gmail-skill.json


Then copy the following files and fix the permissions

     sudo mkdir /home/mycroft/.credentials
     sudo cp /home/pi/.credentials/mycroft-gmail-skill.json /home/mycroft/.credentials/mycroft-gmail-skill.json
     sudo chmod -R 777 /home/mycroft/.credentials

     sudo cp /home/pi/.mycroft/mycroft.conf /home/mycroft/.mycroft/mycroft.conf
     sudo chmod -R 777 /home/mycroft/.mycroft


Edit your mycroft.conf
on "GoogleGmailSkill"  edit your options

     cd /home/mycroft/.mycroft
     sudo nano mycroft.conf


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
