import re

class Security:

    @staticmethod
    def clean_text(text):

        text=str(text)
        text=re.sub(r'[^a-zA-Z0-9 ]','',text)

        return text.lower()