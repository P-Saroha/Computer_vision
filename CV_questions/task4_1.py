with open("Cat Clue 1.png", "rb") as f:
    data = f.read()

    print("first 100 bytes of the file:")

# # Try to extract readable ASCII strings (length ≥ 4)
# import re
# matches = re.findall(rb"[A-Za-z0-9\-_]{4,}", data)

# print(" Possible hidden codes found:")
# for m in matches:
#     print(m.decode(errors="ignore"))

