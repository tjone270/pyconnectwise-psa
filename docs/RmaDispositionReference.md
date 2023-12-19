# RmaDispositionReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_disposition_reference import RmaDispositionReference

# TODO update the JSON string below
json = "{}"
# create an instance of RmaDispositionReference from a JSON string
rma_disposition_reference_instance = RmaDispositionReference.from_json(json)
# print the JSON string representation of the object
print RmaDispositionReference.to_json()

# convert the object into a dict
rma_disposition_reference_dict = rma_disposition_reference_instance.to_dict()
# create an instance of RmaDispositionReference from a dict
rma_disposition_reference_form_dict = rma_disposition_reference.from_dict(rma_disposition_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


