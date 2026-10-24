import docker
from docker.errors import DockerException

client = docker.from_env()
container = None

try:
    print("Starting container with AppArmor profile...")

    container = client.containers.run(
        "flask-apparmor",
        name="flask-apparmor-restriction-test",
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print(f"Container started: {container.short_id}")

    exit_code, output = container.exec_run(
        ["cat", "/etc/passwd"]
    )
    print(
        f"Attempt to read /etc/passwd: "
        f"Exit Code {exit_code}, Output: {output.decode(errors='replace')}"
    )

    exit_code, output = container.exec_run(
        ["/bin/bash", "-c", "echo bash-executed"]
    )
    print(
        f"Attempt to execute /bin/bash: "
        f"Exit Code {exit_code}, Output: {output.decode(errors='replace')}"
    )

except DockerException as error:
    print(f"Docker operation failed: {error}")

finally:
    if container is not None:
        try:
            container.remove(force=True)
            print("Test container removed.")
        except DockerException as error:
            print(f"Container cleanup failed: {error}")

    client.close()
