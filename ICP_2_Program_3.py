def inches_to_centimeters():
    cents_list = [150, 155, 145, 148]
    inches_list = []
    for i in cents_list:
        inches_list.append(float(i * 2.54))
    print(inches_list)

    
inches_to_centimeters()
