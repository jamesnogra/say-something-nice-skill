from mycroft import MycroftSkill, intent_file_handler


class SaySomethingNice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nice.something.say.intent')
    def handle_nice_something_say(self, message):
        person_name = message.data.get('person_name')

        self.speak_dialog('nice.something.say', data={
            'person_name': person_name
        })


def create_skill():
    return SaySomethingNice()

