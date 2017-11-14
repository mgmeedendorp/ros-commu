from dialogue import DialogueLineNoResponse, Dialogue, DialogueLineBinaryResponse, DialogueLineAnyResponse
from dialogue_manager import DialogueLibrary


class CommUDialogueLibrary(DialogueLibrary):
    """
    A DialogueLibrary that can be used when a CommU robot sees an object.
    """


    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The pre-scripted Dialogue concerning the object.
        """
        return CommUDialogueLibrary.dialogue_map[topic]


    dialogue_map = {
        'aeroplane': None,
        'bicycle': None,
        'bird': None,
        'boat': None,
        'bottle':
            Dialogue(
                DialogueLineAnyResponse("What are you drinking?", False,
                    DialogueLineNoResponse("That sounds tasty", True,
                        DialogueLineBinaryResponse("Do you like orange juice?", False,
                            next_line_yes= DialogueLineNoResponse("That's nice! Me too!", True, None),
                            next_line_no = DialogueLineNoResponse("That's a shame. I like it a lot", True, None)
                        )
                    )
                )
            ),
        'bus': None,
        'car': None,
        'cat':
            Dialogue(
                DialogueLineNoResponse("I see you have a cat", True,
                    DialogueLineNoResponse("I love cats!", True,
                        DialogueLineNoResponse("I especially like black cats", True,
                            DialogueLineBinaryResponse("Do you like cats too?", False,
                                next_line_yes= DialogueLineNoResponse("Good!", True, None),
                                next_line_no=  DialogueLineNoResponse("That's a shame", True, None)
                            )
                        )
                    )
                )
            ),
        'chair':
            Dialogue(
                DialogueLineNoResponse("That's a nice chair.", True,
                    DialogueLineNoResponse("I've always liked that kind of chair", True,
                        DialogueLineBinaryResponse("Do you like it?", False,
                            next_line_yes = DialogueLineNoResponse("That's nice", True, None),
                            next_line_no = DialogueLineNoResponse("I still think it's cool", True, None)
                        )
                    )
                )
            ),
        'cow': None,
        'diningtable':
            Dialogue(
                DialogueLineBinaryResponse("I see you have a table. Do you like it?", False,
                    next_line_yes = DialogueLineNoResponse("Yeah, me too!", True, None),
                    next_line_no = DialogueLineNoResponse("I think it seems somewhat inconvenient as well", True, None)
                )
            ),
        'dog': None,
        'horse': None,
        'motorbike': None,
        'person':
            Dialogue(
                DialogueLineNoResponse("Hey there, nice to meet you!", True,
                    DialogueLineAnyResponse("Can I ask you a question?", False,
                        DialogueLineBinaryResponse("Have you ever talked to a robot before?", False,
                            next_line_yes = DialogueLineAnyResponse("Cool, what was his name?", False,
                                DialogueLineNoResponse("I met him yesterday, he's such a nice person!", True,
                                    DialogueLineNoResponse("Let's have a chat.", True, None)
                                )
                            ),
                            next_line_no  = DialogueLineNoResponse("Well, there's a first time for everything.", True,
                                DialogueLineNoResponse("Let's have a chat.", True, None)
                            )
                        )
                    )
                )
            ),
        'pottedplant':
            Dialogue(
                DialogueLineNoResponse("Nice plant you have there", True,
                    DialogueLineNoResponse("I like it a lot", True, None)
                )
            ),
        'sheep': None,
        'sofa':
            Dialogue(
                DialogueLineNoResponse("I love sofas!", True,
                    DialogueLineBinaryResponse("Did you know that sofas can also be used to sleep on?", False,
                        next_line_yes = DialogueLineNoResponse("I won't be able to tell you anything new today then.", True, None),
                        next_line_no  = DialogueLineNoResponse("You learn something new every day.", True, None)
                    )
                )
            ),
        'train': None,
        'tvmonitor':
            Dialogue(
                DialogueLineAnyResponse("What are you using that screen over there for?", False,
                    DialogueLineNoResponse("Cool, I like to do that too.", True, None)
                )
            ),
    }