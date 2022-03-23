import re
import requests
import config
import uptime_data

slack_url = config.SLACK_INFO["url"]
slack_channel = config.SLACK_INFO["channel"]
slack_bot_name = config.SLACK_INFO["bot_name"]
slack_bot_emoji = config.SLACK_INFO["bot_emoji"]


def send_updated_uptimecheck_info(payload):
    response = requests.post(slack_url, json=payload)
    return response


def generate_slack_payload(text, attachments=None):
    payload = {
        "channel": slack_channel,
        "username": slack_bot_name,
        "icon_emoji": slack_bot_emoji,
        "text": text,
    }
    if attachments:
        payload["attachments"] = attachments
    return payload


def uptimecheck_incident_info(incident_id, incident_url, state, arrived_time):
    return f"<{incident_url}|{incident_id}> {state} at {arrived_time}"


def uptimecheck_info_to_attatchment(host, *incident_fields):
    if incident_fields[2] == "closed":
        return {
            "color": "#8EFE00",
            "title": "host: " + host,
            "text": "• *State*: Normal\n• *Incident*: "
            + uptimecheck_incident_info(*incident_fields),
        }
    else:
        return {
            "color": "#FF4C33",
            "title": "host: " + host,
            "text": "• *State*: Falling\n• *Incident*: "
            + uptimecheck_incident_info(*incident_fields),
        }


def uptimecheck_info_msg(text):
    uptimecheck_infos = uptime_data.get_uptimecheck_infos()
    uptimecheck_info_attatchment_list = list()

    for host, info in uptimecheck_infos.items():
        uptimecheck_info_attatchment = uptimecheck_info_to_attatchment(host, *info)
        uptimecheck_info_attatchment_list.append(uptimecheck_info_attatchment)

    if len(uptimecheck_info_attatchment_list) == 0:
        uptimecheck_info_attatchment_list.append(
            {
                "title": "Empty",
                "text": "Uptime check message not received yet from GCP Monitoring.",
            }
        )
    payload = generate_slack_payload(
        text, uptimecheck_info_attatchment_list
    )
    return payload


def uptimecheck_help_msg():
    return generate_slack_payload(
        "*uptime help*",
        [
            {
                "color": "#FEF600",
                "title": "command: uptime check",
                "text": "Receive uptime check monitoring list of the current status.",
            },
            {
                "color": "#FEF600",
                "title": "command: uptime remove {host}",
                "text": "Remove the host from the uptime check monitoring list. You'll be no longer received message that associated with you entered host.",
            },
            {
                "color": "#FEF600",
                "title": "command: uptime restore {host}",
                "text": "Restore the host from the uptime check monitoring list. You'll receive message that associated with you entered host.",
            },
            {
                "color": "#FEF600",
                "title": "command: uptime removed",
                "text": "Receive host list that you removed with 'uptime remove {host}' command.",
            },
        ],
    )


def uptimecheck_removed_hosts_msg():
    removed_host_list = uptime_data.get_removed_host_list()
    removed_host_list_text = "\n".join(removed_host_list)

    return generate_slack_payload(
        "*uptime removed*",
        [
            {
                "color": "#003AFE",
                "title": "removed host list",
                "text": removed_host_list_text,
            },
        ],
    )


def remove_uptimecheck_host(host):
    removed_host_list = uptime_data.get_removed_host_list()
    uptimecheck_infos = uptime_data.get_uptimecheck_infos()
    payload = ""
    host = extract_host(host)

    if host in uptimecheck_infos:
        uptime_data.delete_uptimecheck_info(host)
        uptime_data.add_removed_host(host)
        payload = uptimecheck_info_msg(f"*{host} remove success!*")

    elif host in removed_host_list:
        payload = generate_slack_payload(f"*{host} is already removed.*")

    else:
        payload = generate_slack_payload(
            f"*{host} is not exist in uptime check list.*"
        )
    return payload


def restore_uptimecheck_host(host):
    removed_host_list = uptime_data.get_removed_host_list()
    uptimecheck_infos = uptime_data.get_uptimecheck_infos()
    payload = ""
    host = extract_host(host)

    if host in uptimecheck_infos:
        payload = generate_slack_payload(
            f"*{host} is already exist in uptime check list.*"
        )
    elif host in removed_host_list:
        uptime_data.delete_removed_host(host)
        payload = generate_slack_payload(f"*{host} restore success!*")

    else:
        payload = generate_slack_payload(
            f"*{host} is not exist in removed list. Please check removed list with 'uptime removed' command.*"
        )
    return payload

def extract_host(host):
    host = re.sub("[<>*]", "", host)
    if "|" in host:
        host = host.split("|")[1]
    if "http" in host:
        host = host.split("//")[1]
    return host
