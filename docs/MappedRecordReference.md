# MappedRecordReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.mapped_record_reference import MappedRecordReference

# TODO update the JSON string below
json = "{}"
# create an instance of MappedRecordReference from a JSON string
mapped_record_reference_instance = MappedRecordReference.from_json(json)
# print the JSON string representation of the object
print MappedRecordReference.to_json()

# convert the object into a dict
mapped_record_reference_dict = mapped_record_reference_instance.to_dict()
# create an instance of MappedRecordReference from a dict
mapped_record_reference_form_dict = mapped_record_reference.from_dict(mapped_record_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


