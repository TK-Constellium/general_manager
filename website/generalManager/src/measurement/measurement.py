# units.py
from __future__ import annotations
from typing import Any, Callable
import pint
from decimal import Decimal, getcontext, InvalidOperation
from operator import eq, ne, lt, le, gt, ge


# Set precision for Decimal
getcontext().prec = 28

# Create a new UnitRegistry
ureg = pint.UnitRegistry(auto_reduce_dimensions=True)

# Define currency units
currency_units = ["EUR", "USD", "GBP", "JPY", "CHF", "AUD", "CAD"]
for currency in currency_units:
    # Define each currency as its own dimension
    ureg.define(f"{currency} = [{currency}]")


class Measurement:
    def __init__(self, value: Decimal | float | int | str, unit: str):
        if not isinstance(value, (Decimal, float, int)):
            try:
                value = Decimal(str(value))
            except Exception:
                raise TypeError("Value must be a Decimal, float, int or compatible.")
        if not isinstance(value, Decimal):
            value = Decimal(str(value))
        self.__quantity = self.formatDecimal(value) * ureg.Quantity(1, unit)

    @property
    def quantity(self) -> pint.Quantity:
        return self.__quantity

    @classmethod
    def from_string(cls, value: str) -> Measurement:
        value, unit = value.split(" ")
        return cls(value, unit)

    @staticmethod
    def formatDecimal(value: Decimal) -> Decimal:
        value = value.normalize()
        if value == value.to_integral_value():
            try:
                return value.quantize(Decimal("1"))
            except InvalidOperation:
                return value
        else:
            return value

    def to(self, target_unit: str, exchange_rate: float | None = None):
        if self.is_currency():
            if self.quantity.units == ureg(target_unit):
                return self  # Same currency, no conversion needed
            elif exchange_rate is not None:
                # Convert using the provided exchange rate
                value = self.quantity.magnitude * Decimal(str(exchange_rate))
                return Measurement(value, target_unit)
            else:
                raise ValueError(
                    "Conversion between currencies requires an exchange rate."
                )
        else:
            # Standard conversion for physical units
            converted_quantity: pint.Quantity = self.quantity.to(target_unit)  # type: ignore
            value = Decimal(str(converted_quantity.magnitude))
            unit = str(converted_quantity.units)
            return Measurement(value, unit)

    def is_currency(self):
        # Check if the unit is a defined currency
        return str(self.quantity.units) in currency_units

    def __add__(self, other: Any) -> Measurement:
        if not isinstance(other, Measurement):
            raise TypeError("Addition is only allowed between Measurement instances.")
        if self.is_currency() and other.is_currency():
            # Both are currencies
            if self.quantity.units != other.quantity.units:
                raise ValueError(
                    "Addition between different currencies is not allowed."
                )
            result_quantity = self.quantity + other.quantity
            if not isinstance(result_quantity, pint.Quantity):
                raise ValueError("Units are not compatible for addition.")
            return Measurement(
                Decimal(str(result_quantity.magnitude)), str(result_quantity.units)
            )
        elif not self.is_currency() and not other.is_currency():
            # Both are physical units
            if self.quantity.dimensionality != other.quantity.dimensionality:
                raise ValueError("Units are not compatible for addition.")
            result_quantity = self.quantity + other.quantity
            if not isinstance(result_quantity, pint.Quantity):
                raise ValueError("Units are not compatible for addition.")
            return Measurement(
                Decimal(str(result_quantity.magnitude)), str(result_quantity.units)
            )
        else:
            raise TypeError(
                "Addition between currency and physical unit is not allowed."
            )

    def __sub__(self, other: Any) -> Measurement:
        if not isinstance(other, Measurement):
            raise TypeError(
                "Subtraction is only allowed between Measurement instances."
            )
        if self.is_currency() and other.is_currency():
            # Both are currencies
            if self.quantity.units != other.quantity.units:
                raise ValueError(
                    "Subtraction between different currencies is not allowed."
                )
            result_quantity = self.quantity - other.quantity
            return Measurement(
                Decimal(str(result_quantity.magnitude)), str(self.quantity.units)
            )
        elif not self.is_currency() and not other.is_currency():
            # Both are physical units
            if self.quantity.dimensionality != other.quantity.dimensionality:
                raise ValueError("Units are not compatible for subtraction.")
            result_quantity = self.quantity - other.quantity
            return Measurement(
                Decimal(str(result_quantity.magnitude)), str(self.quantity.units)
            )
        else:
            raise TypeError(
                "Subtraction between currency and physical unit is not allowed."
            )

    def __mul__(self, other: Any) -> Measurement:
        if isinstance(other, Measurement):
            if self.is_currency() or other.is_currency():
                raise TypeError(
                    "Multiplication between two currency amounts is not allowed."
                )
            result_quantity = self.quantity * other.quantity
            return Measurement(
                Decimal(str(result_quantity.magnitude)), str(result_quantity.units)
            )
        elif isinstance(other, (Decimal, float, int)):
            if not isinstance(other, Decimal):
                other = Decimal(str(other))
            result_quantity = self.quantity * other
            return Measurement(
                Decimal(str(result_quantity.magnitude)), str(self.quantity.units)
            )
        else:
            raise TypeError(
                "Multiplication is only allowed with Measurement or numeric values."
            )

    def __truediv__(self, other: Any) -> Measurement:
        if isinstance(other, Measurement):
            if self.is_currency() and other.is_currency():
                raise TypeError("Division between two currency amounts is not allowed.")
            result_quantity = self.quantity / other.quantity
            return Measurement(
                Decimal(str(result_quantity.magnitude)), str(result_quantity.units)
            )
        elif isinstance(other, (Decimal, float, int)):
            if not isinstance(other, Decimal):
                other = Decimal(str(other))
            result_quantity = self.quantity / other
            return Measurement(
                Decimal(str(result_quantity.magnitude)), str(self.quantity.units)
            )
        else:
            raise TypeError(
                "Division is only allowed with Measurement or numeric values."
            )

    def __str__(self):
        if not str(self.quantity.units) == "dimensionless":
            return f"{self.quantity.magnitude} {self.quantity.units}"
        return f"{self.quantity.magnitude}"

    def __repr__(self):
        return f"Measurement({self.quantity.magnitude}, '{self.quantity.units}')"

    def _compare(self, other: Any, operation: Callable[..., bool]) -> bool:
        if isinstance(other, str):
            other = Measurement.from_string(other)

        # Überprüfen, ob `other` ein Measurement-Objekt ist
        if not isinstance(other, Measurement):
            return NotImplemented
        try:
            # Convert `other` to the same units as `self`
            other_converted: pint.Quantity = other.quantity.to(self.quantity.units)  # type: ignore
            # Apply the comparison operation
            return operation(self.quantity.magnitude, other_converted.magnitude)
        except pint.DimensionalityError:
            raise ValueError("Cannot compare measurements with different dimensions.")

    # Comparison Operators
    def __eq__(self, other: Any) -> bool:
        return self._compare(other, eq)

    def __ne__(self, other: Any) -> bool:
        return self._compare(other, ne)

    def __lt__(self, other: Any) -> bool:
        return self._compare(other, lt)

    def __le__(self, other: Any) -> bool:
        return self._compare(other, le)

    def __gt__(self, other: Any) -> bool:
        return self._compare(other, gt)

    def __ge__(self, other: Any) -> bool:
        return self._compare(other, ge)
