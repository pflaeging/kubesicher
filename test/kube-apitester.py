#! /usr/bin/env python3
# Peter Pfläging <peter@pflaeging.net>

from kubernetes import client, config
from openshift.dynamic import DynamicClient

# disable SSL warnings
import urllib3
urllib3.disable_warnings()


k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)

v1_projects = dyn_client.resources.get(api_version='project.openshift.io/v1', kind='Project')

project_list = v1_projects.get()

for project in project_list.items:
    print(project.metadata.name)
