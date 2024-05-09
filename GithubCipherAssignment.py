import sys
if len(sys.argv) == 2:
  key = sys.argv[1]
  message = input()
  message = message.upper()
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  onlyAlpha = ""

for i in range(len(message)):
  if message[i].isalpha():
    onlyAlpha += message[i]
cipherWord = ""
for i in range(len(onlyAlpha)):
  index_val = alphabet.index(onlyAlpha[i]) + int(key)
  cipherWord += alphabet[index_val]
print(cipherWord)
else:
  print("Usage: python caesar.py key")
