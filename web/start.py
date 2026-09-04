#!/usr/bin/env python3
"""Start the Second Brain AI server."""
import subprocess
import sys
import time
import urllib.request
import json

PORT = 5000

def is_running():
    try:
        urllib.request.urlopen(f'http://localhost:{PORT}/api/stats', timeout=2)
        return True
    except:
        return False

def start_server():
    cmd = [sys.executable, "E:\\obsidian\\second brain\\web\\app.py", "--port", str(PORT)]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for server to start
    for i in range(20):
        time.sleep(1)
        if is_running():
            print(f"Server running at http://localhost:{PORT}")
            print(f"Network access: http://192.168.10.73:{PORT}")
            return process
    
    print("Server failed to start")
    process.kill()
    return None

if __name__ == "__main__":
    if is_running():
        print(f"Server already running at http://localhost:{PORT}")
    else:
        start_server()
