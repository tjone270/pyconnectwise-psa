# OnHandSerialNumberReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**serial_number** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.on_hand_serial_number_reference import OnHandSerialNumberReference

# TODO update the JSON string below
json = "{}"
# create an instance of OnHandSerialNumberReference from a JSON string
on_hand_serial_number_reference_instance = OnHandSerialNumberReference.from_json(json)
# print the JSON string representation of the object
print OnHandSerialNumberReference.to_json()

# convert the object into a dict
on_hand_serial_number_reference_dict = on_hand_serial_number_reference_instance.to_dict()
# create an instance of OnHandSerialNumberReference from a dict
on_hand_serial_number_reference_form_dict = on_hand_serial_number_reference.from_dict(on_hand_serial_number_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


