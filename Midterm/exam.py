def probe_matching(s, p):
  match_locations = []
  for i in range(len(s)):
    if s.startswith(p, i):
      match_locations.append(i)
  return match_locations


print(probe_matching("ACTGGTTA", "CTG"))
print(probe_matching("CATGGACTGGA", "TGG"))
print(probe_matching("CATGGACG", "ATGA"))
print(probe_matching("", ""))
