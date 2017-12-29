import datetime, time, random, string, json

with open('app_config.json', 'r+') as app_config:
    load_app_config = json.load(app_config)
    list_app_config = list(load_app_config)

    for x in range(0,len(list_app_config)):
        second_field = load_app_config[list_app_config[x]]
        value = list(second_field)

        for z in range(0,len(value)):
            if value[z] == 'string':

                if "str" in str(list_app_config[x]):
                    second_field[value[z]] = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S+0700')
                else:
                    second_field[value[z]] = ''.join(random.choices(string.ascii_lowercase,  k=5))

            elif value[z] == 'long':
                second_field[value[z]] = int(time.time())

            else:
                second_field[value[z]] = 1

    app_config.seek(0)
    json.dump(load_app_config, app_config, indent=4)
    app_config.truncate()
    app_config.close()

