import json

STDFILE="data/students.json"
def read_json():
    f=open(STDFILE)
    data=json.load(f)
    f.close()
    return data

def write_json(data):
    f=open(STDFILE,"w")
    json.dump(data,f,indent=3)
    f.close()