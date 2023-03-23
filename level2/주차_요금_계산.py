import math


def solution(fees, records):
    answer = []
    dict_record = {}
    for record in records:
        temp = record.split(' ')
        if temp[1] not in dict_record:
            dict_record[temp[1]] = [temp[0]]
        else:
            dict_record[temp[1]].append(temp[0])
    sorted_car_num = sorted(dict_record.keys())
    for car_num in sorted_car_num:
        parked_times = dict_record[car_num]
        if len(parked_times) % 2 == 0:
            sum_times = 0
            fee = fees[1]
            for i in range(0,len(parked_times),2):
                hour_in,minute_in = parked_times[i].split(":")
                hour_out,minute_out = parked_times[i+1].split(":")
                sum_times +=  (int(hour_out)* 60 + int(minute_out)) - (int(hour_in) * 60 + int(minute_in))
            print(car_num,sum_times)
            sum_times = sum_times - fees[0]
            if sum_times > 0:
                fee += math.ceil(sum_times / fees[2]) * fees[3]
            answer.append(fee)
        else:
            last = parked_times.pop(-1)
            sum_times = 0
            fee = fees[1]
            for i in range(0,len(parked_times),2):
                hour_in,minute_in = parked_times[i].split(":")
                hour_out,minute_out = parked_times[i+1].split(":")
                sum_times += (( int(hour_out) * 60 + int(minute_out)) - (int(hour_in) * 60 + int(minute_in)))
            hour_last,minute_last = last.split(":")
            sum_times += (23 * 60 + 59) - (int(hour_last) * 60 + int(minute_last))
            print(car_num,sum_times)
            sum_times = sum_times - fees[0]
            if sum_times > 0:
                fee += math.ceil(sum_times / fees[2]) * fees[3]
            answer.append(fee)
    return answer

print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN",
                "06:00 0000 IN",
                "06:34 0000 OUT",
                "07:59 5961 OUT",
                "07:59 0148 IN",
                "18:59 0000 IN",
                "19:09 0148 OUT",
                "22:59 5961 IN",
                "23:00 5961 OUT"]))