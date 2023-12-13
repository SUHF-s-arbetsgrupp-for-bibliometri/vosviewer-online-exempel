import argparse
import json
import csv

"""

Kodfragment för att läsa in ett nätverk i JSON-format (exporterat från VOSViewer) med syfte att exemplifiera hur information kan adderas till såväl klusternivå som till enskilda noder.

Exemplet använder följande filer:

ExampleNetwork.json - 978 publikationer från Institutionen för datavetenskap vid UmU. Kluster skapade på basis av gemensamma referenser och termer från titel och abstract. Här en partitionering bestående av 16 kluster.

clusterInfo.txt - En beskrivning av varje kluster (här automatiskt extraherade)

itemInfo.txt - Information rörande varje enskild nod, här ScopusID och titel. ID används för att generera länkar in till Scopus.

Dokumentation av VOSViewers JSON-format: https://app.vosviewer.com/docs/file-types/json-file-type/


"""


def parse_args():
    parser = argparse.ArgumentParser(description='Add information to a VOSViewer file.')

    parser.add_argument('-i', '--inputNetwork', required=True, help='Input VOSViewer JSON network file')
    parser.add_argument('-o', '--outputNetwork', required=True, help='Output augmented VOSViewer JSON network file')
    parser.add_argument('-ci', '--clusterInfo', required=True, help='Tab-separated txt-file, cluster-level information')
    parser.add_argument('-ii', '--itemInfo', required=True, help='Tab-separated txt-file, item-level information')

    return parser.parse_args()

def main():
    args = parse_args()

    input_network = args.inputNetwork
    augmented_network = args.outputNetwork
    description_clusters = args.clusterInfo
    description_items = args.itemInfo

    # Läs in den nätverksfil till vilken vi ska addera information
    with open(input_network, 'r', encoding='utf-8-sig') as file:
        # Reading from json file
        json_network = json.load(file)

    # läs in en tabbseparerad fil, information om respektive kluster (t.ex. en beskrivning eller namn). Se clusterInfo.txt
    clusterNumberToAndClusterName = []
    with open(description_clusters, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')

        for row in reader:
            # Check if the row has at least two columns
            if len(row) >= 2:
                cluster_number = int(row[0])
                cluster_label = row[0] + ". " + row[1].strip()

                cluster_info = {"cluster": cluster_number, "label": cluster_label}
                clusterNumberToAndClusterName.append(cluster_info)

    #addera till nätverket
    json_network["network"]["clusters"] = clusterNumberToAndClusterName

    #läs in en tabbseparerad fil med två kolumner, information om respektive nod, (beroende på vad noderna är så kan detta vara titel, URL:er, personinformation, indikatorvärden etc). Se itemInfo.txt

    result_map = {}
    with open(description_items, 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.strip().split('\t')
            if (len(columns) == 2):
                key = columns[0]
                title = columns[1]

                value_object = {
                    "title": title,
                    "url": f"https://www.scopus.com/record/display.uri?origin=inward&eid={key}"
                    # skapar länkar till scopus
                }

                result_map[key] = value_object

    # addera till nätverket, här använder vi möjligheten att addera HTML-kod direkt

    for item in json_network["network"]["items"]:
        itemLabel = item.get("label")
        value_object = result_map.get(itemLabel)
        if (value_object != None):
            item["description"] = "<b>Title: " + value_object.get("title") + "\n" + "<a href=" + '"' + value_object.get(
                "url") + '"' + ">URL</a></b>"


    # spara till fil

    with open(augmented_network, 'w', encoding='utf-8') as updated_file:
        json.dump(json_network, updated_file, indent=2)


if __name__ == '__main__':
    main()
