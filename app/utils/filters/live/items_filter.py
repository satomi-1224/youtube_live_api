from typing import List
from schemas.live.responses.items_response import ItemsResponse
from schemas.live.requests.items_request import ItemsRequest
from schemas.live.live_schema import LiveSchema
from dateutil import parser


class ItemsFilter():
    @staticmethod
    def filter(request: ItemsRequest, lives: List[LiveSchema]) -> List[ItemsResponse]:
        if request.channelId != None:
            lives = [
                live for live in lives 
                if request.channelId == live['creator']['channelId']
            ]
            
        if request.channelTag != None:
            lives = [
                live for live in lives 
                if request.channelTag == live['creator']['channelTag']
            ]
            
        if request.tag != None:
            lives = [
                live for live in lives 
                if request.tag in live['creator']['tag']
            ]
            
        if request.title != None:
            lives = [
                live for live in lives 
                if request.title in live['title']
            ] 
            
        if request.status != None:
            lives = [
                live for live in lives 
                if request.status == live['status']
            ]
            
        if request.status != None:
            lives = [
                live for live in lives 
                if request.status == live['status']
            ]
            
        if request.startDatetimeFrom != None:
            lives = [
                live for live in lives 
                if request.startDatetimeFrom <= parser.parse(live['startDatetime'])
            ]
            
        if request.startDatetimeTo != None:
            lives = [
                live for live in lives 
                if request.startDatetimeTo >= parser.parse(live['startDatetime'])
            ]
            
        if request.endDatetimeFrom != None:
            lives = [
                live for live in lives 
                if request.endDatetimeFrom <= parser.parse(live['endDatetime'])
            ]
            
        if request.endDatetimeTo != None:
            lives = [
                live for live in lives 
                if request.endDatetimeTo >= parser.parse(live['endDatetime'])
            ]
        
        if request.limit != None and request.limit <= len(lives):
            lives = lives[:request.limit]
            
        return lives