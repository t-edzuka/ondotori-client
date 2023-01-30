from rich import print

from ondotori_client.ondotori_data import AccessInfo, ONDOTORI_ENDPOINT, ONDOTORI_HEADER, OndotoriResponse
from ondotori_client.usecase.current_device_data import fetch_current_sensor_data


def main() -> None:
    access_info = AccessInfo()

    response = fetch_current_sensor_data(access_info,
                                         url=ONDOTORI_ENDPOINT,
                                         headers=ONDOTORI_HEADER)
    try:
        ondotori_content: "OndotoriResponse" = response.content
    except ValueError:
        raise
    print(ondotori_content)


if __name__ == '__main__':
    main()
