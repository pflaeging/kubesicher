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

[Further documentation](doc/readme.md)

## Status

I'm just beginning, ...

---

Peter Pfläging <peter@pflaeging.net>
