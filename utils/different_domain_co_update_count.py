import json

def data_filter(load_path,save_path):
    data_prefilter = []
    with open(load_path) as f:
        dials = json.load(f)
        for dial_dict in dials:
            if len(dial_dict["domains"]) > 1 and dial_dict["operation_label"] != "remain":
                data_prefilter.append(dial_dict)
    with open(save_path, 'w') as f:
        json.dump(data_prefilter, f, indent=4)

    data = []
    diag_id_list = []
    turn_list = []
    head_pointer = 0
    tail_pointer = 0
    flag = 0
    with open(save_path) as f:
        dials = json.load(f)
        for i, dial_dict in enumerate(dials):
            turn_id = dial_dict["turn_id"]
            diag_id = dial_dict["ID"]

            if diag_id not in diag_id_list:
                diag_id_list.append(diag_id)
                turn_list = []

            if turn_id not in turn_list:
                turn_list.append(turn_id)

                if tail_pointer > head_pointer: #处理上一个turn的数据
                    for j in range(head_pointer + 1, tail_pointer + 1):
                        if dials[head_pointer]["slot_text"][0:1] != dials[j]["slot_text"][0:1]:
                            flag = 1
                            break
                    if flag == 1:
                        for j in range(head_pointer, tail_pointer + 1):
                            data.append(dials[j])
                        flag = 0

                head_pointer = i
            else:
                tail_pointer = i

    with open(save_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    path_train = '../data/renew/train_dials.json'
    path_dev = '../data/renew/dev_dials.json'
    path_test = '../data/renew/test_dials.json'

    data_save_path_train = '../data/renew/filter/train_dials.json'
    data_save_path_dev = '../data/renew/filter/dev_dials.json'
    data_save_path_test = '../data/renew/filter/test_dials.json'

    data_filter(path_train, data_save_path_train)
    data_filter(path_dev, data_save_path_dev)
    data_filter(path_test, data_save_path_test)
