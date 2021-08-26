#!/bin/bash

SCRIPTSPATH=$(dirname ${BASH_SOURCE})
FILESPATH="${SCRIPTSPATH}/../files"

ssh-keygen -t rsa -b 4096 -f ${FILESPATH}/k8s_lab_rsa -q -N "" <<<y >/dev/null 2>&1