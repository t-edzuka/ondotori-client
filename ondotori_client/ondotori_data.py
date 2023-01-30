from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, BaseSettings, Field

# おんどとり API アクセス例
#  https://ondotori.webstorage.jp/docs/api/reference/devices_device.html


ONDOTORI_ENDPOINT = "https://api.webstorage.jp/v1/devices/current"

ONDOTORI_HEADER = {"Content-Type": "application/json", "X-HTTP-Method-Override": "GET"}


class AccessInfo(BaseSettings):
    api_key: str
    login_id: str
    login_pass: str
    remote_serial: Optional[List[str]] = Field(defaylt=None)
    base_serial: Optional[List[str]] = Field(default=None)

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"

    def to_hyphen_dict(self) -> Dict[str, str]:
        return {key.replace("_", "-"): item for key, item in self.dict().items()}


class ChannelContent(BaseModel):
    num: int
    name: Optional[str]
    value: Union[float, str]
    unit: str


class BaseUnitContent(BaseModel):
    serial: str
    model: str
    name: Optional[str]


class GroupContent(BaseModel):
    num: int
    name: str


class DeviceContent(BaseModel):
    num: int
    serial: str
    model: str
    name: str
    battery: str
    rssi: Optional[str]
    time_diff: str
    std_bias: str
    dst_bias: str
    unixtime: datetime
    channel: List[ChannelContent]
    baseunit: BaseUnitContent


class OndotoriResponse(BaseModel):
    devices: List[DeviceContent]


class ResponseInterface(ABC):
    @property
    @abstractmethod
    def status_code(self) -> int:
        ...

    @property
    @abstractmethod
    def content(self) -> OndotoriResponse:
        ...

    @property
    @abstractmethod
    def headers(self) -> List[tuple[bytes, bytes]]:
        ...

    @property
    @abstractmethod
    def is_success(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_error(self) -> bool:
        ...
