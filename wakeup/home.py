from .config import config
from flask import Blueprint, render_template
from wakeonlan import send_magic_packet

bp = Blueprint('home', __name__)

@bp.route("/", methods=["GET"])
def home():
    return render_template(
        "home.html",
        servers=config['servers']
    )

@bp.route("/wake/<name>", methods=["POST"])
def wake(name):
    print(f"Broadcasting packet for {name}...")

    macs = [s for s in config['servers'] if s['name'] == name]
    if len(macs) == 0:
        return "ERROR", 500
    print(f"Using address: {macs[0]['mac']} via {config['broadcastAddr']}")

    send_magic_packet(
        macs[0]['mac'],
        ip_address=config['broadcastAddr'],
        port=config['port']
    )
    return "OK", 200