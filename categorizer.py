class Categorizer:

    RULES = {
    "salary":"Income",
    "swiggy":"Food",
    "zomato":"Food",
    "uber":"Travel",
    "ola":"Travel",
    "amazon":"Shopping",
    "netflix":"Entertainment",
    "spotify":"Entertainment",
    "electricity":"Bills"
    }

    @staticmethod
    def categorize(text):

        text=text.lower() 

        for k,v in Categorizer.RULES.items():
            if k in text:
                return v

        return "Other"