#!/usr/bin/env python3

import os, sys, yaml, json, re, pprint

default_objecttypes = ["deployments",  "services", "route", "pvc", "configmap", "secret"]

def exportable(object):
    jsonset = json.load(object)
    # delete certain elements
    del jsonset["metadata"]["selfLink"]
    # Make filename
    # pprint.pprint(jsonset)
    filename = "%s:%s.yaml" % (jsonset["kind"], jsonset["metadata"]["name"])
    exportfile = open(filename, 'w')
    # serialize to yaml
    yamlout = yaml.dump(jsonset)
    exportfile.writelines(yamlout)
    exportfile.close()

def serialize_namespace(namespace, objecttypes=default_objecttypes):

    print("Namespace: %s" % namespace)
    for otype in objecttypes:
        print("\t Getting %s:" % otype)
        deploymentobjects = os.popen("oc get %s -o name -n %s" %
            (otype, namespace))
    
        for i in deploymentobjects:
            i = i.rstrip("\n")
            print("\t \t %s" % i)
            getter = os.popen("oc get %s -o json --export -n %s" % 
                (i, namespace))
            exportable(getter)

def main():
    namespace = "alfrescodevelop"

    serialize_namespace(namespace)

if __name__ == '__main__':
    main()