# BundleResultsCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**results** | [**List[BundleResult]**](BundleResult.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.bundle_results_collection import BundleResultsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of BundleResultsCollection from a JSON string
bundle_results_collection_instance = BundleResultsCollection.from_json(json)
# print the JSON string representation of the object
print BundleResultsCollection.to_json()

# convert the object into a dict
bundle_results_collection_dict = bundle_results_collection_instance.to_dict()
# create an instance of BundleResultsCollection from a dict
bundle_results_collection_form_dict = bundle_results_collection.from_dict(bundle_results_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


