#!/usr/bin/env python3
#
# command from kubesicher (https://github.com/pflaeging/kubesicher)
#
# Usage:
# ./get-k8sobjects.py -h
# usage: get-k8sobjects.py [-h] [-v] [--oc] [-n NAMESPACE] [-d] [-b BASEDIR]
#                          [-t OBJECTTYPES] [-l LABEL]
#
# Get kubernetes objects as yaml
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -v, --verbose         verbose output
#   --oc                  use oc command instead of kubectl
#   -n NAMESPACE, --namespace NAMESPACE
#                         export named namespace instead of current
#   -d, --makedir         create directory with namespace / project name for the
#                         exported files
#   -b BASEDIR, --basedir BASEDIR
#                         export root directory. Default is current directory
#   -t OBJECTTYPES, --objecttypes OBJECTTYPES
#                         objecttypes to export. Use comma as separator and no
#                         spaces
#   -l LABEL, --label LABEL
#                         only export objects with this label
#
# Beta version: don't trust me ;-)
#
# 
# Peter Pfläging <peter@pflaeging.net>
# License: Apache 2.0
#
import os, sys, yaml, json, re, argparse, subprocess, pprint

# defaults
default_objecttypes = ["deployments", "services", "route", "pvc", "configmap", "secret"]
command = "/usr/local/bin/kubectl"
verbose = False
destination = ""
labeler = []

def v_out(string):
    if verbose: print(string)

def execute(line):
    return subprocess.run(
        line,
        capture_output=True
        ).stdout.decode("utf-8")

def exportable(object):
    jsonset = json.loads(object)
    # delete certain elements
    del jsonset["metadata"]["selfLink"]
    # Make filename
    filename = "%s%s_%s.yaml" % (destination, jsonset["kind"], jsonset["metadata"]["name"])
    exportfile = open(filename, 'w')
    # serialize to yaml
    yamlout = yaml.dump(jsonset)
    exportfile.writelines(yamlout)
    exportfile.close()

def makenamespacedir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        v_out("Namespace Directory %s created" % dirName)
    else:    
        v_out("Namespace Directory %s already exists" % dirName)    

def serialize_namespace(namespace, objecttypes):

    v_out("Namespace: %s" % namespace)
    for otype in objecttypes:
        v_out("\t Getting %s:" % otype)
        # secrets are not exportable!    
        deploymentobjects = execute([command, "get", otype, "-o", "name", "-n", namespace] + labeler).split("\n")
        for i in deploymentobjects:
            if not i: continue
            v_out("\t \t %s" % i)
            if otype != "secret":    
                getter = execute([command, "get", i, "-o", "json", "-n", namespace, "--export"])
            else:
                getter = execute([command, "get", i, "-o", "json", "-n", namespace])    
            exportable(getter)

def main():
    # setting global variables
    global default_objecttypes
    global command
    global verbose
    global destination
    global labeler

    # argument parsing
    parser = argparse.ArgumentParser( 
        description="Get kubernetes objects as yaml",
        epilog="Beta version: don't trust me ;-)"
        )
    parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
    parser.add_argument("--oc", help="use oc command instead of kubectl", action="store_true")
    parser.add_argument("-n", "--namespace", help="export named namespace instead of current", default="")
    parser.add_argument("-d", "--makedir", help="create directory with namespace / project name for the exported files", action="store_true")
    parser.add_argument("-b", "--basedir", help="export root directory. Default is current directory", default=".")
    parser.add_argument("-t", "--objecttypes", help="objecttypes to export. Use comma as separator and no spaces", default="")
    parser.add_argument("-l", "--label", help="only export objects with this label", default="")
    args = parser.parse_args()

    verbose = args.verbose
    if args.oc: command = "/usr/local/bin/oc" 
    destination = "%s/" % args.basedir 
    if args.namespace == "":
        namespace = execute([command, "config", "view", "--minify", "-o=jsonpath={..namespace}"])
    else:
        namespace = args.namespace  
    if args.makedir: 
        destination = "%s%s/" % (destination, namespace)
        makenamespacedir(destination)
    if args.objecttypes:
        objects = args.objecttypes.split(",")
    else:
        objects = default_objecttypes
    if args.label:
        labeler = ["-l", args.label]
    else:
        labeler = []

    serialize_namespace(namespace,objects)

if __name__ == '__main__':
    main()