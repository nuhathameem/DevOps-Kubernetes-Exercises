import docker
from docker.errors import DockerException

client = docker.from_env()

try:
    print("Building image from Dockerfile...")
    client.images.build(path=".", tag="flask-apparmor")
    print("Image built successfully.")

    print("Running container with AppArmor profile...")

    container = client.containers.run(
        "flask-apparmor",
        name="flask-apparmor-sdk-test",
        ports={"5000/tcp": 5002},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print(f"Container started: {container.short_id}")

    info = client.api.inspect_container(container.id)
    security_options = info["HostConfig"]["SecurityOpt"]
    print(f"Security options configured: {security_options}")

    container.stop()
    container.remove()
    print("Test container stopped and removed.")

except DockerException as error:
    print(f"Docker operation failed: {error}")

finally:
    client.close()