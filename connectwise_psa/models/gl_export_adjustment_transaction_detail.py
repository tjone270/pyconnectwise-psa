# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.iv_item_reference import IvItemReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GLExportAdjustmentTransactionDetail(BaseModel):
    """
    GLExportAdjustmentTransactionDetail
    """ # noqa: E501
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    cost: Optional[Union[StrictFloat, StrictInt]] = None
    cost_account_number: Optional[StrictStr] = Field(default=None, alias="costAccountNumber")
    description: Optional[StrictStr] = None
    gl_class: Optional[StrictStr] = Field(default=None, alias="glClass")
    inventory_account_number: Optional[StrictStr] = Field(default=None, alias="inventoryAccountNumber")
    item: Optional[IvItemReference] = None
    memo: Optional[StrictStr] = None
    product_account_number: Optional[StrictStr] = Field(default=None, alias="productAccountNumber")
    quantity: Optional[StrictInt] = None
    total: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["accountNumber", "cost", "costAccountNumber", "description", "glClass", "inventoryAccountNumber", "item", "memo", "productAccountNumber", "quantity", "total"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GLExportAdjustmentTransactionDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict['cost'] = None

        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GLExportAdjustmentTransactionDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GLExportAdjustmentTransactionDetail) in the input: " + _key)

        _obj = cls.model_validate({
            "accountNumber": obj.get("accountNumber"),
            "cost": obj.get("cost"),
            "costAccountNumber": obj.get("costAccountNumber"),
            "description": obj.get("description"),
            "glClass": obj.get("glClass"),
            "inventoryAccountNumber": obj.get("inventoryAccountNumber"),
            "item": IvItemReference.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "memo": obj.get("memo"),
            "productAccountNumber": obj.get("productAccountNumber"),
            "quantity": obj.get("quantity"),
            "total": obj.get("total")
        })
        return _obj

