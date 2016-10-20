**GoogleGmail-Skill**
===================


An skill to use with Mycroft which allow to get your emails from your Gmail Inbox.

----------


Installation
-------------------
Is necesary to make this procedure two times

outside mycroft virtual environment for python 2

    pip install google-api-python-client apiclient oauth2client httplib2
	
    or 

    pip2 install google-api-python-client apiclient oauth2client httplib2


Now enter inside mycroft virtual environment

Inside mycroft virtual environment

    workon mycroft

    pip install google-api-python-client apiclient oauth2client httplib2


Now go to Mycroft third party skill directory

    cd  /opt/mycroft/third_party/

    git clone  https://github.com/jcasoft/GoogleGmail-Skill.git mycroft-gmail-skill

<i class="icon-cog"></i>Add 'GoogleGmail-Skill' section in your Mycroft configuration file on:

    $HOME/.mycroft/mycroft.ini


	[GoogleGmailSkill]
	loginEnabled = True
	maxResults = 10
	timeFormat = 12		# 12 for AM/PM and 24 for 24 hours time format


Authorize Google GMail Skill in distro with local web browser, wait web browse open and select "Allow"

    From your command line go to third_party folder skill

    cd /opt/mycroft/third_party

    python mycroft-gmail-skill

	
Authorize Google Calendar Skill in distro without local web browser

    From your command line go to third_party folder skill

    cd /opt/mycroft/third_party

    python mycroft-gmail-skill --noauth_local_webserver

Open the generated link in computer with browser and wait the verification code and paste

     Enter verification code: 4/oxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   



Restart Skills

    ./start.sh skills

----------


Features
--------------------

Currently this skill can do the following things to get information from your calendar (with some variation):

- Check my gmail
- Get my last gmail
- Get my last gmail complete 
- Get my last gmail detailed
- Get my last gmail with detail 
- Get my last gmail with body   
- Get my last 5 gmail
- Get my last 5 gmail complete 
- Get my last 5 gmail detailed
- Get my last 5 gmail with detail 
- Get my last 5 gmail with body
- Get my gmail


> **Note:**

> - You can toggle key word with:
> - The words: complete, detailes, with detail, with body; offer the same results




**Enjoy !**
--------