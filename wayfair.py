def slotWheels(history):
    # Write your code here
    result=0
    while len(history[0]) > 0:
        max_stop = -1
        for i in range(len(history)):

            sorted_val = sorted(list(map(int,history[i])))
            max_stop = max(sorted_val[-1], max_stop)
            history[i] = sorted_val[:-1]

        result+=max_stop
    return result
