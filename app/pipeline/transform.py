# Transform file, not entirely sure how to integrate yet, but I guess we'll see how it goes

def transform(df):
    df["is_flagged"] = df["amount"] > 900
    return df
