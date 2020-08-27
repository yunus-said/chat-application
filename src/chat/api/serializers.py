from rest_framework import serializers

from chat.models import Chat, Contact
from chat.views import get_user_contact


class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    # print('participants: ', participants)
    # indicator = serializers.SerializerMethodField()
    # otherParticipants = []
    #
    # peer = None
    # for participant in participants:
    #     if participants[i] != this.props.username:
    #       # otherParticipants.append(c.participants[i])
    #       peer = participants[i]
    #       break
    #
    # def get_indicator(self, instance):
    #     TODO Return if the peer user is currently connected by checking the difference between connections and disconnections
    #     remainder = peer.connectionCount % 2
    #     if remainder is 0:
    #         return 'offline'
    #     else:
    #         return 'online'

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants')
        # fields = ('id', 'messages', 'participants', 'indicator')
        read_only = ('id')

    def create(self, validated_data):
        print(validated_data)
        participants = validated_data.pop('participants')
        chat = Chat()
        chat.save()
        for username in participants:
            contact = get_user_contact(username)
            chat.participants.add(contact)
        chat.save()
        return chat


# do in python shell to see how to serialize data

# from chat.models import Chat
# from chat.api.serializers import ChatSerializer
# chat = Chat.objects.get(id=1)
# s = ChatSerializer(instance=chat)
# s
# s.data
