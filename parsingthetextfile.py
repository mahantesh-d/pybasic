f = open('app_config.txt', 'r', encoding='utf-8')
text = f.readlines()
f.close()
for z in text:
    x = ''.join(z)
#    print(x)
    b = x.split("|")
#print(b)
    print("INSERT INTO all_trade.app_config (config_name_key0,"
    "config_val1_data,"
    "config_val2_data,"
    "config_val3_data,"
    "remark_data,"
    "create_by_data,"
    "create_datetime_data,"
    "update_by_data,"
    "update_datetime_key1,"
    "app_config_pk,"
    "int_created_date,"
    "int_updated_date,"
    "int_is_deleted,"
    "description_data,"
    "impala_created_date) SELECT")
    for x in b:
        print("'"+x+"',")
    print("CURRENT_TIMESTAMP;")
#print(b[0])
#print(x.split("|"))
#print(type(b))