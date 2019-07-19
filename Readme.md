# kubesicher

## About

kubesicher is an effort to make backups of k8s cluster in a structured way without dumping binary data.

The idea is really simple:

- watch for object changes in a k8s cluster
- serialize these changes as portable YAML definitions
- put the objects in a git repo
- finish

## Structure

1. Implement the commands in python using "kubectl" or "oc" (for OpenShift or OKD)
1. Make an OCI container which can run in every k8s type cluster
1. Schedule with k8s cronjobs
1. Save in a defined git repo

## get-k8sobjects.py

is a tool to export a group of kubernetes objects.

Usage:
```
./get-k8sobjects.py -h
usage: get-k8sobjects.py [-h] [-v] [--oc] [-n NAMESPACE] [-d] [-b BASEDIR]
                         [-t OBJECTTYPES] [-l LABEL]

Get kubernetes objects as yaml

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbose output
  --oc                  use oc command instead of kubectl
  -n NAMESPACE, --namespace NAMESPACE
                        export named namespace instead of current
  -d, --makedir         create directory with namespace / project name for the
                        exported files
  -b BASEDIR, --basedir BASEDIR
                        export root directory. Default is current directory
  -t OBJECTTYPES, --objecttypes OBJECTTYPES
                        objecttypes to export. Use comma as separator and no
                        spaces
  -l LABEL, --label LABEL
                        only export objects with this label

Beta version: don't trust me ;-)
```

## Future

- Automatic restore from git repo
- Customization GUI
- ...

## Status

I'm just beginning

---
Peter Pfläging <peter@pflaeging.net>
