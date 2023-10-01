import json
import requests
import uuid
import hashlib
import re


class TempMail:
    def __init__(self, email):
        self.email = email[0]
        self.hashed_email = email[1]

    def display_email_info(self):
        print("Email:", self.email)
        print("Hashed Email:", self.hashed_email)

    def get_mail_attribute(self):
        url = "https://api.apilayer.com/temp_mail/mail/id/" + self.hashed_email

        payload = {}
        headers = {
            "apikey": "sRtO9gC2pzCtUes2KwZuZCpss6BC2X33"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.ok:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if the response is a list
            if isinstance(data, list):
                mail_ids = []
                password_links = []
                passwords = []

                # Adjust the URL pattern to capture only the varying part of the URL (the code)
                url_pattern = r'http[s]?://api.dev.lotika.ru/Users/ResetConfirm\?code=[a-zA-Z0-9]+'

                # Define the regular expression pattern to find passwords with the format vmuDunDVwicV
                password_pattern = r'[a-zA-Z0-9]{12}'

                # Iterate through each dictionary in the list
                for entry in data:
                    mail_id = entry.get("mail_id")
                    mail_text = entry.get("mail_text")
                    if mail_id:
                        mail_ids.append(mail_id)
                    if mail_text:
                        # Find all URLs that match the pattern
                        urls_found = re.findall(url_pattern, mail_text)
                        # Extract the code from each URL and store the full URL in password_links
                        password_links.extend(urls_found)

                        # Find all passwords that match the pattern
                        passwords_found = re.findall(password_pattern, mail_text)
                        passwords.extend(passwords_found)

                # Return the last mail_id found in the list (or None if the list is empty)
                return response.status_code, response.text, mail_ids[
                    -1] if mail_ids else None, password_links, passwords
            else:
                # If the response is a dictionary, directly extract the "mail_id" value and password reset link
                mail_id = data.get("mail_id")
                mail_text = data.get("mail_text")
                url_pattern = r'http[s]?://api.dev.lotika.ru/Users/ResetConfirm\?code=[a-zA-Z0-9]+'
                url_found = re.findall(url_pattern, mail_text)

                # Find all passwords that match the pattern
                password_pattern = r'[a-zA-Z0-9]{12}'
                passwords_found = re.findall(password_pattern, mail_text)

                return response.status_code, response.text, mail_id, url_found[
                    0] if url_found else None, passwords_found
        else:
            return response.status_code, response.text, None, None, None
    def get_mail_attachments(self): pass



#email_data = random_email()
new_mail = TempMail(['shumak.romashchuk@cevipsa.com', '4cc768a14846eb2f54447d74697d0ae2'])
new_mail.display_email_info()
status_code, result, mail_id, password_links, passwords = new_mail.get_mail_attribute()
print("Status Code:", status_code)
print("Response:", result)
print("Last mail ID:", mail_id)
print("Password Links:", password_links)
print("Password:", passwords[-1])