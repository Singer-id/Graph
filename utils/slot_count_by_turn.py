import json
from collections import OrderedDict
EXPERIMENT_DOMAINS = ["hotel", "train", "restaurant", "attraction", "taxi"]


def get_slot_information(ontology):
    ontology_domains = dict([(k, v) for k, v in ontology.items() if k.split("-")[0] in EXPERIMENT_DOMAINS])
    SLOTS = [k.replace(" ","").lower() if ("book" not in k) else k.lower() for k in ontology_domains.keys()]
    return SLOTS

def slot_count(load_path, SLOTS):
    slot_counter = {}
    with open(load_path) as f:
        dials = json.load(f)
        for dial_dict in dials:
            for ti, turn in enumerate(dial_dict["turns"]):
                slot_temp = SLOTS
                slot_values = turn["state"]["slot_values"]
                #print(slot_values)
                for slot in slot_temp:
                    if slot_values.get(slot):
                        if slot not in slot_counter.keys():
                            slot_counter[slot] = 0
                        slot_counter[slot] += 1
                        #print(str(slot)+"+1")
    return slot_counter

def domain_count(load_path):
    domain_counter = {}
    with open(load_path) as f:
        dials = json.load(f)
        for dial_dict in dials:
            for domain in dial_dict["domains"]:
                if domain not in EXPERIMENT_DOMAINS:
                    continue
                if domain not in domain_counter.keys():
                    domain_counter[domain] = 0
                domain_counter[domain] += 1
    return domain_counter

def save_count(slot_save_path, domain_save_path):
    with open(slot_save_path, 'w') as f:
        json.dump(slot_count(path_train, ALL_SLOTS), f, indent=4)
        json.dump(slot_count(path_dev, ALL_SLOTS), f, indent=4)
        json.dump(slot_count(path_test, ALL_SLOTS), f, indent=4)

    with open(domain_save_path, 'w') as f:
        json.dump(domain_count(path_train), f, indent=4)
        json.dump(domain_count(path_dev), f, indent=4)
        json.dump(domain_count(path_test), f, indent=4)

def data_renew(load_path, SLOTS): #将数据里加入槽值更新标签label2，存json。数据形式类似data_laoder读入的形式
    data = []
    with open(load_path) as f:
        dials = json.load(f)
        for dial_dict in dials:
            for ti, turn in enumerate(dial_dict["turns"]):
                turn_id = ti
                slot_temp = SLOTS
                slot_values = turn["state"]["slot_values"]

                for slot in slot_temp:
                    value_text = slot_values.get(slot, 'none').strip()
                    if turn_id == 0:
                        previous_value_text = 'none'
                    else:
                        previous_value_text = data[-1 * len(slot_temp)]["value_text"]

                    if previous_value_text == value_text:
                        output_text2 = "remain"
                    elif previous_value_text == 'none':
                        output_text2 = "generate"
                    elif value_text == 'none':
                        output_text2 = "delete"
                    else:
                        output_text2 = "replace"

                    data_detail = {
                        "ID": dial_dict["dial_id"],
                        "domains": dial_dict["domains"],
                        "turn_id": turn_id,
                        "system": turn["system"],
                        "user":turn["user"],
                        "slot_text": slot,
                        "value_text": value_text,
                        "operation_label":output_text2
                    }
                    data.append(data_detail)
    return data

if __name__ == "__main__":
    path_train = '../data/train_dials.json'
    path_dev = '../data/dev_dials.json'
    path_test = '../data/test_dials.json'

    #ontology = json.load(open("../data/multi-woz/MULTIWOZ2 2/ontology.json", 'r'))  # 2.0
    ontology = json.load(open("../data/mwz2.1/ontology.json", 'r'))  # 2.1
    ALL_SLOTS = get_slot_information(ontology)
    #slot_save_path = 'slot_count_2.0.json'
    #domain_save_path = 'domain_count_2.0.json'
    #save_count(slot_save_path, domain_save_path)

    data_save_path_train = '../data/renew/train_dials.json'
    data_save_path_dev = '../data/renew/dev_dials.json'
    data_save_path_test = '../data/renew/test_dials.json'

    with open(data_save_path_train, 'w') as f:
        json.dump(data_renew(path_train, ALL_SLOTS), f, indent=4)
    with open(data_save_path_dev, 'w') as f:
        json.dump(data_renew(path_dev, ALL_SLOTS), f, indent=4)
    with open(data_save_path_test, 'w') as f:
        json.dump(data_renew(path_test, ALL_SLOTS), f, indent=4)