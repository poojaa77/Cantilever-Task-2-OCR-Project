import os
import socket
from application import app

if __name__ == "__main__":
    host = "0.0.0.0"  # Bind to all interfaces so LAN devices can access if needed
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "true").lower() == "true"

    # Print only localhost by default
    print(f" * Running on http://127.0.0.1:{port}")

    # Optional: print LAN IP for network access
    try:
        lan_ip = socket.gethostbyname(socket.gethostname())
        print(f" * LAN access (optional): http://{lan_ip}:{port}")
    except Exception:
        pass  # silently ignore if LAN IP cannot be determined

    # Start Flask
    app.run(host=host, port=port, debug=debug)


# Works on Windows
# Shows only one URL
# Supports LAN access if needed