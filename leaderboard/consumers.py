from channels.generic.websocket import AsyncWebsocketConsumer


class LeadersConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('leaders', self.channel_name)
        await self.accept()

    async def connect(self, code):
        await self.channel_layer.group_discard('leaders', self.channel_name)
