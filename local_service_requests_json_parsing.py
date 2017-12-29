import json

with open('local_service_requests_new8.json', 'r+') as lsr:
    lsr_data = json.load(lsr)
    list_lsr_data = list(lsr_data)
for x in range (0, len(list_lsr_data)):
    second_value = (lsr_data[list_lsr_data[x]])
    #print(type(second_value))
    list_second_value = list(second_value)
    for z in range (0, len(list_second_value)):
        if list_second_value[z] == 'array':
            third_values = (second_value[list_second_value[z]])
            print(third_values[0])
