words = ["Hello", "World!", "I", "am", "a", "Pythonista!"]
print(*words, sep="\n")

with open("output.txt", "w") as output:
  print(*words, sep="\n", file=output)

cat output.txt
