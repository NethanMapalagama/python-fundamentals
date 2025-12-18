Emails = open(
    "C:/Users/netha/Desktop/vs code/python/Invalid Emails question/emails.txt", "r"
)
Invalid = open(
    "C:/Users/netha/Desktop/vs code/python/Invalid Emails question/InvalidEmails.txt",
    "a",
)

while True:

    ErrorCount = 2
    email = Emails.readline()

    if not email:
        break

    email = email.strip()  # Remove newline
    suffix = email[-4:]

    if suffix[:1] == ".":
        ErrorCount = ErrorCount - 1

    found = False
    i = 0

    while i <= (len(email) - 1) and found == False:
        if email[i] == "@":
            found = True
            ErrorCount = ErrorCount - 1
        i = i + 1

    if ErrorCount > 0:
        Invalid.write(f"{email} {ErrorCount}\n")


Emails.close()
Invalid.close()
