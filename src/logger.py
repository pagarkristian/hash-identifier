import os
from datetime import datetime

def write_log(hash_value, hash_type):

        os.makedirs("logs", exist_ok=True)

        with open("logs/hash_identifier.log", "a") as log :

            timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

            log.write(
                f"[{timestamp}]"
                f"HASH={hash_value}"
                f"TYPE={hash_type}\n"

)
