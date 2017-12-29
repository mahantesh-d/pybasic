f = open("app_config", 'r+')
data = f.readlines()
f.close()
hql = []
for x in range(0,len(data)):
    print(data[x])
    if 'time' in data[x]:
        time_to_replace = str(data[x])
        time_field = time_to_replace.replace("timestamp with time zone", '').replace("DEFAULT now()",'').replace(',','').replace('\n','')
        time_field_time = time_to_replace.replace("time with time zone", '').replace("DEFAULT now()",'').replace(',','').replace('\n','')
        hql.append(time_field.replace(' ','')+' bigint,\n')
        hql.append(time_field.replace(' ','')+'_str'+' string,\n')
    elif 'text' in data[x]:
        str_to_replace = str(data[x])
        text_field = str_to_replace.replace('text','').replace('NOT NULL','').replace(',','').replace('\n','')
        hql.append(text_field.replace(' ','')+' string,\n')
    elif 'bigint' in data[x]:
        pk_to_replace = str(data[x])
        pk_field = pk_to_replace.replace('bigint', '').replace('NOT NULL', '').replace(',', '').replace('\n', '')
        hql.append(pk_field.replace(' ', '') + ' int,\n')
    elif 'REPLICATION' in data[x]:
        rep_to_replace = str(data[x])
        rep_line = rep_to_replace.replace('DISTRIBUTE BY REPLICATION;','STORED AS AVRO;')
        hql.append(rep_line)
    else:
        hql.append(data[x])
new_hql = open('app_config_hql', 'w')
for fields in hql:
    new_hql.write(fields)
new_hql.close()