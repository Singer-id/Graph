from openie import StanfordOpenIE
import json

properties = {
    'openie.affinity_probability_cap': 2 / 3,
}

def read_data(path_name,save_path):
    data = []
    with open(path_name) as f:
        dials = json.load(f)
        for dial_dict in dials[0]:
            dialog_history = ""
            for ti, turn in enumerate(dial_dict["turns"]):
                dialog_history +=  (" System: " + turn["system"] + " User: " + turn["user"])
                data.append(dialog_history)

    with open(save_path, 'w') as f:
        f.write(data)

if __name__ == "__main__":
    path_train = 'data/train_dials.json'
    save_train = 'data/train_openIE.txt'

    read_data(path_train,)
    with StanfordOpenIE(properties=properties) as client:
       with open(save_path) as f:
           content = f.read()
           for line in content:
                print('Text: %s.' % line)
                #for triple in client.annotate(text):
                    #print('|-', triple)
                graph_image = 'graph.png'
                client.generate_graphviz_graph(line, graph_image)
                print('Graph generated: %s.' % graph_image)