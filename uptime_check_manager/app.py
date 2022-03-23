import time
import config
import slack_util
import uptime_data

from flask import Flask, request
from flask_apscheduler import APScheduler
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

app = Flask(__name__)

auth = HTTPBasicAuth()
users = config.HTTPBASICAUTH_USERS


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route("/fromGCPMonitoring", methods=["POST"])
@auth.login_required
def fromGCPMonitoring():
    params = request.get_json()
    host = params["incident"]["resource"]["labels"]["host"]
    incident_url = params["incident"]["url"]
    incident_id = params["incident"]["incident_id"]
    state = params["incident"]["state"]
    arrived_time = time.localtime()
    arrived_time = "%04d/%02d/%02d %02d:%02d:%02d" % (
        arrived_time.tm_year,
        arrived_time.tm_mon,
        arrived_time.tm_mday,
        arrived_time.tm_hour,
        arrived_time.tm_min,
        arrived_time.tm_sec,
    )

    uptime_data.add_uptimecheck_info(
        host, incident_id, incident_url, state, arrived_time
    )
    print(params)
    return "ok", 200


@app.route("/fromSlack", methods=["GET", "POST"])
def fromSlack():
    if request.form["user_id"] != "USLACKBOT":
        payload = ""
        text_splited = request.form["text"].split(" ")

        if request.form["text"] == "uptime check":
            payload = slack_util.uptimecheck_info_msg("uptime check")
        elif request.form["text"] == "uptime help":
            payload = slack_util.uptimecheck_help_msg()
        elif request.form["text"] == "uptime removed":
            payload = slack_util.uptimecheck_removed_hosts_msg()
        elif (
            len(text_splited) == 3
            and text_splited[0] == "uptime"
            and text_splited[1] == "remove"
        ):
            payload = slack_util.remove_uptimecheck_host(text_splited[2])
        elif (
            len(text_splited) == 3
            and text_splited[0] == "uptime"
            and text_splited[1] == "restore"
        ):
            payload = slack_util.restore_uptimecheck_host(text_splited[2])
        if payload != "":
            slack_util.send_updated_uptimecheck_info(payload)
        return "ok", 200
    else:
        return "ok", 200


@app.route("/")
def index():
    return "uptime check manager", 200


if __name__ == "__main__":

    def send_periodic_uptimechck_msg():
        payload = slack_util.uptimecheck_info_msg("uptime check")
        return slack_util.send_updated_uptimecheck_info(payload)

    class Config(object):
        JOBS = [
            {
                "id": "send_periodic_uptimechck_msg",
                "func": "__main__:send_periodic_uptimechck_msg",
                "trigger": "interval",
                "seconds": config.SEND_MESSAGE_INTERVAL,
            }
        ]

    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(port=5000, host="0.0.0.0")
