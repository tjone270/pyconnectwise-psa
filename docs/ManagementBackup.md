# ManagementBackup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**billing_level** | **str** |  | 
**id** | **int** |  | [optional] 
**item** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.management_backup import ManagementBackup

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementBackup from a JSON string
management_backup_instance = ManagementBackup.from_json(json)
# print the JSON string representation of the object
print ManagementBackup.to_json()

# convert the object into a dict
management_backup_dict = management_backup_instance.to_dict()
# create an instance of ManagementBackup from a dict
management_backup_form_dict = management_backup.from_dict(management_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


