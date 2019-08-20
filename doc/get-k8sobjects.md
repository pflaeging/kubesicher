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
```
