import re
import os
import itertools


def logs():

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'data/logdata.txt')

    with open(filename, "r") as file:
        logdata = file.read()

    # find host
    pattern_ip = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    ips = re.findall(rf"{pattern_ip}",logdata)
    # for ip in ips : print(ip)

    # find user_name
    pattern_username = "\s[-]\s(\w*\d|[-])"
    usernames = re.findall(rf"{pattern_username}",logdata)
    # for user in usernames : print(user)

    pattern_time = "\[([^]]+)\]"
    times = re.findall(rf"{pattern_time}",logdata)
    # for time in times : print(time)

    pattern_request = '["]([^]]+)["]'
    requests = re.findall(rf"{pattern_request}",logdata)
    # for request in requests : print(request)

    dict_values = []

    for i in range(0,len(ips)):

        my_dict = dict(host=ips[i],user_name=usernames[i],time=times[i],request=requests[i])
        dict_values.append(my_dict)

    for _ in dict_values: print(_)

    return dict_values
logs()
