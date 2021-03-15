test_data = open("log_data.txt", "r")
N = int(input())
lost_ping = {}  #pingがタイムアウトしたサーバーのipとタイムアウトの回数
ip_day_dic = {} #pingがタイムアウトしたサーバーのipと最初にタイムアウトした日付
breakdown_ls = []   #故障と判断されたサーバーのip

def print_day(day):
    print("{0}/{1}/{2} {3}:{4}:{5}".format(day[:4],day[4:6],day[6:8],day[8:10],day[10:12],day[12:14]))

for line in test_data:
    # print line
    day,ip,state = map(str, line.split(","))
    if state == "-" or state == "-\n":
        if ip not in lost_ping.keys():
            lost_ping[ip] = 1
            ip_day_dic[ip] = day
        else:
            lost_ping[ip] += 1
            if lost_ping[ip] == N:
                print("Breakdown ip:" + ip, end = " ")
                print_day(ip_day_dic[ip])
                breakdown_ls.append(ip)
    else:
        if ip in breakdown_ls:
            print("Restoration ip:" + ip, end = " ")
            print_day(day)
            breakdown_ls.remove(ip)

# print(lost_ping)

test_data.close()