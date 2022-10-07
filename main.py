def encode (message):
    encoded_message ="" \
    i = 0
    while (i <=len(message)-1):
        count = 1
        char = message [i]
    encoded_message = encoded_message+char+str(count)
    i = i+1 #i=+1
    return  encoded_message

encodeD_message = encode ("AAAAABBBBBB")
pri
