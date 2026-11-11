"""Send a Jenkins build result to a Webex space."""

import json
import os
import sys
from urllib import error, request


def required_environment_variable(name):
    value = os.environ.get(name)

    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")

    return value


def main():
    status = os.environ.get("WEBEX_BUILD_STATUS", "UNKNOWN")
    icon = "✅" if status == "SUCCESS" else "❌"
    commit = os.environ.get("GIT_COMMIT", "unknown")[:7]
    job_name = os.environ.get("JOB_NAME", "unknown")
    build_number = os.environ.get("BUILD_NUMBER", "unknown")
    build_url = os.environ.get("BUILD_URL", "Unavailable")

    message = (
        f"{icon} **Jenkins build {status}**\n"
        f"- Job: {job_name} #{build_number}\n"
        f"- Commit: `{commit}`\n"
        f"- Details: {build_url}"
    )

    payload = json.dumps(
        {
            "roomId": required_environment_variable("WEBEX_ROOM_ID"),
            "markdown": message,
        }
    ).encode("utf-8")

    webex_request = request.Request(
        "https://webexapis.com/v1/messages",
        data=payload,
        headers={
            "Authorization": (
                f"Bearer {required_environment_variable('WEBEX_BOT_TOKEN')}"
            ),
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with request.urlopen(webex_request, timeout=30) as response:
            print(f"Webex notification HTTP {response.status}")
    except error.HTTPError as exception:
        print(
            f"Webex notification failed: HTTP {exception.code}",
            file=sys.stderr,
        )
        raise


if __name__ == "__main__":
    main()