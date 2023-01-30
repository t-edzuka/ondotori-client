from typing import List, Mapping, Union

import httpx
from httpx import Response

from ondotori_client.ondotori_data import (
    ONDOTORI_ENDPOINT,
    ONDOTORI_HEADER,
    AccessInfo,
    OndotoriResponse,
    ResponseInterface,
)


class ResponseImpl(ResponseInterface):
    def __init__(self, response: Response):
        self.response = response

    @property
    def status_code(self) -> int:
        return self.response.status_code

    @property
    def content(self) -> OndotoriResponse:
        response_content = self.response.content
        if self.is_success:
            return OndotoriResponse.parse_raw(response_content)
        elif self.is_error and self.status_code == 400:
            raise ValueError(f"""Ondotori access failed. status code:{self.status_code}\n
                             content: {self.response.json()}""")
        else:
            raise ValueError(f"Failed: status code {self.status_code}, content: {response_content}")

    @property
    def headers(self) -> List[tuple[bytes, bytes]]:
        return self.response.headers.raw

    @property
    def is_success(self) -> bool:
        return self.response.is_success

    @property
    def is_error(self) -> bool:
        return self.response.is_error


def fetch_current_sensor_data(
        access_info: AccessInfo,
        url: str = ONDOTORI_ENDPOINT,
        headers: Union[Mapping[str, str], None] = None,
        timeout_sec: float = 2.0,
) -> ResponseInterface:
    if headers is None:
        headers = ONDOTORI_HEADER
    response = httpx.post(
        url=url, json=access_info.to_hyphen_dict(), headers=headers, timeout=timeout_sec
    )
    return ResponseImpl(response)
