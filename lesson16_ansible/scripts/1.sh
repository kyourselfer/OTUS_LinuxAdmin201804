#!/bin/bash
ansible all -i hosts -m command -a 'uptime'
