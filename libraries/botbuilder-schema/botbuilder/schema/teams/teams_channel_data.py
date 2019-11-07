# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

from botbuilder.schema.teams import ChannelInfo, TeamInfo, NotificationInfo, TenantInfo 

class TeamsChannelData:
    def __init__(self, 
                channel: ChannelInfo = None, 
                eventType = "", 
                team: TeamInfo = None, 
                notification: NotificationInfo = None, 
                tenant: TenantInfo = None):
        self._channel = ChannelInfo(**channel) if channel is not None else ChannelInfo()
        self._event_type = eventType 
        self._team = TeamInfo(**team) if team is not None else TeamInfo()
        self._notification = NotificationInfo(**notification)  if notification is not None else NotificationInfo()
        self._tenant = TenantInfo(**tenant) if tenant is not None else TenantInfo()
        
    
    def get_channel(self):
        return self._channel
    
    def set_channel(self, channel):
        self._channel = channel
    
    def get_event_type(self):
        return self._event_type
        
    def set_event_type(event_type):
        self._event_type = event_type
    
    def get_team(self):
        return self._team
    
    def set_team(self, team):
        self._team = team
    
    def get_notification(self):
        return self._notification
    
    def set_notification(self, notification):
        self._notification = notification
    
    def get_tenant(self):
        return self._tenant
    
    def set_tenant(self):
        return self._tenant

    event_type = property(get_event_type, set_event_type)
    channel = property(get_channel, set_channel)
    team = property(get_team, set_team)
    notification = property(get_notification, set_notification)
    tenant = property(get_tenant, set_tenant)