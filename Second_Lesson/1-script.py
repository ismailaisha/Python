import subprocess

ip_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

with open("ping_results.txt", "w") as f:
    for ip in ip_list:
        result = subprocess.run(["ping", "-c", "2", ip])
        if result.returncode == 0:
            f.write(f"{ip} доступен\n")
        else:
            f.write(f"{ip} недоступен\n")