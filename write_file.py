def WriteFile(file_name, content):
  f = open(file_name, "w", newline='')

  for tweet in content:
    line = ' '.join([str(elem) for elem in tweet])

    f.write(line)
  f.close()
