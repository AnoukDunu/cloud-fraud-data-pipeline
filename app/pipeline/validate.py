# Temp validation function. Will implement more later
def validate(df):
    assert df.isnull().sum().sum() == 0
    assert (df["amount"] > 0).all()