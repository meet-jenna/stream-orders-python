# StreamDsp

## V1

Types:

```python
from jenna_stream_orders.types.stream_dsp import (
    Holiday,
    Image,
    Modifier,
    ModifierGroup,
    ModifierRulesV2,
    ObjectUpdate,
    Schedule,
    Tax,
    V1GetMenuFileURLResponse,
    V1RequestTokenResponse,
)
```

Methods:

- <code title="get /stream-dsp/v1/authorize">client.stream_dsp.v1.<a href="./src/jenna_stream_orders/resources/stream_dsp/v1/v1.py">authorize</a>(\*\*<a href="src/jenna_stream_orders/types/stream_dsp/v1_authorize_params.py">params</a>) -> None</code>
- <code title="get /stream-dsp/v1/menuFileS3Url">client.stream_dsp.v1.<a href="./src/jenna_stream_orders/resources/stream_dsp/v1/v1.py">get_menu_file_url</a>() -> <a href="./src/jenna_stream_orders/types/stream_dsp/v1_get_menu_file_url_response.py">V1GetMenuFileURLResponse</a></code>
- <code title="post /stream-dsp/v1/event">client.stream_dsp.v1.<a href="./src/jenna_stream_orders/resources/stream_dsp/v1/v1.py">new_event</a>(\*\*<a href="src/jenna_stream_orders/types/stream_dsp/v1_new_event_params.py">params</a>) -> object</code>
- <code title="post /stream-dsp/v1/token">client.stream_dsp.v1.<a href="./src/jenna_stream_orders/resources/stream_dsp/v1/v1.py">request_token</a>(\*\*<a href="src/jenna_stream_orders/types/stream_dsp/v1_request_token_params.py">params</a>) -> <a href="./src/jenna_stream_orders/types/stream_dsp/v1_request_token_response.py">V1RequestTokenResponse</a></code>

### Locations

Types:

```python
from jenna_stream_orders.types.stream_dsp.v1 import Address, LocationListResponse
```

Methods:

- <code title="get /stream-dsp/v1/locations">client.stream_dsp.v1.locations.<a href="./src/jenna_stream_orders/resources/stream_dsp/v1/locations/locations.py">list</a>() -> <a href="./src/jenna_stream_orders/types/stream_dsp/v1/location_list_response.py">LocationListResponse</a></code>

#### Connection

Types:

```python
from jenna_stream_orders.types.stream_dsp.v1.locations import (
    ConnectLocationDto,
    ConnectionRetrieveResponse,
)
```

Methods:

- <code title="post /stream-dsp/v1/locations/connection">client.stream_dsp.v1.locations.connection.<a href="./src/jenna_stream_orders/resources/stream_dsp/v1/locations/connection.py">create</a>(\*\*<a href="src/jenna_stream_orders/types/stream_dsp/v1/locations/connection_create_params.py">params</a>) -> None</code>
- <code title="get /stream-dsp/v1/locations/connection">client.stream_dsp.v1.locations.connection.<a href="./src/jenna_stream_orders/resources/stream_dsp/v1/locations/connection.py">retrieve</a>(\*\*<a href="src/jenna_stream_orders/types/stream_dsp/v1/locations/connection_retrieve_params.py">params</a>) -> <a href="./src/jenna_stream_orders/types/stream_dsp/v1/locations/connection_retrieve_response.py">ConnectionRetrieveResponse</a></code>
- <code title="delete /stream-dsp/v1/locations/connection">client.stream_dsp.v1.locations.connection.<a href="./src/jenna_stream_orders/resources/stream_dsp/v1/locations/connection.py">delete</a>(\*\*<a href="src/jenna_stream_orders/types/stream_dsp/v1/locations/connection_delete_params.py">params</a>) -> None</code>

# Order

Types:

```python
from jenna_stream_orders.types import Customer, OrderModifier
```
