test_data = open("log_data.txt", "r")
breakdown_ls = [] #故障と判断されたサーバーのip

def print_day(day): #日付を見やすく出力する関数
  print("{0}/{1}/{2} {3}:{4}:{5}".format(day[:4],day[4:6],day[6:8],day[8:10],day[10:12],day[12:14]))

for line in test_data:
  day,ip,state = map(str, line.split(","))
  # print(day,ip,state)
  if state == "-" or state == "-\n":  #pingのタイムアウトを確認
    if ip not in breakdown_ls:  #故障状態が続いているサーバーのIPを繰り返し出力しないための処理
      print("Breakdown ip:" + ip , end = " ")
      print_day(day)
      breakdown_ls.append(ip)
    else:
      continue
  else:
    if ip in breakdown_ls:
      print("Restoration ip:" + ip , end = " ")
      print_day(day)
      breakdown_ls.remove(ip)

test_data.close()