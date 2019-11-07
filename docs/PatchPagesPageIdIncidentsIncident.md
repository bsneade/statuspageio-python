# PatchPagesPageIdIncidentsIncident

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Incident Name | [optional] 
**status** | **str** | Incident status | [optional] 
**impact_override** | **str** | value to override calculated impact value | [optional] 
**scheduled_for** | **datetime** | The timestamp the incident is scheduled for. | [optional] 
**scheduled_until** | **datetime** | The timestamp the incident is scheduled until. | [optional] 
**scheduled_remind_prior** | **bool** | Controls whether to remind subscribers prior to scheduled incidents. | [optional] 
**scheduled_auto_in_progress** | **bool** | Controls whether the incident is scheduled to automatically change to in progress. | [optional] 
**scheduled_auto_completed** | **bool** | Controls whether the incident is scheduled to automatically change to complete. | [optional] 
**metadata** | [**object**](.md) | Attach a json object to the incident. All top-level values in the object must also be objects. | [optional] 
**deliver_notifications** | **bool** | Deliver notifications to subscribers if this is true. If this is false, create an incident without notifying customers. | [optional] [default to True]
**auto_transition_deliver_notifications_at_end** | **bool** | Controls whether send notification when scheduled maintenances auto transition to completed. | [optional] 
**auto_transition_deliver_notifications_at_start** | **bool** | Controls whether send notification when scheduled maintenances auto transition to started. | [optional] 
**auto_transition_to_maintenance_state** | **bool** | Controls whether change components status to under_maintenance once scheduled maintenance is in progress. | [optional] 
**auto_transition_to_operational_state** | **bool** | Controls whether change components status to operational once scheduled maintenance completes. | [optional] 
**auto_tweet_at_beginning** | **bool** | Controls whether tweet automatically when scheduled maintenance starts. | [optional] 
**auto_tweet_on_completion** | **bool** | Controls whether tweet automatically when scheduled maintenance completes. | [optional] 
**auto_tweet_on_creation** | **bool** | Controls whether tweet automatically when scheduled maintenance is created. | [optional] 
**auto_tweet_one_hour_before** | **bool** | Controls whether tweet automatically one hour before scheduled maintenance starts. | [optional] 
**backfill_date** | **str** | TimeStamp when incident was backfilled. | [optional] 
**backfilled** | **bool** | Controls whether incident is backfilled. If true, components cannot be specified. | [optional] 
**body** | **str** | The initial message, created as the first incident update. | [optional] 
**components** | [**PostPagesPageIdIncidentsIncidentComponents**](PostPagesPageIdIncidentsIncidentComponents.md) |  | [optional] 
**component_ids** | **list[str]** | List of component_ids affected by this incident | [optional] 
**scheduled_auto_transition** | **bool** | Same as :scheduled_auto_transition_in_progress. Controls whether the incident is scheduled to automatically change to in progress. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


