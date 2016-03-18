# Given a dictionary and a license plate. find a shortest word that contains 
# all the characters of the license.
# for instance, license st908i, the shortest word is "sit". 

def license_plate(words, plate):
  # get distinct character from the plate.
  # build the inverted index based on words.
  # a -> lenght=2 (posting list): word id, ...
  #      length=3 ..
  #      ...
  # For each letter, get the posting list, start from smallest length, return if any intersection.
