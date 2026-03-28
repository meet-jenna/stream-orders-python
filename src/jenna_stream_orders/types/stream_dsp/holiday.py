# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Holiday"]


class Holiday(BaseModel):
    date: str
    """Day of the year in format MM-DD. Example: 05-14"""

    recurring_yearly: bool
    """Flag that indicates if this holiday repeats every year"""

    hours: Optional[List[str]] = None
    """Timeslots that the restaurant is open for this holiday.

    If ommited, the location is closed for the entire day. Example: ['7:15-14:30',
    '15:30-22:00'], exact same format as `Schedule` entity times
    """

    name: Optional[str] = None
    """Name of this holiday. Optional"""

    specific_years: Optional[List[float]] = None
    """
    When `reccurring_yearly` is false, this array contains the specific years that
    the holiday occurs on. Example: [2024, 2025]
    """
