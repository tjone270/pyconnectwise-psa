# PaymentType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**classification** | [**ClassificationReference**](ClassificationReference.md) |  | [optional] 
**company_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 30; | 

## Example

```python
from connectwise_psa.models.payment_type import PaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentType from a JSON string
payment_type_instance = PaymentType.from_json(json)
# print the JSON string representation of the object
print PaymentType.to_json()

# convert the object into a dict
payment_type_dict = payment_type_instance.to_dict()
# create an instance of PaymentType from a dict
payment_type_form_dict = payment_type.from_dict(payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


