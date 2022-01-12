def problem3_1(txtfilename):
  infile = open(txtfilename)
  for line in infile:
    print(line, end="")
  print("\n")
  print("There are", len(txtfilename) ,"letters in the file.")
  infile.close