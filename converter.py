import json
import sys

KEYS = {
    "predicate":"predicates",
    "id":"ids",
    "category":"categories",
    "type":"attribute_type_id",
    "url":"value_url",
    "name":"original_attribute_name",
    "source":"attribute_source"
}
PLURALIZE=["predicate","id","category"]



def main():
    file = sys.argv[1]
    try:
        with open(file) as f:
            data = json.load(f)
            try:
                converted=parse(data)
            except Exception as ex:
                print("Something went wrong in the parsing of the input file.  Sorry about that")
                print(ex)
    except Exception as ex:
        print("Something went wrong with the opening of thDe 1.0 file.  Sorry about that")
        print(ex)
        exit(1)

    fileSplit = file.split('.',1)
    fileBase=fileSplit[0]
    fileExtenstion=fileSplit[1]
    try:
        with open(fileBase+"-1.1."+fileExtenstion, 'w') as outfile:
             json.dump(converted, outfile)
    except Exception as ex:
        print("Something went wrong with the writing of the converted file.  Sorry about that")
        print(ex)
        exit(1)

def parse(json):
    keylist = list(json.keys())
    for key in keylist:
        if key in KEYS:
            if(key in PLURALIZE):
                json[key]=[json[key]]
            json[KEYS.get(key)]=json.pop(key)
            if (isinstance(json[KEYS.get(key)],dict)):
                parse(json[key])
        elif (isinstance(json[key],dict)):
            parse(json[key])
    return json


if __name__ == "__main__":
    main()