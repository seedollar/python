# Example of how to use the fabric package to invoke python code.
def iso():
    from datetime import date
    print(date.today().isoformat())