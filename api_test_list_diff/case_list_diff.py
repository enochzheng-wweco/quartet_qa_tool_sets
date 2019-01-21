"""
Enoch - Jan 2019

To find out what is already in api test list and what is newly added
Usage:
1.put the 3 files in a folder
2.change path on 2 .sh files.
3.run .py file
"""
import subprocess


def api_list():
    (status, output) = subprocess.getstatusoutput('./api_list.sh')
    blob_list = output.split("\n")
    name_list=[]

    for item in blob_list:
        name_start = item.find("test_")
        name_end = item.find(".py")
        if name_start and name_end:
            name = item[name_start:name_end].strip()

        class_start = item.find("class ")
        class_end = item.find("(")
        if class_start and class_end:
            class_name = item[class_start+5:class_end].strip()
        if name != None and class_name !=None:
            name_list.append(name + "." + class_name)

    return name_list

def org_api_list():
    (status, output) = subprocess.getstatusoutput('./org_api_list.sh')
    blob_list = output.split("\n")
    name_list=[]
    for item in blob_list:
        name_start = item.find('Case(')
        name_end = item.find(')')
        if name_start != None and name_end != None:
            name = item[name_start+5:name_end].strip()
        if name != None:
            name_list.append(name)

    return name_list

if __name__ == "__main__":
    new = api_list()
    print (new)
    org = org_api_list()
    print(org)
    for i in new:
        if i not in org:
            print (i)

