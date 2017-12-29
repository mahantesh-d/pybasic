import sys
f = open('app_config.txt', 'r', encoding='utf-8')
text = f.readlines()
f.close()
for z in text:
    x = ''.join(z)
    b = x.split("|")
    with open('app_config_insert.txt', 'a') as w:
        w.write("INSERT INTO all_trade.app_config (config_name_key0,"
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
        #print("'"+x+"',")
            with open('app_config_insert.txt', 'ab') as w:
                #vv = str(x).encode('utf-8')
                w.write(bytearray("'"+x+"',"), 'utf-8')
        w.write("CURRENT_TIMESTAMP;")
w.close()