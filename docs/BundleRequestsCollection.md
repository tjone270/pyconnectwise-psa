# BundleRequestsCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BundleRequest]**](BundleRequest.md) |  | 

## Example

```python
from connectwise_psa.models.bundle_requests_collection import BundleRequestsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of BundleRequestsCollection from a JSON string
bundle_requests_collection_instance = BundleRequestsCollection.from_json(json)
# print the JSON string representation of the object
print BundleRequestsCollection.to_json()

# convert the object into a dict
bundle_requests_collection_dict = bundle_requests_collection_instance.to_dict()
# create an instance of BundleRequestsCollection from a dict
bundle_requests_collection_form_dict = bundle_requests_collection.from_dict(bundle_requests_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


