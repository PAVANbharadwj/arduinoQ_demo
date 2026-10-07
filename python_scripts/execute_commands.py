import subprocess

commands = [
    "uname -a",
    "free -h",
    "df -h",
    "ip addr"
]

for command in commands:
    print("\n---", command, "---")

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    print(result.stdout)
