# PaymentTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.payment_type_info import PaymentTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypeInfo from a JSON string
payment_type_info_instance = PaymentTypeInfo.from_json(json)
# print the JSON string representation of the object
print PaymentTypeInfo.to_json()

# convert the object into a dict
payment_type_info_dict = payment_type_info_instance.to_dict()
# create an instance of PaymentTypeInfo from a dict
payment_type_info_form_dict = payment_type_info.from_dict(payment_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


