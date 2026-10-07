import subprocess

log_file = "unoq_logs.txt"

commands = [
    "dmesg | tail -50",
    "journalctl -n 50"
]

with open(log_file, "w") as file:

    for command in commands:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        file.write("===== " + command + " =====\n")
        file.write(result.stdout)
        file.write("\n\n")

print("Logs collected successfully")
print("Saved to:", log_file)
