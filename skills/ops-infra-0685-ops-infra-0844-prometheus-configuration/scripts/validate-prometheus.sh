#!/bin/bash
# Validate Prometheus configuration
promtool check config /etc/prometheus/prometheus.yml
promtool check rules /etc/prometheus/rules/*.yml
