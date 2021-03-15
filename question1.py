test_data = open("log_data.txt", "r")
breakdown_ls = [] #故障と判断されたサーバーのip

def print_day(day):
  print("{0}/{1}/{2} {3}:{4}:{5}".format(day[:4],day[4:6],day[6:8],day[8:10],day[10:12],day[12:14]))

for line in test_data:
  # print line
  day,ip,state = map(str, line.split(","))
  if state == "-" or state == "-\n":
    if ip not in breakdown_ls:
      print("ip:" + ip)
      print("breakdown:",end = "")
      print_day(day)
      breakdown_ls.append(ip)
    else:
      continue
  else:
    if ip in breakdown_ls:
      print("restoration:",end = "")
      print_day(day)
      breakdown_ls.remove(ip)

test_data.close()