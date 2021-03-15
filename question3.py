test_data = open("log_data.txt", "r")
N = int(input())
m,t = map(int, input().split())

lost_ping = {}  #pingがタイムアウトしたサーバーのipとタイムアウトの回数
ip_day_dic = {} #pingがタイムアウトしたサーバーのipと最初にタイムアウトした日付
breakdown_ls = []   #故障と判断されたサーバーのip

load_dic = {}   #サーバーごとの負荷状態を管理するための辞書
overload_ls = []    #過負荷状態のサーバーのip

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
        if ip not in load_dic.keys():
            load_dic[ip] = [int(state)]
        else:
            load_dic[ip].append(int(state))
        
        # print(sum(load_dic[ip][:m])/m)
        if sum(load_dic[ip][:m])/m > t and ip not in overload_ls:
            print("Overload ip:" + ip ,end = " ")
            print_day(day)
            overload_ls.append(ip)
        elif sum(load_dic[ip][:m])/m < t and ip in overload_ls:
            print("Load Reduction ip" + ip , end = " ")
            print_day(day)
            overload_ls.remove(ip)
        if ip in breakdown_ls:
            print("Restoration ip:" + ip, end = " ")
            print_day(day)
            breakdown_ls.remove(ip)

# print(load_dic)

test_data.close()