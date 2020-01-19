# -*- coding: utf-8 -*-
"""Module provide functions for generate and encoded password."""

import secrets
import string
from base64 import b64encode
from hashlib import sha512
from os import urandom


def generate_salt(size: int = 16) -> str:
    """Generate random salt with specific size.

    :param size: size of salt (string length)
    :return: str -- salt
    """
    salt = b64encode(urandom(size)).decode('utf-8')
    if len(salt) > size:
        salt = salt[:size]
    return salt


def generate_password(size: int = 16, only_integers: bool = False) -> str:
    """Generate random password with specific size and kind of symbols.

    :param size: length of password
    :param only_integers: flag that indicates use only the digits for password
    :return: str -- password
    """
    alphabet = string.digits + ('' if only_integers else string.ascii_letters)
    password = ''.join(secrets.choice(alphabet) for _ in range(size))
    return password


def encrypt(value: str, salt: str) -> str:
    """Encrypt string value plus salt with sha512 encryption.

    :param value: string that need to encrypt
    :param salt: salt that add to end of value
    :return: str -- hexdigest string of encrypted value with salt
    """
    encoded = (value + salt).encode('utf-8')
    return sha512(encoded).hexdigest()


def create_signature(value: str, salt: str) -> str:
    """Create signature by value plus salt with sha1 hash.

    :param value: main part of signature
    :param salt: salt for signature
    :return: str -- hexdigest signature string
    """
    encoded = (value + salt).encode('utf-8')
    return sha512(encoded).hexdigest()
