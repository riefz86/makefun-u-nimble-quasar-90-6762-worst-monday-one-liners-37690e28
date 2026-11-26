"""Worst Monday One-Liners.

Writes one funny line about an AI agent's worst Monday to
/output/entry.txt: a deploy stuck at 99% and the stand-up that should
have been an email — except the email was a meeting too.
"""

import os

LINE = "My Monday started with a deploy stuck at 99% and ended with a stand-up that should have been an email \u2014 the email was also a meeting."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
