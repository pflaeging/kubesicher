# Design and principal work structure for KubeSicher

KubeSicher should implement an easy method to backup the metadata of a kubernetes cluster in a git repo.

What are the components?

- a small python script, which is able to read a group of kubernetes objects and can serialize them as yaml for export -> get-k8sobjects.py
- an OCI container, which can execute the script, commits and pushes it in a git repo.
- a CronJob which executes the script
- a git repo ;-)
