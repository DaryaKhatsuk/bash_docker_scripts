#!/bin/bash

ALARM_API_URL="https://example.com/send_alarm"
MEMORY_THRESHOLD_PERCENT=90

send_alarm() {
    curl -X POST "$ALARM_API_URL" >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "Alarm sent successfully!"
    else
        echo "Failed to send alarm."
    fi
}

monitor_memory_usage() {
    while true; do
    	echo "Memory usage exceeded threshold..."
        memory_percent=$(df -kh . | tail -n1 | awk '{print $5}')
        echo "$memory_percent"

	percent="${memory_percent%\%}"

        if ((percent >= MEMORY_THRESHOLD_PERCENT)); then
            echo "Memory usage exceeded threshold ($percent%). Sending alarm..."
            send_alarm
        fi

        sleep 60
    done
}

monitor_memory_usage
