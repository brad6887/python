arrive = input()
start = input()
arrive_list = arrive.split(':')
arrive_list = [int(item) for item in arrive_list]
start_list = start.split(':')
start_list = [int(item) for item in start_list]

asecs = (arrive_list[2]) + (arrive_list[1] * 60) + (arrive_list[0] * 3600)
ssecs = (start_list[2]) + (start_list[1] * 60) + (start_list[0] * 3600)
wait = ssecs - asecs
print(wait)
