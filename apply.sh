#!/bin/bash

oc delete -f pipeline.yaml --ignore-not-found=true
oc apply -f pipeline.yaml

oc delete -f pipeline_run.yaml --ignore-not-found=true
oc apply -f pipeline_run.yaml