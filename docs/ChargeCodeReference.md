# ChargeCodeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.charge_code_reference import ChargeCodeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ChargeCodeReference from a JSON string
charge_code_reference_instance = ChargeCodeReference.from_json(json)
# print the JSON string representation of the object
print ChargeCodeReference.to_json()

# convert the object into a dict
charge_code_reference_dict = charge_code_reference_instance.to_dict()
# create an instance of ChargeCodeReference from a dict
charge_code_reference_form_dict = charge_code_reference.from_dict(charge_code_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


