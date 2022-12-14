import hashlib
hash ="69d8c7575198a63bc8d97306e80c26e04015a9afdb92a699adaaac0b51570de7"
file = open("wordfile.txt","r")
for word in file : 
  word = word.strip('\n')
  dig = (hashlib.sha256(word.encode("ascii", "ignore")).hexdigest())

  if dig == hash:
    print ("meaningful English word is : ",word)
