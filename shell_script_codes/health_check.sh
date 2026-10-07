#!/bin/bash

echo "=============================="
echo "     UNO Q HEALTH CHECK"
echo "=============================="

echo
echo "[1] BOOT / SYSTEM"
echo "------------------------------"
uptime
uname -a

echo
echo "[2] STORAGE"
echo "------------------------------"
df -h

echo
echo "[3] NETWORK INTERFACES"
echo "------------------------------"
ip addr

echo
echo "[4] SERVICES"
echo "------------------------------"
systemctl --failed

echo
echo "=============================="
echo "       CHECK COMPLETE"
echo "=============================="
