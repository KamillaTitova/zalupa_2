import datetime as dt
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class TimestampMixin(object):
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
