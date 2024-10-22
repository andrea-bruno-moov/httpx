from .__version__ import __description__, __title__, __version__
from ._api import *
from ._auth import *
from ._client import *
from ._config import *
from ._content import *
from ._exceptions import *
from ._models import *
from ._status_codes import *
from ._transports import *
from ._types import *
from ._urls import *

try:
    from ._main import main
except ImportError:  # pragma: no cover

    def main() -> None:  # type: ignore
        import sys

        print(
            "The httpx command line client could not run because the required "
            "dependencies were not installed.\nMake sure you've installed "
            "everything with: pip install 'httpx[cli]'"
        )
        sys.exit(1)


# Note that we deliberately ensure all module names are private.
# The only public API is whatever we expose here.
#
# As a style guide we recommend always using a single top-level import.
# 
# ```
# import httpx
#
# client = httpx.Client()
# ```

__all__ = [
    # Implemented in `__version__.py`...
    "__description__",
    "__title__",
    "__version__",

    # Implemented in `_api.py`...
    "delete",
    "get",
    "head",
    "options",
    "patch",
    "post",
    "put",
    "request",
    "stream",

    # Implemented in `_auth.py`...
    "Auth",
    "BasicAuth",
    "DigestAuth",
    "NetRCAuth",

    # Implemented in `_client.py`...
    "USE_CLIENT_DEFAULT",
    "AsyncClient",
    "Client",

    # Implemented in `_config.py`...
    "Limits",
    "Proxy",
    "Timeout",
    "create_ssl_context",

    # Implemented in `_content.py`...
    "ByteStream",

    # Implemented in `_exceptions.py`...
    "CloseError",
    "ConnectError",
    "ConnectTimeout",
    "CookieConflict",
    "DecodingError",
    "HTTPError",
    "HTTPStatusError",
    "InvalidURL",
    "LocalProtocolError",
    "NetworkError",
    "PoolTimeout",
    "ProtocolError",
    "ProxyError",
    "ReadError",
    "ReadTimeout",
    "RemoteProtocolError",
    "RequestError",
    "RequestNotRead",
    "ResponseNotRead",
    "StreamClosed",
    "StreamConsumed",
    "StreamError",
    "TimeoutException",
    "TooManyRedirects",
    "TransportError",
    "UnsupportedProtocol",
    "WriteError",
    "WriteTimeout",

    # Implemented in `_main.py`...
    "main",

    # Implemented in `_models.py`...
    "Cookies",
    "Headers",
    "Request",
    "Response",

    # Implemented in `_status_codes.py`...
    "codes",

    # Implemented in `_transports/*.py`...
    "ASGITransport",
    "AsyncBaseTransport",
    "AsyncHTTPTransport",
    "BaseTransport",
    "HTTPTransport",
    "MockTransport",
    "WSGITransport",

    # Implemented in `_types.py`...
    "AsyncByteStream",
    "SyncByteStream",

    # Implemented in `_urls.py`...
    "QueryParams",
    "URL",
]


__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        setattr(__locals[__name], "__module__", "httpx")  # noqa
