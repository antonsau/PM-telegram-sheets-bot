# Project management bot

Actually, it's being used for saving all insights, news, projects which our team consider interesting for further analysis.
It saves messages to Google Sheets file. Our team uses it in so called DeFi pipeline (analysing, monitoring and performing tasks, searching for investment and speculation opportunities).

UPD. It also sends daily and weekly reminders to the team chat.

1. Download the repo.
2. Create the virtual environment for the cloned repo. Run the command "pip3 -m venv env".
3. Install requried dependencies. Run the command "pip3 install -r requirements.txt".
4. Update jsonexample files*.
5. Grant access for the service account to the Google Sheets file.
6. Update spreadsheet.py (the inserted row is created there).
7. Run main.py (if running in the terminal do not forget to activate virtual environment)


*To get serviceaccount.json, please check Google Workspace Admin Help (https://support.google.com/a/answer/7378726?hl=en)
