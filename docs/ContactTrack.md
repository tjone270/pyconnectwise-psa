# ContactTrack


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**action_remaining** | **int** |  | [optional] 
**action_taken** | **int** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**end_date** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**started_by** | **str** |  | [optional] 
**track_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.contact_track import ContactTrack

# TODO update the JSON string below
json = "{}"
# create an instance of ContactTrack from a JSON string
contact_track_instance = ContactTrack.from_json(json)
# print the JSON string representation of the object
print ContactTrack.to_json()

# convert the object into a dict
contact_track_dict = contact_track_instance.to_dict()
# create an instance of ContactTrack from a dict
contact_track_form_dict = contact_track.from_dict(contact_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


