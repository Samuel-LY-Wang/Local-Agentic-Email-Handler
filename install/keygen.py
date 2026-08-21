from cryptography.hazmat.primitives.asymmetric import rsa
import requests
import uuid
from config.defaults import SERVER_ENDPOINT

def gen_keys() -> dict[str, int]:
    """
    Generates a new RSA key pair and returns them as a dictionary. Please note that the standard e=65537 is enforced (and is thus not returned).
    Returns:
        dict: A dictionary containing the modulus 'n' and private exponent 'd' of the RSA key pair.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    numbers = private_key.private_numbers()
    pub_numbers = numbers.public_numbers

    return {
        "n": pub_numbers.n,
        "d": numbers.d
    } # e=65537 is standard and will be enforced

def save_keys(uid: str, n: int, d: int):
    """
    Saves the UUID and RSA modulus to both config/uuid.txt and the server endpoint. Also saves the private exponent to config/uuid.txt for decryption purposes.
    """
    with open("config/uuid.txt", "w") as f:
        f.write(f"{uid}\n{n}\n{d}")
    requests.post(SERVER_ENDPOINT + "/register", params={"uid": uid, "n": n})

if __name__ == "__main__":
    keys = gen_keys()
    save_keys(str(uuid.uuid4()), keys["n"], keys["d"])