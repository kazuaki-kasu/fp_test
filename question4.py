test_data = open("log_data.txt", "r")
N = int(input())
lost_ping = {}  #pingがタイムアウトしたサーバーのipとタイムアウトの回数
ip_day_dic = {} #pingがタイムアウトしたサーバーのipと最初にタイムアウトした日付
breakdown_ls = []   #故障と判断されたサーバーのip

subnet_dic = {}
network_ls = []

def print_day(day):
    print("{0}/{1}/{2} {3}:{4}:{5}".format(day[:4],day[4:6],day[6:8],day[8:10],day[10:12],day[12:14]))

for line in test_data:
    # print line
    day,ip,state = map(str, line.split(","))

    nw,pre = ip.split("/")
    nw = nw.split(".")
    sub_mask = (32-int(pre))/8
    for i in range(int(sub_mask)):
        nw[-i-1] = "0"
    nw = ".".join(nw)
    # print(nw, "," , pre)
    if nw in subnet_dic.keys():
        subnet_dic[nw].append(state)
    else:
        subnet_dic[nw] = [state]
        # if subnet_dic[nw]

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