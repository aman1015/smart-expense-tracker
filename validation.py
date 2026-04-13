import pandas as pd

class Validator:

    REQUIRED = ["date","description","amount","type"]

    @staticmethod
    def validate(df):

        errors=[]

        for col in Validator.REQUIRED:
            if col not in df.columns:
                errors.append(f"Missing column {col}")

        if "amount" in df:
            if not pd.to_numeric(df["amount"],errors="coerce").notnull().all():
                errors.append("Invalid amount values")

        if "type" in df:
            if not df["type"].isin(["credit","debit"]).all():
                errors.append("type must be credit/debit")

        return errors