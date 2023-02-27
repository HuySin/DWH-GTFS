
def push(MODEL, index, msg_decode):
    flag = 0
    
    for i in range(len(MODEL)):
        if MODEL[i][index] == 0:
            MODEL[i][index] = msg_decode
            flag = 1
            break
    if flag == 0:
        MODEL.append([0, 0, 0, 0])
        MODEL[len(MODEL)-1][index] = msg_decode


def push_to_QUEUE(MODEL_1, MODEL_2, MODEL_3, MODEL_4, MODEL_5, msg_decode):
    if msg_decode['messageType'] == 'MET':
        index = 1
    elif msg_decode['messageType'] == 'SWR':
        index = 2
    elif msg_decode['messageType'] == 'LOG':
        index = 3
    else:
        index = 0

    if msg_decode['modelVersion'] == 1:
        push(MODEL_1, index, msg_decode)

    elif msg_decode['modelVersion'] == 2:
        push(MODEL_2, index, msg_decode)

    elif msg_decode['modelVersion'] == 3:
        push(MODEL_3, index, msg_decode)

    elif msg_decode['modelVersion'] == 4:
        push(MODEL_4, index, msg_decode)

    elif msg_decode['modelVersion'] == 5:
        push(MODEL_5, index, msg_decode)

