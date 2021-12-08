import json, argparse
import networkx as nx

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interaction_network', required=True)
    parser.add_argument('-o', '--stats_json', required=True)
    args = parser.parse_args()

    data = {}
    G = nx.Graph()

    with open(args.interaction_network, 'r') as f:
        obj = json.load(f)
        for pony1 in obj:
            for pony2 in obj[pony1]:
                if not G.has_edge(pony1, pony2):
                    G.add_edge(pony1, pony2, weight=obj[pony1][pony2])

    data["most_connected_by_num"] = []
    by_degree = sorted(G.degree, key=lambda x: x[1], reverse=True)
    if len(by_degree) >= 3: by_degree = by_degree[:3]
    for node in by_degree:
        data["most_connected_by_num"].append(node[0])
    
    data["most_connected_by_weight"] = []
    by_weight = sorted(G.degree(weight='weight'), key=lambda x: x[1], reverse=True)
    if len(by_weight) >= 3: by_weight = by_weight[:3]
    for node in by_weight:
        data["most_connected_by_weight"].append(node[0])

    by_between = nx.betweenness_centrality(G, normalized=False)
    by_between = list(dict(sorted(by_between.items(), key=lambda item: item[1], reverse=True)))
    if len(by_between) >= 3: by_between = by_between[:3]
    data["most_central_by_betweenness"] = by_between

    with open(args.stats_json, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()