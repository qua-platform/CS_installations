import ssl
from typing import Optional
from dataclasses import field, dataclass

from qm.type_hinting.general import PathLike


@dataclass(frozen=True)
class CredentialOverrides:
    certificate_path: PathLike = field(default="")
    verify_mode: ssl.VerifyMode = field(default=ssl.CERT_REQUIRED)
    check_hostname: bool = field(default=True)


def create_credentials(credentials_override: Optional[CredentialOverrides] = None) -> ssl.SSLContext:
    import certifi

    context = ssl.create_default_context(
        purpose=ssl.Purpose.SERVER_AUTH,
        cafile=certifi.where(),
    )
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.set_ciphers("ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20")
    context.set_alpn_protocols(["h2"])
    if ssl.HAS_NPN:
        context.set_npn_protocols(["h2"])

    if credentials_override:
        if credentials_override.certificate_path:
            context.load_verify_locations(credentials_override.certificate_path)
        context.verify_mode = credentials_override.verify_mode
        context.check_hostname = credentials_override.check_hostname

    return context


__all__ = ["create_credentials", "CredentialOverrides"]
